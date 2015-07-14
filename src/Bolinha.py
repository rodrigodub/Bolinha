#! /usr/bin/python3
# -*- coding: windows-1252 -*-

#################################################
#                   Bolinha
# Bolinha is a script to process LAS files
#
# v0.1.008
# for Issue #3
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
        self.inputFileName = input('File name? ')
        self.inputFile = self.readFile(self.inputFileName)

    def readFile(self, filename):
        """Method to read the input file contents"""
        return LHFile(filename).readInfo()


# test loop
def test():
    print('------------------------')
    print('Test.')
    print('------------------------')
    # Unix
    # a = '/Users/rodrigo/GitHub/Bolinha/test/'
    # Windows
    # a = r'C:\GitHub\Bolinha\test'
    # a = input('Path? ')
    # 'C:\GitHub\Bolinha\test\KRC4400_8-4-4.las'
    # b = ['KRC4400_8-4-4.las', 'v5-AKN1129.las'
    # , 'v5-AIA1492.las'
    # , 'v5-Boliden Renström 2014_REF2823.las'
    # , 'v5-AKN1116.las', 'v5-KRC4402_8-4-4.las']
    # Unix
    # c = LHFile(a+b[1])
    # Windows
    # c = LHFile(a + '\\' + b[1])
    # d = c.readInfo()
    # [print(i) for i in d]
    a = Las2csv()
    [print(i) for i in a.inputFile]


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()
