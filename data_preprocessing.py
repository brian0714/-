import pandas as pd
import numpy as np
import state_DB
import tensorflow as tf
import keras
import datetime

#stock_no = '2317'

def model_training(stock_no):
    print('='*100)
    print('股號',stock_no)
    stock_no = str(stock_no)
    models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')
    stock_p = pd.read_csv('stocks_csv/{}.csv'.format(stock_no),encoding='UTF-8')
    print(stock_p)
    print('='*20)

    stock_p = stock_p.rename(columns={
        '日期':'date', 
        '成交股數':'trade_num', 
        '成交金額':'trade_p', 
        '開盤價':'open', 
        '最高價':'high', 
        '最低價':'low', 
        '收盤價':'close', 
        '漲跌價差':'price_dif', 
        '成交筆數':'volume',
                    })


    stock_p = stock_p.drop(['Unnamed: 0',],axis=1)
    stock_p.dropna(how='any',inplace=True)

    stock_p.replace(('--'),(0.0),inplace=True)
    stock_p['price_dif'].replace( ('X0.00'),(0.0) , inplace=True)
    stock_p = stock_p.dropna(axis=0,how='any')#.astype(float)

    #stock_p_date = stock_p['date']
    #print(stock_p['date'])

    for i in range(len(models_results)):
        if str(models_results['stock_no'][i]) == str(stock_no):
            last_training_date = models_results['last_training_date'][i]

    for i in range(len(stock_p)):
        date = stock_p['date'][i] #股票最新資料時間
        #print(int(date.replace('/', '')),int(last_training_date.replace('/', '')))
        if int(date.replace('/', '')) < int(last_training_date.replace('/', '')):
            last_train_data = i
            break


    new_data = last_train_data-1
    time_frame_size = 20
    calculate_index = 300 #計算技術指標需取前300筆資料
    stock_p = stock_p[:new_data + time_frame_size + calculate_index]
    print('新資料長度:',len(stock_p)-320)

    stock_p = stock_p.drop(['date',],axis=1)
    stock_p = stock_p.sort_index(axis=0,ascending=False).astype(float)

    #指標計算
    #print(stock_p.columns)
    #print(stock_p.info())
    r_h=stock_p['high'].tolist()
    # r_h.reverse()
    r_l=stock_p['low'].tolist()
    # r_l.reverse()
    r_c=stock_p['close'].tolist()
    # r_c.reverse()
    #RSV計算
    RSV=[]
    N=9
    s=0
    for i in range(len(r_c)):
      rsv=0
      c=r_c[i]
      if i < N:
        h=max(r_h[0:i+1])
        l=min(r_l[0:i+1])
      else:
        h=max(r_h[s:i+1])
        l=min(r_l[s:i+1])
        s+=1
      rsv=100*(c-l)/(h-l)
      RSV.append(rsv)
    # print(RSV)
    #KDJ計算'
    K=[]
    prev_k=50#default=50
    for i in range(len(RSV)):
      rsv=RSV[i]
      if i != 0:
        prev_k=K[i-1]
      k=(2/3)*prev_k+((1/3)*rsv)
      K.append(k)
    # print(K)

    D=[]
    prev_d=50
    for i in range(len(K)):
      k=K[i]
      if i != 0:
        prev_d=D[i-1]
      d=(2/3)*prev_d+((1/3)*k)
      D.append(d)
    # print(D)

    J=[]
    j=0
    for k,d in zip(K,D):
      j=3*k-2*d
      J.append(j)
    # print(J)

    #MA計算
    MA=[]
    MA_kind=['MA3','MA7','MA10','MA30','MA150','MA250']
    MA_dict={'MA3':3,'MA7':7,'MA10':10,'MA30':30,'MA150':150,'MA250':250}
    for i in range(len(MA_dict)):
      N=MA_dict[MA_kind[i]]
      ma=0
      ma_N=[]
      s=0
      for i in range(len(r_c)):
        if i < N:
          ma=np.mean(r_c[0:i+1])
        else:
          ma=np.mean(r_c[s:i+1])
          s+=1
        ma_N.append(ma)
      MA.append(ma_N)
    #print(MA)

    #RSI計算
    # rs=upper/lower
    # rsi=100*(rs/(1+rs))
    rs_dif=[]
    d=0
    for i in range(len(r_c)):
      if i == 0:
        d=0
      else:
        d=r_c[i]-r_c[i-1]
      rs_dif.append(d)

    N=14
    dif_N=[]   
    RSI=[]
    s=0
    for i in range(len(rs_dif)):
      dif_N=[]
      if i < (N-1):
        dif_N=rs_dif[0:i+1]
      else:
        dif_N=rs_dif[s:i+1]
        s+=1
      upper=[]
      lower=[]
      rs=0
      rsi=0
      for d in dif_N:
        if d > 0:
          upper.append(d)
        elif d < 0:
          lower.append(d)
      if lower == []:
        rsi=100
      elif upper == []:
        rsi=0
      else:
        rs=np.mean(upper)/-(np.mean(lower))
        rsi=100*(rs/(1+rs))
      RSI.append(rsi)
    # print(rs_dif)
    # print(r_c)
    # print(RSI)

    #MACD計算
    DI=[]
    di=0
    for h,l,c in zip(r_h,r_l,r_c):
      di=(h+l+2*c)/4
      DI.append(di)

    EMA_12=[]
    N=12
    ema_12=0
    for i in range(len(DI)):
      if i < N-1:
        ema_12=0
      elif i == N-1:
        ema_12=np.mean(DI[0:i])
      else:
        ema_12=(EMA_12[i-1]*(N-1)+DI[i]*2)/(N+1)
      EMA_12.append(ema_12)

    EMA_26=[]
    N=26
    ema_26=0
    for i in range(len(DI)):
      if i < N-1:
        ema_26=0
      elif i == N-1:
        ema_26=np.mean(DI[0:i])
      else:
        ema_26=(EMA_26[i-1]*(N-1)+DI[i]*2)/(N+1)
      EMA_26.append(ema_26)

    DIF=[]
    dif=0
    for ema_12,ema_26 in zip(EMA_12,EMA_26):
      dif=ema_12-ema_26
      DIF.append(dif)

    MACD=[]
    N=9
    macd=0
    for i in range(len(DIF)):
      if i < N-1:
        macd=0
      elif i == N-1:
        macd=np.mean(DIF[0:i])
      else:
        macd=(MACD[i-1]*(N-1)+DIF[i]*2)/(N+1)
      MACD.append(macd)
    # print(MACD)


    #新增index作feature
    index=[K,D,J,RSV,MACD]

    for ma in MA:
      index.append(ma)
    stock_p['K']=K
    stock_p['D']=D
    stock_p['J']=J
    stock_p['RSI']=RSI
    stock_p['MACD']=MACD
    for n,ma in zip(MA_kind,MA):
      stock_p[n]=ma

    #調整RSV增加kdj column
    def KDJ_adjust_extension(rsv_n_list):
      r_h=stock_p['high'].tolist()
      r_l=stock_p['low'].tolist()
      r_c=stock_p['close'].tolist()

      for rsv_n in rsv_n_list:
        #RSV計算
        RSV=[]
        N=rsv_n
        s=0
        for i in range(len(r_c)):
          rsv=0
          c=r_c[i]
          if i < N:
            h=max(r_h[0:i+1])
            l=min(r_l[0:i+1])
          else:
            h=max(r_h[s:i+1])
            l=min(r_l[s:i+1])
            s+=1
          rsv=100*(c-l)/(h-l)
          RSV.append(rsv)
        # print(RSV)
        #KDJ計算'
        K=[]
        prev_k=50#default=50
        for i in range(len(RSV)):
          rsv=RSV[i]
          if i != 0:
            prev_k=K[i-1]
          k=(2/3)*prev_k+((1/3)*rsv)
          K.append(k)
        # print(K)

        D=[]
        prev_d=50
        for i in range(len(K)):
          k=K[i]
          if i != 0:
            prev_d=D[i-1]
          d=(2/3)*prev_d+((1/3)*k)
          D.append(d)
        # print(D)

        J=[]
        j=0
        for k,d in zip(K,D):
          j=3*k-2*d
          J.append(j)
        
        stock_p[('K_'+str(rsv_n))] = K
        stock_p[('D_'+str(rsv_n))] = D
        stock_p[('J_'+str(rsv_n))] = J

    rsv_n_list = [i for i in range(1,9)]
    KDJ_adjust_extension(rsv_n_list)
    #print(stock_p.columns)
    #print(len(stock_p.columns))
    # print(stock_p[['K_1','K_2']])

    #擴增殘差feature(1, 3, 7, 9, 20)+標準化

    n_dif = 1
    stock_array = stock_p.values.tolist()
    # print(stock_array)
    for col in range(len(stock_array[0])):
      for row in range(1,len(stock_array)):
        dif = stock_array[row][col] - stock_array[row - n_dif][col]
        stock_array[row].append(dif)
    # print(stock_array[1][:19])
    # print(stock_array[1][19:])
    # print(len(stock_array[1]))

    stock_array = np.array(stock_array[1:])
    from sklearn import preprocessing
    min_max_scaler = preprocessing.MinMaxScaler()
    stock_p_norm = min_max_scaler.fit_transform(stock_array)
    #print(len(stock_p_norm[0]))
    #print(stock_p_norm[-96])


    #建立滑動式窗口
    # print(stock_p_norm.columns)
    start=0
    window=[]
    def data_split(df, time_frame, calculate_index):
        # 資料維度: 開盤價、收盤價、最高價、最低價、成交量等, X維
        # number_features = len(df.columns)

        datavalue = df

        result = []
        # 若想要觀察的 time_frame 為20天, 需要多加一天做為驗證答案
        for index in range( len(datavalue) - (time_frame+1) ): # 從 datavalue 的第0個跑到倒數第 time_frame+1 個
            result.append(datavalue[index: index + (time_frame+1) ]) # 逐筆取出 time_frame+1 個K棒數值做為一筆 instance
        result = np.array(result)

        #無ground truth之明日預測
        tommorow_predict = np.array([datavalue[-time_frame:]])
        print('tommorow_predict',tommorow_predict)
        print(len(tommorow_predict))
        
        window = result
        # print(result)
        # number_train = round(0.9 * result.shape[0]) # 取 result 的前90% instance做為訓練資料

        #丟棄前n(300)筆技術指標不準之資料

        
        skip = calculate_index - 2 #calculate_index=300, 前300筆技術指標有瑕疵
        N = skip#round(0 * (result.shape[0]-skip)+skip+1)  #首次建模訓練 資料數量

        x_train = result[skip:N, :-1] # 訓練資料中, 只取每一個 time_frame 中除了最後一筆的所有資料做為feature
        y_train = result[skip:N, -1][:,5] # 訓練資料中, 取每一個 time_frame 中最後一筆資料的某個數值(取決於哪個當y)做為答案 (close:5,state:8)
        # print(N)
        #print('train size:',len(x_train))
        # print(x_train[0][0])
        # 測試資料
        x_test = result[N:N+1, :-1]
        y_test = result[N:N+1, -1][:,5]
        print('x_test',x_test)
        #print('test size:',len(x_test))
        #print(len(x_test[0]))

        start = N
        
        #無須用到train test
        
        print('矩陣size:',len(result[skip:]))
        return start, window, tommorow_predict

    # 以20天為一區間進行股價預測
    start, window, tommorow_predict = data_split(stock_p_norm, 20, calculate_index)

    #模型訓練

    model_name = "{}_model.h5".format(stock_no)
    #取得預訓練模型路徑
    save_loc = "deep_learning_model/" + model_name

    #去正規化
    def denormalize(df, norm_value):
        original_value = df['close'].values.reshape(-1,1) #state/close
        norm_value = norm_value.reshape(-1,1)
        
        min_max_scaler = preprocessing.MinMaxScaler()
        min_max_scaler.fit_transform(original_value)
        denorm_value = min_max_scaler.inverse_transform(norm_value)
        return denorm_value

    #將所有資料進行預測
    predict_closes=[]
    
    for i in range(start,len(window)):
      # Calling `save('my_model')` creates a SavedModel folder `my_model`.
      if i != start:
        reconstructed_model.save(save_loc)
      # It can be used to reconstruct the model identically.
      reconstructed_model = keras.models.load_model(save_loc)

      test_input=window[i:i+1, :-1]
      test_target=window[i:i+1, -1][:,5]
      # reconstructed_model.fit(test_input, test_target)
      reconstructed_model.fit(test_input, test_target,batch_size=128, epochs=15,verbose=0)
      # print(i)
      if i != len(window)-1:
          close_predict = reconstructed_model.predict(window[i+1:i+2, :-1])
          denorm_pred = denormalize(stock_p, close_predict)
          predict_closes.append(denorm_pred[0][0])
      if len(predict_closes) % 10 == 0:
          print(str(i-start)+'/'+str((len(window)-start)))
          print(predict_closes)

    
    #預測明日價格
    reconstructed_model = keras.models.load_model(save_loc)
    tommorow_close_predict = reconstructed_model.predict(tommorow_predict)
    denorm_tommorow_close_predict = denormalize(stock_p, tommorow_close_predict)
    denorm_tommorow_close_predict = round(denorm_tommorow_close_predict[0][0],2)
    print(denorm_tommorow_close_predict)
    
    
    
    stock_p = pd.read_csv('stocks_csv/{}.csv'.format(stock_no),encoding='UTF-8')
    stock_p = stock_p.rename(columns={
        '日期':'date', 
        '成交股數':'trade_num', 
        '成交金額':'trade_p', 
        '開盤價':'open', 
        '最高價':'high', 
        '最低價':'low', 
        '收盤價':'close', 
        '漲跌價差':'price_dif', 
        '成交筆數':'volume',
                    })
    stock_p = stock_p.drop(['Unnamed: 0',],axis=1)
    stock_p.dropna(how='any',inplace=True)

    stock_p.replace(('--'),(0.0),inplace=True)
    stock_p['price_dif'].replace( ('X0.00'),(0.0) , inplace=True)
    stock_p = stock_p.drop(['date',],axis=1)
    stock_p = stock_p.dropna(axis=0,how='any').astype(float)

    test_closes = stock_p['close'].values.tolist()[:len(predict_closes)]
    test_closes.reverse()
    print(len(predict_closes))
    predict_closes = [round(p,2) for p in predict_closes]
    print('預測價格：',predict_closes)
    print('實際價格：',test_closes)

    #將新爬取資料之預測結果更新predict_results
    predict_results = pd.read_csv('DB_csv/predict_results.csv',encoding='ANSI')
    original_preds = predict_results[stock_no].values.tolist()
    for p in predict_closes:
        original_preds.insert(0,p)
    predict_results[stock_no] = original_preds[:365]
    predict_results.to_csv('DB_csv/predict_results.csv',encoding='ANSI', index=False)
    print('已更新')
    
    #更新上次訓練時間至今日 及上傳預測價格
    return round(denorm_tommorow_close_predict,2)
    '''western_date = datetime.date.today()
    western_date_month = western_date.month
    if western_date.month < 10:
        western_date_month = '0' + str(western_date.month)
    taiwan_date = '{}/{}/{}'.format(western_date.year-1911,western_date_month,western_date.day)
    for i in range(len(models_results)):
        if str(models_results['stock_no'][i]) == str(stock_no):
            print(taiwan_date)
            modify_last_training_date = models_results['last_training_date'].values.tolist()
            print(modify_last_training_date)
            modify_last_training_date[i] = taiwan_date
            print(modify_last_training_date)
            models_results['last_training_date'] = modify_last_training_date

            modify_predict_stock_price = models_results['predict_stock_price'].values.tolist()    
            modify_predict_stock_price[i] = round(denorm_tommorow_close_predict,2)
            models_results['predict_stock_price'] = modify_predict_stock_price

            models_results.to_csv('DB_csv/models_results.csv',encoding='ANSI', index=False)
            print('Changed!')
            break'''
    #print('Done')
        
