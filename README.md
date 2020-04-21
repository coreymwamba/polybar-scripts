# polybar-scripts
The scripts in this repository all work in a system for my [polybar](https://polybar.github.io/).
The `geoclue-py` script pulls in a location. This is used by `get_weather`, which produces an XML file with data from OpenWeatherMap. This XML file is then used by `weather-summary`, which also uses `moonphase`.

![a visual example of the polybar module](https://github.com/coreymwamba/polybar-scripts/blob/master/grab-1587460628.jpg)

## Requirements
+ An [Openweathermap API key](https://openweathermap.org/api)
+ Geoclue(https://gitlab.freedesktop.org/geoclue/geoclue)
+ [libxml2](http://xmlsoft.org/)
+ [Genius](https://www.jirka.org/genius.html), which is capable of rounding numbers with having to write a function, unlike bc.
+ [Weather Icons](https://erikflowers.github.io/weather-icons/)

I think Geoclue and libxml2 are generally available as standard packages in most Linux distributions, but YMMV.

## geoclue-py
This is a basic-level use of Geoclue. It just gives the latitude and longitude, separated by a space.

```
$ python bin/geoclue-py.py 
53.9078956 -1.4869201
```
## moonphase
This is based on [this script](https://gist.github.com/zuloo/f2fed0de6ddbc0d25e2e). I didn't understand the rationale for the numbers used in the script, so I re-did the calculation, according to the description in Wikipedia. I needed Julian Day numbers; so used [the accepted answer on Stack Overflow](https://stackoverflow.com/questions/43317428/bash-how-to-get-current-julian-day-number). It's incredibly rough working, but (right now) accurate, and has been for the last few days. This is mainly because the Julian Day of the previously calculated new moon is written to a file, so the phase calculations are kept small.

## get_weather
This script uses Geoclue and your API key from Openweathermap to pull in a current weather report for your discovered location, and puts that report in a file. I didn't combine it with `weather-summary` because it gives you the chance to use the data in other scripts as you choose. **Call this script every ten minutes, or less often;** Openweathermap has a rate limit of one call per ten minutes, and requesting a report every five seconds will get you blocked.

## weather-summary
This script prints out a formatted line of the weather, based on the contents of the XML file. This means that you can use this in scripts where you can't control the time interval for discrete elements.

### Usage
weather-summary [UNIT_OPTIONS] -f "[FORMAT_STRING]"

UNIT_OPTIONS (all optional, units default to metric system and 24h clock):

**-C | -F | -K**      temperature units (Celsius, Fahrenheit, Kelvin)    
**-P | -H**           pressure units (hPa, mmHg)    
**-S | -m | -k**      speed units (m/s, m.p.h., km/h)    
**-M | -i**           precipitation measurement units (mm, in)    
**-4 | -2**           sunrise/sunset time format (24h, 12h)    

FORMAT FLAG:

 **-f** "FORMAT" where    
       %C = location    
       %c = country    
       %T = description    
       %I = description icon    
       %S = sunrise time    
       %s = sunset time    
       %R = sunrise icon    
       %r = sunset icon    
       %t = temperature    
       %h = maximum temperature    
       %l = minimum temperature    
       %H = humidity    
       %f = "feels like" temperature    
       %w = wind speed    
       %D = wind compass direction    
       %d = wind direction in degrees    
       %P = preciptation    
       %p = precipation measurement    
       %u = pressure    
       %B = Beaufort wind scale    
       %b = Beaufort wind scale icon    
       %M = moon phase    
       %m = moon phase icon

### Examples
With no options, the metric values are given: 
```
$ weather-summary -f "%C %t %u %w"
Derby 11 1020 6.7
```
The same, with options:
```
$ weather-summary -FmH -f "%C %t %u, %w"
Derby 52°F 765 mmHg, 15 m.p.h.
```
