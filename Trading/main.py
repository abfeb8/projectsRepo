from connect import *

sheet = Connect("Weekly Buy-Sell", "Clean")
names = sheet.row_values(1)


def filterData(a, b):  # will return a list of dictionary containg rows to be processed
    # a, b is the range of rows which need to be processed
    # this is an examle of an element of the list
    '''{'Call': 'Long',
        'DHigh': '447.3',
        'Dlow': '436.55',
        'Live': '443.15',
        'Price': '446.3',
        'Risk/Reward': '0.27',
        'SL%': '1.68%',
        'Status': '',
        'Stock Name': 'CONCOR',
        'Stop Loss': '438.8',
        'Target': '474.3',
        'Target%': '6.27%',
        'Timestamp': '26/07/2020',
        'Trade': '',
        'Trade_High': '447.3',
        'Trade_LTP': '443.15',
        'Trade_Low': '436.55'}'''
    # for every row there will be one dictionary element present
    mix = []
    range_data = sheet.get("A{}:Q{}".format(a, b))
    for i in range(len(range_data)):
        temp = {}
        for j in range(len(names)):
            temp[names[j]] = range_data[i][j]
        mix.append(temp)
    return mix


def tradeConfirmation(row):  # check wethere a trade has been taken or not
    if row["Call"] == "Long":
        try:
            if float(row["Trade_Low"]) <= float(row["Price"]):
                row["Trade"] = 'In'
                return True
            else:
                row['Trade'] = 'Out'
                return False
        except Exception:
            print(">>Something wrong with ", row["Stock Name"])

    else:
        # short position
        if row["Call"] == "Short":
            try:
                if float(row["Trade_Low"]) >= float(row["Price"]):
                    row["Trade"] = 'In'
                    return True
                else:
                    row['Trade'] = 'Out'
                    return False
            except Exception:
                print(">>Something wrong with ", row["Stock Name"])


def checkStop(row):  # check if the stock has hit stop loss or not
    if row["Trade"] == "In":
        if row["Trade_LTP"] <= row["Stop Loss"]:
            row["Status"] = 'Stoped'
            row["Trade"] = "Complet"  # will marke the trade as complete
        else:
            row["Status"] = 'Between'


def checkTatget(row):  # check if the stock has hit target price or not
    if row["Trade"] == "In":
        if row["Trade_LTP"] >= row["Target"]:
            row["Status"] = 'Target'
            row["Trade"] = "Complet"  # will marke the trade as complete
        else:
            row["Status"] = 'Between'


rows = filterData(2, 19)
for i in rows:
    tradeConfirmation(i)
    checkStop(i)
    checkTatget(i)
    print(i["Stock Name"], i["Trade"], i["Status"])
