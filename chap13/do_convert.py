#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: convert.py
#    Created:       <2019/02/06 21:07:00>
#    Last Modified: <2019/02/06 21:21:02>

from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

flights2 = {}

# for flight in flights:
#     flights2[convert2ampm(flight)] = flights[flight].title()

for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

pprint.pprint(flights2)
