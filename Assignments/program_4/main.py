import os, sys
import pprint as pp
import collections

f = open("C:\\cygwin64\\home\\Abdel\\Spatial-DS-aitroua\\Assignments\\program_4\\program_4_helper.py", "r")

data = f.read()
data = jason.loaddata

all_airports = []

for k,v in data.items():
    gj = collections.OrderedDict()
    gj['Type'] = 'Features'
    gj['properties'] = v
    lat = ['lat']
    lon = ['lon']
    del gj['properties']['lat']
    del gj['Properties']['lon']
    gj['geometry'] = {}
    gj['geometry']['type'] = 'Point'
    gj['geometry']['coordinates'] = [
            lon,
            lat
        ]
    all_airports.append(gj)

pp.pprint(all_airports[0])

out = open("C:\\cygwin64\\home\\Abdel\\Spatial-DS-aitroua\\Assignments\\program_4\\program_4_helper.py", "w")

out.write(json.dumps()