import requests

r = requests.post('http://0.0.0.0:5000/api/user/', params={'name':'zach@hotmail.com', 'password':'pass'})

r = requests.put('http://0.0.0.0:5000/api/user/1',  params={'pagenumber':'132dsafds', 'pagename': 'pdasfdsython.py'})

#r = requests.get('http://0.0.0.0:5000/api/user/1')


print r
