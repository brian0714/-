#爬證券網資料 可選年數及股號
import requests
import pandas as pd
import datetime

def crawl_stock_data(crawled_stock_no):
    crawl_state = ''
    try:
        print('股號：',crawled_stock_no)
        models_results = pd.read_csv('DB_csv/models_results.csv',encoding='ANSI')

        #models_results['last_update_date'] = ['111/05/21']*50 #強制執行底下程式碼

        last_update_year = int(models_results['last_update_date'][0].split('/')[0])+ 1911
        search_year = datetime.datetime.today().year - last_update_year + 2 #10 #抓幾年的股票資料

        month = str(datetime.datetime.today().month)
        if len(month) == 1:
            month = '0' + month
        months = ['12','11','10','09','08','07','06','05','04','03','02','01']

        #dates = [20200201, 20200101, 20191201]
        dates = []
        for i in months[months.index(month):]:
            today_date = str(datetime.datetime.today().year) + i + str(datetime.datetime.today().day)
            dates.append(int(today_date))
            
        for j in range(search_year-1):
            for k in months:
                today_date = str(datetime.datetime.today().year-(j+1)) + k + str(datetime.datetime.today().day)
                dates.append(int(today_date))
        #print(dates)
                
        #國泰金2882 #鴻海2317
        # 已爬完：2330,2454,2317,2308,2303,2881,1301,1303,2882,2002,2412,2891,2886,1216,2884,3008,2885,3034,2357,5871,2379,2382,2327,2892,5880,2207,2880,3045,2887,6505,2912,4938,1590,2395,2474,1402,1102,2801,
                        # 9910,4904,2105,8046,2408,
        # 已爬4年: 3711,1326,1101,6415,5876,2633,
        # 已爬3年: 6669,
        # 有問題(10年)：3711,1326,1101,6415,5876,6669,2633,
        
        TW_50 = []
        TW_50.append(crawled_stock_no)
        #TW_50 = models_results['stock_no'].values.tolist()

        #爬各股
        import time

        #del dates[0]#需刪除
        for no in TW_50: 
            stockNo = no
            url_template = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}"
            datas=[]
            
            stock_no_data = pd.read_csv('stocks_csv/{}.csv'.format(stockNo),encoding='UTF-8')
            #print(stock_no_data)

            last_crawl_date = stock_no_data['日期'][0].split('/')
                
            last_date = int('{}{}{}'.format(int(last_crawl_date[0]) + 1911,last_crawl_date[1],last_crawl_date[2])) #20190216 #表示上市日
            print('所有近期日期:',dates)
            for date in dates :
                print('需更新之日期:',date, last_date)
                if date < last_date:
                    break

                url = url_template.format(date, stockNo)

                data = pd.read_html(requests.get(url).text)[0]
                data.columns = data.columns.droplevel(0)
                data = data.sort_index(axis = 0, ascending = False)#排序從最新到最舊
                datas.append(data)
                time.sleep(5) #爬一頁(一個月)之等候時間(秒)
                print(stockNo,date,'Done')
            
            
            #file_name = "{}_{}.csv".format(stockNo, search_year)
            new_data = pd.concat(datas)
            new_data.insert(0, 'Unnamed: 0', [0]*len(new_data))
            #new_data.to_csv('try_crawl/'+file_name)

            old_data = stock_no_data
            for i in range(31):
                new_dates = new_data['日期'].values.tolist()
                if old_data['日期'][i] in new_dates:
                    old_data = old_data.drop([i])

            final_data = pd.concat([new_data, old_data])
            final_file_name = '{}.csv'.format(stockNo) #'final.csv'#
            final_data.to_csv('stocks_csv/' + final_file_name, encoding = 'UTF-8',index = False)
            
            print(no, ': Completed')
    except ValueError:
        crawl_state = 'crawl_error'

    return crawl_state

#crawl_stock_data('2317')
