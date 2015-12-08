url='https://torstatus.blutmagie.de/query_export.php/Tor_query_EXPORT.csv'
header_valid=[u'Router Name', u'Country Code', u'Bandwidth (KB/s)', u'Uptime (Hours)', u'IP Address', u'Hostname', u'ORPort', u'DirPort', u'Flag - Authority', u'Flag - Exit', u'Flag - Fast', u'Flag - Guard', u'Flag - Named', u'Flag - Stable', u'Flag - Running', u'Flag - Valid', u'Flag - V2Dir', u'Platform', u'Flag - Hibernating', u'Flag - Bad Exit', u'FirstSeen', u'ASName', u'ASNumber', u'ConsensusBandwidth', u'OrAddress']
dname='mit.edu'

import requests
import re
from netaddr import  IPAddress

class findtor():
    """findtor class"""
    def __init__(self):
        self.results={}
        self.iplist=[]
        self.torreport=[]
        self.headers=[]
    def getfile(self):
        try:
            print "grabbing file, this may take a few moments\n"
            urlresult=requests.get(url)
            if urlresult.status_code==200:
                urlresult_temp=urlresult.text
                self.torreport=urlresult_temp.split('\n')
                self.headers=self.torreport[0].split(',')
            else:
                urlresult.raise_for_status()
        except Exception as e:
            print "Something went wrong {0}".format(e)
            exit()
    def processfile(self):
        temp_results=[]
        for item in self.torreport:
            if re.search(dname,item):
                temp_results.append(item)
        if temp_results:
            for line in temp_results:
                ipadd= IPAddress(line.split(',')[4])
                self.results[ipadd]=line
                self.iplist.append(ipadd)          
        else:
            print "Error: Search term {0} not found".format(dname)
            exit()
    def report(self):
        self.iplist.sort()
        print "{0};{1};{2};{3};{4}".format(self.headers[0],self.headers[4],self.headers[5],self.headers[6],self.headers[7])
        for item in self.iplist:
            #print "{0}\n".format(self.results[item])
            temparray=self.results[item].split(',')
            print "{0};{1};{2};{3};{4}".format(temparray[0],temparray[4],temparray[5],temparray[6],temparray[7])

def main ():
    mit=findtor()
    mit.getfile()
    mit.processfile()
    mit.report()
if __name__ == '__main__':
    main()
            
        
        