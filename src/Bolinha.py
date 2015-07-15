#! /usr/bin/python3
# -*- coding: windows-1252 -*-

#################################################
#                   Bolinha
# Bolinha is a script to process LAS files
#
# v0.1.015
# for Issues #13
#
# Rodrigo Nobrega
# 20150709-20150715
#################################################
__author__ = 'Rodrigo Nobrega'

# import modules
# import os
# import datetime
from Littlehelper import LHFile


# Las2csv()
class Las2csv(object):
    """
    Class to convert LAS 3.0 file into CSVs.
    Attributes:
    inputFileName : string - path/file name
    inputFile : list - the file contents, each line an item
    topsList : list - list of TOPS sections on file
    topsFields : list - list of trios [top section, top name, [field1, field2, ..., fieldn]]
    topsData : list - list of data from each TOPS section as [top section, [d1, d2, ..., dn]]
    """
    def __init__(self):
        self.inputFileName = input('File name? ')
        self.inputFile = self.readFile(self.inputFileName)
        self.topsList = self.setTopsList(self.inputFile)
        self.topsFields = self.setTopsFields(self.inputFile, self.topsList)
        self.topsData = self.setTopsData(self.inputFile, self.topsList)

    def readFile(self, filename):
        """Method to read the input file contents"""
        return LHFile(filename).readInfo()

    def setTopsList(self, inputfile):
        """Method to return the list of TOPS sections in the input file"""
        return [i[:-1] for i in inputfile if '~TOPS_DEFINITION' in i]

    def setTopsFields(self, inputfile, topslist):
        """Method to define the list of fields for each TOPS section"""
        # resulting list to output
        result = []
        for i in topslist:
            # each ~TOPS_DEFINITION section
            tops = []
            tops.append(i)
            # finds the inputFile index of the ~TOPS_DEFINITION
            idx = inputfile.index(i+'\n')
            # takes the third line as the TOP NAME
            tops.append(inputfile[idx+3].split(':')[1]
                        .replace(' Lithology      {S}\n', '').replace(' Symbol      {S}\n', ''))
            # list of field names
            fields = []
            while inputfile[idx+3] != '#------------------------------------------------------------\n':
                fields.append(inputfile[idx+3].split(':')[1]
                              .replace('      {S}\n', '').replace('      {F}\n', '').replace('      {I}\n', ''))
                idx += 1
            tops.append(fields)
            result.append(tops)
        return result

    def setTopsData(self, inputfile, topslist):
        """Method to read and return the real section data to a list"""
        # resulting list to output
        result = []
        for i in topslist:
            # each ~TOPS_DEFINITION section
            tops = []
            tops.append(i)
            # finds the inputFile index of the ~TOPS_DEFINITION
            idx = inputfile.index(i+'\n')
            # skip until first separator
            while inputfile[idx] != '#------------------------------------------------------------\n':
                idx += 1
            # skip until first data line
            idx += 2
            data = []
            # iterate until next separator, marking end of data
            while idx < len(inputfile) and inputfile[idx] != '#------------------------------------------------------------\n':
                data.append(inputfile[idx])
                idx += 1
            tops.append(data)
            result.append(tops)
        return result


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
    # '/Users/rodrigo/GitHub/Bolinha/test/KRC4400_8-4-4.las'
    # 'C:\GitHub\Bolinha\test\v5-AKN1129.las'
    # 'C:\GitHub\Bolinha\test\v5-AIA1492.las'
    # 'C:\GitHub\Bolinha\test\v5-Boliden Renström 2014_REF2823.las'
    # '/Users/rodrigo/GitHub/Bolinha/test/v5-Boliden Renström 2014_REF2823.las'
    # 'C:\GitHub\Bolinha\test\v5-AKN1116.las'
    # 'C:\GitHub\Bolinha\test\v5-KRC4402_8-4-4.las'
    # b = ['KRC4400_8-4-4.las', 'v5-AKN1129.las'
    # , 'v5-AIA1492.las'
    # , 'v5-Boliden Renström 2014_REF2823.las'
    # , 'v5-AKN1116.las', 'v5-KRC4402_8-4-4.las']
    a = Las2csv()
    # [print(i) for i in a.inputFile]
    # [print(i) for i in a.topsList]
    # [print(i) for i in a.topsFields]
    [print(i) for i in a.topsData]


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()
