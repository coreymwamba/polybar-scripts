#!/usr/bin/env python
import gi
gi.require_version('Geoclue', '2.0')
from gi.repository import Geoclue
clue = Geoclue.Simple.new_sync('something',Geoclue.AccuracyLevel.EXACT,None)
location = clue.get_location()
lat=location.get_property('latitude')
lon=location.get_property('longitude')
print(lat,lon)
