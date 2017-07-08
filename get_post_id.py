import requests
from get_user_id import get_user_id
from constants import BASE_URL,APP_ACCESS_TOKEN
def get_post_id(insta_user_name):
    #Function Logic Here
    user_id = get_user_id(insta_user_name)
    if user_id==None:
        print "user does not exist"
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id,APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media=requests.get(request_url).json()
    if user_media['meta']['code']==200:
       if len(user_media['data']):
          return user_media['data'][0]['id']
       else:
           print 'There is no recent post of the user'
           exit()
    else:
        print "Status code other than 200 received!"
        exit()
#get_post_id(insta_user_name="sharmatanu9878")