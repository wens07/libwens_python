# symbol.py
# Author: wengqiang
# Date Last Modified: 15:15 2017/11/21
#
# Changelog:
#  
#     
#
# Usage:
#    
#     

#!/usr/bin/env python
# coding=utf-8

import requests

def get_ticker_of_symbol(url, symbol, param):

    if symbol == "":
        print("parameter symbol should not be empty! exit function get_ticker_of_symbol")
        return
    if param == None:
        print("parameter param should not be empty! exit function get_ticker_of_symbol")
        return

    response = requests.request("GET", url, params=param)
    content = response.json()
    # print(content)

    # get the certain  content
    print("%s: current price %s, lowest price %s, highest price %s, "%(str.upper(symbol), content["lastPrice"], content["lowPrice"], content["highPrice"]), end=' ')
    print("bid %s, ask %s, volume %s"%(content["bidPrice"], content["askPrice"], content["volume"]))

    return content
