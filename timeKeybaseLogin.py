import requests


headers = {'user-agent': 'my-app/0.0.1',
           "Accept-Encoding":"gzip, deflate, br",
           "Accept":"*/*",
           "Accept-Language":"en-US,en;q=0.8,da;q=0.6",
           "Connection":"keep-alive",
           "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
           "Host":"keybase.io",
           "Origin":"https://keybase.io",
           "X-Requested-With":"XMLHttpRequest",
           "DNT":"1",
           "Referer":"https://keybase.io/verify",
          }

r = requests.get("https://keybase.io/_/api/1.0/login.json",
                 headers=headers )

print r.elapsed
print r.status_code