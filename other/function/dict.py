#!/usr/bin/env python
# -*- coding utf-8 -*-
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Bob']
c = {'Larry': 95, 'Abe': 97, 'Lee': 99}
print c['Lee']
c['Lee'] = 97
print c['Lee']
a = d
d.pop('Bob')
print d
print a 