#model_training(stock_no)
#model_training(1101)
    
'''models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')
predict_closes = [105.87002, 104.83872, 104.288734, 104.19173, 104.56517, 104.88908, 104.73034, 104.12549, 103.67225, 104.95175, 106.272606, 106.70105, 106.19387, 105.4269, 104.90428, 104.89754, 104.61099, 104.1096, 103.761795, 103.58424, 103.37921, 102.91319, 102.71357, 102.7903, 102.61901, 102.60112, 103.44688, 104.73018, 105.71579, 106.1057, 105.60091, 104.84052, 104.74552, 105.1744, 105.46891, 105.68123, 105.4425, 105.13462, 104.320206, 103.52675, 103.558754, 103.96423, 104.27653, 104.57877, 104.114265, 103.05197, 102.17468, 102.12841, 102.63277, 102.82562, 102.29893, 101.772354, 102.25731, 103.64894, 104.504875, 104.54035, 104.739334, 105.38493, 105.85325, 106.01335, 105.8977, 105.70058, 105.71675, 105.40839, 105.089005, 104.39967, 103.63881, 102.90622, 102.35205, 102.66907, 103.32734, 103.468605, 103.138245, 102.63232, 102.540794, 102.7317, 103.04648, 102.41415, 101.563736, 100.83013, 100.752495, 101.23115, 101.8359, 102.72018, 103.63969, 104.07337, 104.12923, 104.08052, 103.72287, 103.00035, 103.00236, 103.62696, 104.322334, 105.39857, 106.515564, 106.515564]
predict_closes = [round(p,2) for p in predict_closes]
predict_results = pd.read_csv('DB_csv/predict_results.csv',encoding='ANSI')
original_preds = predict_results[stock_no].values.tolist()
for p in predict_closes:
    original_preds.insert(0,p)
predict_results[stock_no] = original_preds[:365]
predict_results.to_csv('DB_csv/predict_results.csv',encoding='ANSI', index=False)

    #更新上次訓練時間至今日
western_date = datetime.date.today()
western_date_month = western_date.month
if western_date.month < 10:
    western_date_month = '0' + str(western_date.month)
taiwan_date = '{}/{}/{}'.format(western_date.year-1911,western_date_month,western_date.day)
for i in range(len(models_results)):
    if str(models_results['stock_no'][i]) == stock_no:
        modify_last_training_date = models_results['last_training_date'].values.tolist()    
        modify_last_training_date[i] = taiwan_date
        models_results['last_training_date'] = modify_last_training_date
        models_results.to_csv('DB_csv/models_results.csv',encoding='ANSI', index=False)
        break
'''
        
