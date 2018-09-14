# bitfinex_test.py
# Author: wengqiang
# Date Last Modified: 10:50 2017/11/21
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

from datetime import datetime
import os
from digital_coin import bitfinex
from digital_coin import binance
from digital_coin import poloniex

def get_concerned_prices():
    # price on poloniex
    # poloniex_api.symbol.get_ticker_of_my_concerned()


    # price on bitfinex
    bitfinex_urlticker = "https://api.bitfinex.com/v1/pubticker/"

    print("%s The price in bitfinex:"%(datetime.now()))
    bitfinex.symbol.get_ticker_of_symbol(bitfinex_urlticker, "btcusd")
    print()
    bitfinex.symbol.get_ticker_of_symbol(bitfinex_urlticker, "ethusd")
    bitfinex.symbol.get_ticker_of_symbol(bitfinex_urlticker, "ethbtc")
    print()
    bitfinex.symbol.get_ticker_of_symbol(bitfinex_urlticker, "etpusd")

    print("\n\n\n")
    # price on binance
    print("%s The price in binance:"%(datetime.now()))
    binance_urlticker = "https://api.binance.com/api/v1/ticker/24hr"
    symbol = "BTCUSDT"
    param = {
        'symbol': symbol
    }
    binance.symbol.get_ticker_of_symbol(binance_urlticker,symbol, param)
    print()

    symbol = "ETHUSDT"
    param = {
        'symbol': symbol
    }
    binance.symbol.get_ticker_of_symbol(binance_urlticker,symbol, param)
    symbol = "ETHBTC"
    param = {
        'symbol': symbol
    }
    binance.symbol.get_ticker_of_symbol(binance_urlticker,symbol, param)
    print()

    symbol = "BTSBTC"
    param = {
        'symbol': symbol
    }
    binance.symbol.get_ticker_of_symbol(binance_urlticker,symbol, param)
    symbol = "BTSETH"
    param = {
        'symbol': symbol
    }
    binance.symbol.get_ticker_of_symbol(binance_urlticker,symbol, param)





if __name__ == '__main__':

    while(True):
        get_concerned_prices()

        incontent = input("please enter any key to continue or 'e' to exit program! ")
        if(incontent == 'e'):
            break
        else:
            continue



# os.system("pause")

