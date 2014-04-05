import urllib.request
import xml.etree.ElementTree as etree
import csv
import os


class YWeather(object):
    def __init__(self):
        self.dir = os.getcwd()
        if '/yahoo_weather' not in self.dir:
            self.codes = self.readDict(self.dir+'/yahoo_weather/codes.csv')
        else:
            self.codes = self.readDict(self.dir+'/codes.csv')

    def translate_code(self, code):
        return self.codes[code]

    def weather_data(self, woeid, unit):
        url = 'http://weather.yahooapis.com/forecastrss?w=' + str(woeid) + '&u=' + unit
        #print(url)
        root = self.returnroot(url)
        data = dict()
        #Pull any useful information out of the xml
        try:
            for i in range(0, 4):
                data['day'+str(i)] = root[0][12][i+7].attrib
                data['day'+str(i)]['conditions']= self.translate_code(data['day'+str(i)]['code'])
            data['language'] = root[0][3].text
            data['location'] = root[0][6].attrib
            data['units'] = root[0][7].attrib
            data['day0']['wind'] = root[0][8].attrib
            data['day0']['atmosphere'] = root[0][9].attrib
            data['day0']['astronomy'] = root[0][10].attrib
            data['day0']['current_conditions'] = root[0][12][5].attrib
                 
            data['location_lat'] = root[0][12][1].text
            data['location_long'] = root[0][12][2].text
            data['yahoo_link'] = root[0][12][3].text
            data['pubDate'] = root[0][12][4].text
            
            #Get forecast data, today being day0
            
        except IndexError:
            print("WOEID: " + str(woeid) + " Is not a valid WOEID")
        
        return data

    def readDict(self, file):
        h = []
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row != []:
                    h.append(row)
        return dict(h)
        
    def returnroot(self, url):
        try:
            xmltext = (urllib.request.urlretrieve(url))
        except:
            print('Internet connection or WOEID is not valid')
        root = (etree.parse(xmltext[0])).getroot()
        global c
        c = root
        return root


data = YWeather().weather_data(6, 'c')
