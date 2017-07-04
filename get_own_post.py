import urllib
import requests
from constants import APP_ACCESS_TOKEN,BASE_URL
def get_own_post():
    #Function Logic
    request_url=(BASE_URL +'users/self/media/recent/?access_token=%s')%(APP_ACCESS_TOKEN)
    print 'GET request url:%s'%(request_url)
    own_media=requests.get(request_url).json()
    if own_media['meta']['code']==200:
        #EXTRACT POST ID
       if len(own_media['data']):
           image_name=own_media['data'][0]['id']+'.jpeg'
           image_url=own_media['data'][0]['images']['standard_resolution']['url']
           urllib.urlretrieve(image_url,image_name)
           print 'Your Image Has Been Succesfully Downloaded'
       else:
           print "Post doenot Exist"
    else:
        print "Status Code other Then 200 received"
