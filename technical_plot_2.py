import yfinance as y 
import pandas as p 
import plotly.graph_objects as g
import state_DB

def draw_technical_plot(stock_no):
    #上市股: '股票代碼.tw'
    #上櫃股: '股票代碼.two'
    stock = y.download(stock_no+'.tw', period='1d', interval='1m')

    #c_name = y.Ticker(stock_no+'.tw')
    #print(c_name.info['longName'])

    data = stock.reset_index()
    data.columns = ['現在時間', '開盤價', '最高價', '最低價', '收盤價', '調整後收盤價', '成交量']
    data['現在時間'] = p.to_datetime(data['現在時間'].dt.strftime('%Y-%m-%d %H:%M'))
    data['成交量'] //= 1000  #把單位從成交股數換成成交張數

    result = g.Figure()

    #成交量的圖
    result.add_trace(
        g.Bar(
            name = '成交量',
            x = data['現在時間'],
            y = data['成交量'],
            yaxis = 'y2',
            marker_color = '#99ccff'
        )
    )

    #k線圖
    result.add_trace(
        g.Candlestick(
            name = 'K線圖',
            x = data['現在時間'],
            open = data['開盤價'],
            high = data['最高價'],
            low = data['最低價'],
            close = data['收盤價'],
            increasing_line_color = '#fd5047',
            increasing_fillcolor = '#f29696',
            decreasing_line_color = '#3d9970',
            decreasing_fillcolor = '#91c2b3'
        )
    )

    result.update_layout(
        #title = stock_no,
        hovermode = 'x unified', #滑鼠停在圖上的時候會有資訊卡
        #xaxis_rangeslider_visible = False, #x軸座標的小圖，可以用來滑動上面的圖

        #yaxis = dict(title = '股價'),

        #yaxis2為成交量之y軸座標
        yaxis2 = dict(
            overlaying = 'y',
            visible = False
        ),

        font = dict(
            size = 20
        )
    )

    #水平置上呈現圖例(預設plotly右側)
    result.update_layout(legend=dict( orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1 ))
    
    #result.show()
    import plotly.express as px
    result.write_html("technical_plot.html")

#draw_technical_plot(state_DB.info_title_name)
