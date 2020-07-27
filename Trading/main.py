from connect import *

sheet = Connect("Weekly Buy-Sell", "Clean")
names = sheet.row_values(1)


def filterData(a, b):
    # a, b is the range of rows which need to be processed
    # this function will return a list of dictionarys with col names as keys and row as values, eg:
    '''{'Timestamp': '12/07/2020', 'Call': 'Long', 'Stock Name': 'ULTRACEMCO', 'Stop Loss': '3740', 'Price': '3790', 
    'Target': '4030', 'SL%': '1.32%', 'Target%': '6.33%', 'Risk/Reward': '0.21', 'Live': '3870', 'Dlow': '3781', 
    'DHigh': '3901', 'Trade': '', 'Status': '', 'Trade_LTP': '3779.5', 'Trade_Low': '3735', 'Trade_High': '3869'}'''
    # for every row there will be one dictionary element present
    mix = []
    range_data = sheet.get("A{}:Q{}".format(a, b))
    for i in range(len(range_data)):
        temp = {}
        for j in range(len(names)):
            temp[names[j]] = range_data[i][j]
        mix.append(temp)
    return mix


print(filterData(2, 19))
