# Long做多程序
# 分析：第一题做多无初始资金，每次交易假定为买一份或者卖一份

import pandas as pd;

hold_number = 0  # 定义一个持有股票数量的变量，初始值为0
buy_price = 0.0  # 定义购买股票时候的价格变量
sell_price = 0.0  # 定义出售股票的时候的价格变量
ma = 240  # 定义ma的值，为240日
sumProfit = 0.0  # 定义收益变量

df = pd.read_excel("399300.xlsx");
date_close_price = df["closePrice"].values  # 读取收盘价
date_open_price = df["openPrice"].values  # 读取开盘价


def get_ma(current_ma, current_day):  # 计算ma日均线
    average_ma = 0.0
    for j in range(current_ma):
        average_ma += date_close_price[current_day-j]

    average_ma = average_ma / ma
    return average_ma


for i in range(len(date_close_price) - 1):
    today_close_price = date_close_price[i]  # 获取当日收盘价
    yesterday_close_price = date_close_price[i - 1]  # 获取昨日收盘价
    if i <= ma:
        continue  # 为达到生成第二个均线数据之前，不发生任何交易
    else:
        today_ma = get_ma(ma, i)
        yesterday_ma = get_ma(ma, i-1)
        if (today_close_price > today_ma) and (yesterday_close_price < yesterday_ma):  # 达到买入信号，买入
            hold_number = 1  # 默认买入为一份
            buy_price = date_open_price[i+1]  # 设定买入价格
        elif (today_close_price < today_ma) and (yesterday_close_price > yesterday_ma):
            sell_price = date_open_price[i+1]  # 设定卖出价格
            sumProfit += (sell_price-buy_price)*hold_number-sell_price*hold_number*0.0005  # 计算收益
            hold_number = 0  # 卖出后手中持有股票为0

print(sumProfit)
