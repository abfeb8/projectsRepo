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
        if float(row["Trade_LTP"]) <= float(row["Stop Loss"]):
            row["Status"] = 'Stoped'
            row["Trade"] = "Exit"  # will marke the trade as complete
        else:
            row["Status"] = 'Between'


def checkTatget(row):  # check if the stock has hit target price or not
    if row["Trade"] == "In":
        if float(row["Trade_LTP"]) >= float(row["Target"]):
            row["Status"] = 'Target'
            row["Trade"] = "Exit"  # will marke the trade as complete
        else:
            row["Status"] = 'Between'


def update2Sheet():   # write the updated data to google sheet
    updatedData = []
    for i in rows:
        updatedData.append([i["Trade"], i["Status"], float(i["Trade_LTP"]),
                            float(i["Trade_Low"]), float(i["Trade_High"])])
    sheet.update('M{}:Q{}'.format(a, b), updatedData)


def updatPrice(row):
    # check if trade is Exited or not
    if row["Trade"] != "Exit":
        try:
            # update Trade_LTP
            row["Trade_LTP"] = float(row["Live"])
            # update Trade_Low price
            if float(row["Trade_Low"]) > float(row["DLow"]):
                row["Trade_Low"] = row["DLow"]
            # update Trade_high price
            if float(row["Trade_High"]) < float(row["DHigh"]):
                row["Trade_High"] = row["DHigh"]
        except Exception:
            pass


a, b = [2, 19]
rows = filterData(a, b)

for i in rows:
    updatPrice(i)
    tradeConfirmation(i)
    checkTatget(i)
    checkStop(i)
update2Sheet()
