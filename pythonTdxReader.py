import os
import struct
from sys import argv

sdir = argv[1]

PER_MIN5 = 0
PER_DAY = 4

class TdxTime:
    def __init__(self):
        self.Year   = 1900
        self.Month  = 1
        self.Day    = 1
        self.Hour   = 0
        self.Minute = 0
        self.Second = 0

class TdxHistoryData:
    def __init__(self):
        self.Time   = TdxTime()
        self.Open   = 0
        self.High   = 0
        self.Low    = 0
        self.Close  = 0
        self.Amount = 0
        self.Volumn = 0


def run():
    SHDayLineDir = sdir + '\\vipdoc\\sh\\lday'
    SZDayLineDir = sdir + '\\vipdoc\\sz\\lday'
    SH5MLineDir = sdir + '\\vipdoc\\sh\\fzline'
    SZ5MLineDir = sdir + '\\vipdoc\\sz\\fzline'
    
    ReadDayKLine(SHDayLineDir)
    ReadDayKLine(SZDayLineDir)
    Read5MKLine(SH5MLineDir)
    Read5MKLine(SZ5MLineDir)

    return

def ReadDayKLine(fdir):
    try:
        for f in os.listdir(fdir):
            fpath = fdir + '\\' + f
            if os.path.isfile(fpath):
                print('Handling file ' + f)
                ReadKLineFile(fpath, f, PER_DAY)
    except Exception as e:
        print('Read file exception:' + f)
    return

def Read5MKLine(fpath):
    try:
        for f in os.listdir(fdir):
            fpath = fdir + '\\' + f
            if os.path.isfile(fpath):
                print('Handling file ' + f)
                ReadKLineFile(fpath, f, PER_MIN5)
    except Exception as e:
        print('Read file exception:' + f)
    return

def ReadKLineFile(fpath, f, type):
    file = open(fpath, 'rb')
    year,month,day,hour,minute,second,open,high,low,close,amount,volumn=struct.unpack('H5c5f1d')
    return

if __name__ == '__main__':
    if len(argv) < 1:
        exit(0)

    try:
        run()
    except Exception as e:
        print(e)
