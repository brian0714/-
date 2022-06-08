import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')

predict_results = pd.read_csv('DB_csv/predict_results.csv',encoding='ANSI')
#print(models_results.info())

def draw_compare_plot(stock_no):
    stock_no = str(stock_no)
    stock_no_data = pd.read_csv('stocks_csv/{}.csv'.format(stock_no),encoding='UTF-8')
    stock_no_data.replace(('--'),(np.NaN),inplace=True)
    stock_no_data['漲跌價差'].replace( ('X0.00'),(np.NaN) , inplace=True)
    stock_no_data = stock_no_data.dropna(axis=0,how='any')    

    y_test = stock_no_data['收盤價'][:365].values.tolist()
    #print('實際',y_test)
    y_test.reverse()
    y_test = [float(i) for i in y_test]
    ytest = np.array(y_test)
    #print('實際',y_test)


    y_pred = predict_results[stock_no].values.tolist()
    #print('預測',y_pred)
    y_pred.reverse()
    y_pred = [round(i,2) for i in y_pred]
    ypred = np.array(y_pred)
    #print('預測',y_pred)

    
    plt.plot(ytest,color='blue', label='Answer')
    plt.plot(ypred,color='red', label='Prediction')

    plt.legend(loc='best')
    #plt.show()
    plt.savefig('compare_img/{}_compare.png'.format(stock_no))
    plt.close()

#draw_compare_plot(2317)

#for stock_no in models_results['stock_no']:
 #   draw_compare_plot(stock_no)


from sklearn.metrics import mean_squared_error, r2_score

def calculate_performance(stock_no, days):
    stock_no = str(stock_no)
    stock_no_data = pd.read_csv('original_stocks_csv/{}.csv'.format(stock_no),encoding='UTF-8')
    stock_no_data.replace(('--'),(np.NaN),inplace=True)
    stock_no_data['漲跌價差'].replace( ('X0.00'),(np.NaN) , inplace=True)
    stock_no_data = stock_no_data.dropna(axis=0,how='any')    

    n = days
    y_test = stock_no_data['收盤價'][:n].values.tolist()
    y_test.reverse()
    y_test = [float(i) for i in y_test]
    ytest = np.array(y_test)


    y_pred = predict_results[stock_no][:n].values.tolist()
    y_pred.reverse()
    ypred = np.array(y_pred)

    
    def MAPE(Y_actual,Y_Predicted):
        mape = np.mean(np.abs((Y_actual - Y_Predicted)/Y_actual))*100
        return mape

    #print('平均股價:',np.mean(y_test))
    #print('MSE:',mean_squared_error(y_test, y_pred))
    #print('rMSE:',np.sqrt(mean_squared_error(ytest, ypred)))
    #print('MAPE:',MAPE(ytest, ypred))
    #print('r2:', r2_score(ytest, ypred))
    rMSE = np.sqrt(mean_squared_error(ytest, ypred))
    mape = MAPE(ytest, ypred)
    return rMSE, mape

#rmse_20, mape_20 = calculate_performance(1101,20)

'''stock_p = pd.read_csv('stocks_csv/{}.csv'.format(2317),encoding='UTF-8')
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
test_closes = stock_p['close'].values.tolist()[:96]
test_closes.reverse()

predicts = [105.87002, 104.83872, 104.288734, 104.19173, 104.56517, 104.88908, 104.73034, 104.12549, 103.67225, 104.95175, 106.272606, 106.70105, 106.19387, 105.4269, 104.90428, 104.89754, 104.61099, 104.1096, 103.761795, 103.58424, 103.37921, 102.91319, 102.71357, 102.7903, 102.61901, 102.60112, 103.44688, 104.73018, 105.71579, 106.1057, 105.60091, 104.84052, 104.74552, 105.1744, 105.46891, 105.68123, 105.4425, 105.13462, 104.320206, 103.52675, 103.558754, 103.96423, 104.27653, 104.57877, 104.114265, 103.05197, 102.17468, 102.12841, 102.63277, 102.82562, 102.29893, 101.772354, 102.25731, 103.64894, 104.504875, 104.54035, 104.739334, 105.38493, 105.85325, 106.01335, 105.8977, 105.70058, 105.71675, 105.40839, 105.089005, 104.39967, 103.63881, 102.90622, 102.35205, 102.66907, 103.32734, 103.468605, 103.138245, 102.63232, 102.540794, 102.7317, 103.04648, 102.41415, 101.563736, 100.83013, 100.752495, 101.23115, 101.8359, 102.72018, 103.63969, 104.07337, 104.12923, 104.08052, 103.72287, 103.00035, 103.00236, 103.62696, 104.322334, 105.39857, 106.515564, 106.515564]
preds = [round(p,2) for p in predicts]
ypred = np.array(preds)
ytest = np.array(test_closes)
print(ypred)
print(ytest)
plt.plot(ytest,color='blue', label='Answer')
plt.plot(ypred,color='red', label='Prediction')

plt.legend(loc='best')
plt.show()
#plt.savefig('compare_img/{}_compare.png'.format(stock_no))
#plt.close()'''
