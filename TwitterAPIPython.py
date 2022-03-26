import pandas as pd
import json
import requests
from requests_oauthlib import OAuth1Session

oauth_user = OAuth1Session(client_key='t0S3HCeFVjL0kG7wsm43rzS3h',
                               client_secret='hcxdoNZQTk5sW3dp8HQuZYrL6SFbgtlkzkcdFrBn00k2c2eA4Z',
                               resource_owner_key='2418628328-MwtI3x7wSTKXVvc82VKr3mAouk9JO9BJ3JA35Wf',
                               resource_owner_secret='hE8OC7cisnM54XcnrSChQeCA6DWZosP85crH8XdQ7Gju0')
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

oauth_user = OAuth1Session(client_key='t0S3HCeFVjL0kG7wsm43rzS3h',
                               client_secret='hcxdoNZQTk5sW3dp8HQuZYrL6SFbgtlkzkcdFrBn00k2c2eA4Z',
                               resource_owner_key='2418628328-MwtI3x7wSTKXVvc82VKr3mAouk9JO9BJ3JA35Wf',
                               resource_owner_secret='hE8OC7cisnM54XcnrSChQeCA6DWZosP85crH8XdQ7Gju0')
url_user = 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular'
r = oauth_user.get(url_user)
data=r.json()
#print(data)
test=data['statuses'][0]
dff=[]

for tweet in range(len(test):
    #print(tweet)
    tweet={'created_at':test['created_at'],
           'id':test['id'],
           'url':test['entities']['urls'][0]['url'],
           'expanded_url':test['entities']['urls'][0]['expanded_url'],
          'user':test['user']['created_at'],
          'name':test['user']['name']}
    dff.append(tweet)
    #strdata=json.dumps(df)
df= pd.DataFrame(tweet)
df

************************************************************************************************************************************