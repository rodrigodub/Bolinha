#! /usr/bin/python3
# -*- coding: windows-1252 -*-

#################################################
#                   Bolinha
# Bolinha is a script to process LAS files
#
# v0.1.006
# for Issue #10
#
# Rodrigo Nobrega
# 20150709-20150714
#################################################
__author__ = 'Rodrigo Nobrega'

# import modules
# import os
# import datetime
from Littlehelper import LHFile


# Las2csv()
class Las2csv(object):
    """
    Class to convert LAS 3.0 file into CSVs
    """
    def __init__(self):
        pass


# test loop
def test():
    print('------------------------')
    print('Test.')
    print('------------------------')
    # a = '/Users/rodrigo/GitHub/Bolinha/test/'
    a = r'C:\GitHub\Bolinha\test'
    b = ['KRC4400_8-4-4.las', 'v5-AKN1129.las'
    , 'v5-AIA1492.las'
    , 'v5-Boliden Renström 2014_REF2823.las'
    , 'v5-AKN1116.las', 'v5-KRC4402_8-4-4.las']
    # c = LHFile(a+b[1])
    c = LHFile(a + '\\' + b[2])
    d = c.readInfo()
    [print(i) for i in d]


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()
