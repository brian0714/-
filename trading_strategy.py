import pandas as pd
threshold = 0.5
def trading_strategy(predict_close, close):
    global threshold
    threshold = threshold#參數
    state = 0

    print('交易策略',predict_close, close, '價差',abs(float(predict_close) - float(close))/float(close), '門檻',threshold/100)
    predict_close = float(predict_close)
    close = float(close)
    if (abs(float(predict_close) - float(close))/float(close)) >= (threshold/100):#判斷是否小於1%
        if predict_close >  close:#做多
            state = 2
        elif predict_close < close:#做空
            state = 1
        else:
            state = 0
    else:
        #print('不交易')
        state = 0
    
    return state

'''models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')
for i in range(len(models_results)):
    if str(models_results['stock_no'][i]) == '2317':
        predict_close = models_results['predict_stock_price'][i]
        close = models_results['current_stock_price'][i]
        break

state = trading_strategy(predict_close, close)
print(state)
'''
