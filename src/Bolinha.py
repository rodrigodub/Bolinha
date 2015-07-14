#! /usr/bin/python3
# -*- coding: windows-1252 -*-

#################################################
#                   Bolinha
# Bolinha is a script to process LAS files
#
# v0.1.009
# for Issues #3 #7
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
        self.tops_list = self.setTopsList(self.inputFile)

    def readFile(self, filename):
        """Method to read the input file contents"""
        return LHFile(filename).readInfo()

    def setTopsList(self, inputFile):
        """Method to return the list of TOPS sections in the input file"""
        return [i[:-1] for i in inputFile if '~TOPS_DEFINITION' in i]


# test loop
def test():
    print('------------------------')
    print('Test.')
    print('------------------------')
    # Unix
    # a = '/Users/rodrigo/GitHub/Bolinha/test/'
    # Windows
    # a = r'C:\GitHub\Bolinha\test'
    # 'C:\GitHub\Bolinha\test\KRC4400_8-4-4.las'
    # 'C:\GitHub\Bolinha\test\v5-AKN1129.las'
    # 'C:\GitHub\Bolinha\test\v5-AIA1492.las'
    # 'C:\GitHub\Bolinha\test\v5-Boliden Renström 2014_REF2823.las'
    # 'C:\GitHub\Bolinha\test\v5-AKN1116.las'
    # 'C:\GitHub\Bolinha\test\v5-KRC4402_8-4-4.las'
    # b = ['KRC4400_8-4-4.las', 'v5-AKN1129.las'
    # , 'v5-AIA1492.las'
    # , 'v5-Boliden Renström 2014_REF2823.las'
    # , 'v5-AKN1116.las', 'v5-KRC4402_8-4-4.las']
    a = Las2csv()
    # [print(i) for i in a.inputFile]
    [print(i) for i in a.tops_list]


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()
