import requests
import urllib
from constants import APP_ACCESS_TOKEN,BASE_URL
from get_user_id import get_user_id
def get_user_post(insta_username):
    #FUNCTION LOGIC
    user_id=get_user_id(insta_username)
    if user_id==None:
        print 'User doesnot Exist'
        exit()
    request_url=(BASE_URL+'user/%s/media/recent/?access_token=%s')%(user_id,APP_ACCESS_TOKEN,)
    print 'GET request url:%s'%(request_url)
    user_media=requests.get(request_url).json()
    if user_id['meta']['code']==200:
        #EXTRACT POST ID
       if len(user_media['data']):
           image_name=user_media['data'][0]['id']+'.jpeg'
           image_url=user_media['data'][0]['images']['standard_resolution']['url']
           urllib.urlretrieve(image_url,image_name)
           print "Your image Has Been Downloaded!"
       else:
           print "There is no recent post"
    else:
        print 'Status code other than 200 received'
get_user_post()


