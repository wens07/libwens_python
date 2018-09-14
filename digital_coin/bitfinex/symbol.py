# symbol.py
# Author: wengqiang
# Date Last Modified: 10:54 2017/11/21
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
import string


def get_all_coin_symbols(url):
    response = requests.request("GET", url)

    return response.text


def get_all_coin_symbols_detail(url, symbol=""):
    result = []
    response = requests.request("GET", url)
    content = response.json()

    # print(content)

    if symbol != "":
        for i in range(len(content)):
            if symbol in content[i]["pair"]:
                result.append(content[i])

        # print(result)
        return result
    else:
        # print(content)
        return content

def get_ticker_of_symbol(url, symbol):
    if symbol == "":
        print("parameter symbol should not be empty! exit function get_ticker_of_symbol")
        return
    url += symbol

    response = requests.request("GET", url)
    content = response.json()

    # get the certain  content
    print("%s: current price %s, lowest price %s, highest price %s, "%(str.upper(symbol), content["last_price"], content["low"], content["high"]), end=' ')
    print("bid %s, ask %s, volume %s"%(content["bid"], content["ask"], content["volume"]))

    return content


