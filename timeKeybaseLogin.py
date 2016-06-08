
import requests


timeValuesBadLen = []
timeValuesGoodLen = []

values = {'username': 'user',
          'password': 'kun1point'}


for i in xrange(100):
  r = requests.post("http://127.0.0.1:5000/login", data=values)
  if r.status_code == 200:
    #print r.elapsed
    timeValuesBadLen.append(r.elapsed.total_seconds())

print "Time with to short password: {0}".format( sum(timeValuesBadLen)/len(timeValuesBadLen))

values = {'username': 'user',
          'password': 'we just need a very long string, that shows that a difference comes in time!'}

for i in xrange(100):
  r = requests.post("http://127.0.0.1:5000/login", data=values)
  if r.status_code == 200:
    #print r.elapsed
    timeValuesGoodLen.append(r.elapsed.total_seconds())

print "Time with correct length password: {0}".format( sum(timeValuesGoodLen)/len(timeValuesGoodLen))
