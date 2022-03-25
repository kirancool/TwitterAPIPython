import pandas as pd
import json
import requests
from requests_oauthlib import OAuth1Session

oauth_user = OAuth1Session(client_key='',
                               client_secret='',
                               resource_owner_key='',
                               resource_owner_secret='')
url_user = 'https://api.twitter.com/1.1/collections/entries.json?id=custom-539487832448843776'
r = oauth_user.get(url_user)
data=r.json()
#print(data)

dff=[]

for tweet in data:
  dff.append({'collection_type':data['objects']['timelines']['custom-539487832448843776']['collection_type'],
           'name':data['objects']['timelines']['custom-539487832448843776']['name'],
           'collection_url':data['objects']['timelines']['custom-539487832448843776']['collection_url'],
          'created_at':data['objects']['tweets']['504032379045179393']['created_at'],
          'expanded_url':data['objects']['tweets']['504032379045179393']['entities']['media'][0]['expanded_url'],
          'media_url':data['objects']['tweets']['504032379045179393']['entities']['media'][0]['media_url']})
  strdata=json.dumps(dff)
  df=pd.DataFrame(dff)
  print(df)
  
*************************************************************************************************************************************************************************************


#from urlib.request import urlopen
import pandas as pd
import json
import requests
from requests_oauthlib import OAuth1Session

oauth_user = OAuth1Session(client_key='',
                               client_secret='',
                               resource_owner_key='',
                               resource_owner_secret='')
url_user = 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular'
r = oauth_user.get(url_user)
data=r.json()
#print(data)
test=data['statuses'][0]
dff=[]

for tweet in range(100):
    #print(tweet)
    tweet={'created_at':test['created_at'],
           'id':test['id'],
           'url':test['entities']['urls'][0]['url'],
           'expanded_url':test['entities']['urls'][0]['expanded_url'],
          'user':test['user']['created_at'],
          'name':test['user']['name']}
    dff.append(tweet)
    #strdata=json.dumps(df)
d=pd.DataFrame(dff)
d