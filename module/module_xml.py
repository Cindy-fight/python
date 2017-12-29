from xml.parsers.expat import ParserCreate

# 解析XML
class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s , attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s'  % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

#生成XML
def create_xml():
    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append(r'<a href="www.baidu.com">click</a>')
    L.append((r'</root>'))
    return ''.join(L)

print(create_xml())

# practice
import enum
import re

class WeekDay(enum.Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

class WeatherSaxHandler(dict):
    def start_element(self, name, attr):
        print(type(attr))
        # <> Wed, 27 May 2015 11: 00 am CST < / lastBuildDate >
        yweather_regex = re.compile(r'yweather:(\w*)')
        y_match = yweather_regex.match(name)
        if y_match:
            condition = y_match.group(1)
            if "condition" == condition:
                day = attr['date'].split(',')[0]
                if WeekDay[day]:
                    self._today = WeekDay[day].value
                    if self._today == 6:
                        self._tomorrow = 0
                    else:
                        self._tomorrow = self._today + 1
            elif "location" == condition:
                self['city'] = attr['city']
                self['country'] = attr['country']
            elif "forecast" == condition:
                day = attr['day']
                if WeekDay[day].value == self._today:
                    attr['low'] = int(attr['low'])
                    attr['high'] = int(attr['high'])
                    self['today'] = attr
                elif WeekDay[day].value == self._tomorrow:
                    attr['low'] = int(attr['low'])
                    attr['high'] = int(attr['high'])
                    self['tomorrow'] = attr

    def end_element(self, name):
        print('sax : end_element : %s' % (name))

    def char_data(self, text):
        print('sax : char_data: %s' % text)

    # def __str__(self):
    #     return "country : %s , city : %s , today : %s , tomorrow : %s " % (
    #         self.country, self.city, self.today, self.tomorrow)

def parse_weather(xml):
    weatherhandler = WeatherSaxHandler()
    parser_weather = ParserCreate()
    parser_weather.StartElementHandler = weatherhandler.start_element
    parser_weather.EndElementHandler = weatherhandler.end_element
    parser_weather.CharacterDataHandler = weatherhandler.char_data
    parser_weather.Parse(xml)
    return weatherhandler

data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''


print(parse_weather(data))
