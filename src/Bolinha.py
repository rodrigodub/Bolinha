#! /usr/bin/python3
# -*- coding: windows-1252 -*-

#################################################
#                   Bolinha
# Bolinha is a script to process LAS files
#
# v0.1.024
# for Issue #5
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
    path : string - just the path
    las : string - just the LAS file name
    inputFile : list - the file contents, each line an item
    collarInfo : dictionary - dictionary of collar information from ~PARAMETER INFORMATION section
    holeid : string - the historic drillhole HOLEID (= SITECODE + DH_NUMBER)
    topsList : list - list of TOPS sections on file
    topsFields : list - list of trios [top section, top name, [field1, field2, ..., fieldn]]
    topsData : list - list of data from each TOPS section as [top section, [d1, d2, ..., dn]]
    logList : list - list of LOG sections on file
    logFields : list - list of trios [log section, log name, [field1, field2, ..., fieldn]]
    logData : list - list of data from each LOG section as [log section, [d1, d2, ..., dn]]
    """
    def __init__(self):
        self.inputFileName = input('File name? ')
        self.path = self.inputFileName.rsplit('\\', maxsplit=1)[0]
        self.las = self.inputFileName.rsplit('\\', maxsplit=1)[1]
        self.inputFile = self.readFile(self.inputFileName)
        self.collarInfo = self.setCollarInfo(self.inputFile)
        self.topsList = self.setTopsList(self.inputFile)
        self.topsFields = self.setTopsFields(self.inputFile, self.topsList)
        self.topsData = self.setTopsData(self.inputFile, self.topsList)
        self.logList = self.setLogList(self.inputFile)
        self.logFields = self.setLogFields(self.inputFile, self.logList)
        self.logData = self.setLogData(self.inputFile, self.logList)

    def readFile(self, filename):
        """Method to read the input file contents"""
        return LHFile(filename).readInfo()

    def setTopsList(self, inputfile):
        """Method to return the list of TOPS sections in the input file"""
        return [i[:-1] for i in inputfile if '~TOPS_DEFINITION' in i]

    def setLogList(self, inputfile):
        """Method to return the list of LOG sections in the input file"""
        return [i[:-1] for i in inputfile if '~LOG_DEFINITION' in i]

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
                        .replace(' Lithology      {S}\n', '').replace(' Symbol      {S}\n', '').replace('      {S}\n', '').replace('/', ''))
            # list of field names
            fields = []
            while inputfile[idx+3] != '#------------------------------------------------------------\n':
                fields.append(inputfile[idx+3].split(':')[1]
                              .replace('      {S}\n', '').replace('      {F}\n', '').replace('      {I}\n', '').replace('/', ''))
                idx += 1
            tops.append(fields)
            result.append(tops)
        return result

    def setLogFields(self, inputfile, loglist):
        """Method to define the list of fields for each LOG section"""
        # resulting list to output
        result = []
        for i in loglist:
            # each ~LOG_DEFINITION section
            log = []
            log.append(i)
            # finds the inputFile index of the ~LOG_DEFINITION
            idx = inputfile.index(i+'\n')
            # takes the second line as the LOG NAME
            log.append(inputfile[idx+2].split(':')[1]
                        .replace(' Azimuth      {F}\n', '').replace('      {F}\n', ''))
            # list of field names
            fields = []
            while inputfile[idx+2] != '#------------------------------------------------------------\n':
                fields.append(inputfile[idx+2].split(':')[1]
                              .replace('      {S}\n', '').replace('      {F}\n', '').replace('      {I}\n', ''))
                idx += 1
            log.append(fields)
            result.append(log)
        return result

    def setTopsData(self, inputfile, topslist):
        """Method to read and return the real TOPS section data to a list"""
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

    def setLogData(self, inputfile, loglist):
        """Method to read and return the real LOG section data to a list"""
        # resulting list to output
        result = []
        for i in loglist:
            # each ~LOG_DEFINITION section
            log = []
            log.append(i)
            # finds the inputFile index of the ~LOG_DEFINITION
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
            log.append(data)
            result.append(log)
        return result

    def setCollarInfo(self, inputfile):
        """
        Method to retrieve collar information from the ~PARAMETER INFORMATION
        section
        and store it in a dictionary
        """
        # resulting dictionary with only existing information + the complete list
        dictionary = {}
        # complete list of PARAMETER section
        parameter = []
        idx = inputfile.index('~PARAMETER INFORMATION\n')
        idx += 1
        while inputfile[idx] != '#------------------------------------------------------------\n':
            parameter.append(inputfile[idx])
            idx += 1
        for i in parameter:
            if i.split(':')[0].split('.')[1].strip():
                dictionary[i.split('.')[0]] = i.split(':')[0].split('.', maxsplit=1)[1].strip()
        dictionary['HOLEID'] = dictionary['SITECODE'] + dictionary['DH_NUMBER']
        dictionary['COMPLETE'] = parameter
        return dictionary

    def writeFiles(self):
        """
        Method to write the output files. It assumes all instance attributes have been successfully created
        and references them by self.attribute (i.e. they are not passed as arguments to the method)
        """
        # increment to sort files alphabetically
        fileindex = 1
        # write Collar file
        outputFileName = self.inputFileName.replace('.las', '') + '_{:02d}_Collar.csv'.format(fileindex)
        LHFile(outputFileName).writeInfo('HOLEID, DEPTH, DIP, DIR, DIAMETER, LOG_SIGN, LOG_DATE')
        concat = self.collarInfo['HOLEID']
        try:
            concat += ', ' + self.collarInfo['TOT_LENGTH']
        except:
            concat += ','
        try:
            concat += ', ' + self.collarInfo['DIP']
        except:
            concat += ','
        try:
            concat += ', ' + self.collarInfo['DIR']
        except:
            concat += ','
        try:
            concat += ', ' + self.collarInfo['DIAMETER']
        except:
            concat += ','
        try:
            concat += ', ' + self.collarInfo['LOG_SIGN']
        except:
            concat += ','
        try:
            concat += ', ' + self.collarInfo['LOG_DATE']
        except:
            concat += ','
        LHFile(outputFileName).writeInfo(concat)
        print('Collar file written: {}'.format(outputFileName))
        # write TOPS files
        topsindex = 0
        for i in self.topsFields:
            fileindex += 1
            outputFileName = self.inputFileName.replace('.las', '') + '_{:02d}_{}.csv'.format(fileindex, i[1])
            LHFile(outputFileName).writeInfo('HOLEID, FROM, TO, {}'.format(i[2]).replace('[', '').replace(']', '').replace("'", ""))
            for j in self.topsData[topsindex][1]:
                LHFile(outputFileName).writeInfo('{}, {}'.format(self.collarInfo['HOLEID'], j.replace('\n','')))
            topsindex += 1
            print('TOPS file written: {}'.format(outputFileName))
        # write LOG files
        logindex = 0
        for i in self.logFields:
            fileindex += 1
            outputFileName = self.inputFileName.replace('.las', '') + '_{:02d}_{}.csv'.format(fileindex, i[1])
            LHFile(outputFileName).writeInfo('HOLEID, DEPTH, {}'.format(i[2]).replace('[', '').replace(']', '').replace("'", ""))
            for j in self.logData[logindex][1]:
                LHFile(outputFileName).writeInfo('{}, {}'.format(self.collarInfo['HOLEID'], j.replace('\n','')))
            logindex += 1
            print('LOG file written: {}'.format(outputFileName))


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
    # [print(i) for i in a.topsData]
    # [print(i) for i in a.logList]
    # [print(i) for i in a.logFields]
    # [print(i) for i in a.logData]
    # [print(i) for i in a.collarInfo]
    # print(a.collarInfo)
    # print('Path: {}'.format(a.path))
    # print('File: {}'.format(a.las))
    # print('Path+File: {}'.format(a.inputFileName))
    # print('New File: {}'.format(a.writeFiles()))
    a.writeFiles()


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()
