import requests
from constants import APP_ACCESS_TOKEN,BASE_URL
insta_username = "sharmatanu9878"
def get_user_id(insta_username):
    #function logic
    request_url=(BASE_URL +'users/search?q=%s&access_token=%s')%(insta_username,APP_ACCESS_TOKEN)
    print 'GET REQUEST url:%s'%(request_url)
    user_info=requests.get(request_url).json()
    if user_info['meta']['code']==200:
        if len(user_info['data']):
           print((user_info['data'][0]['id']))
           return(user_info['data'][0]['id'])
        else:
            return None
    else:
        print 'status code other then 200 received'
        exit()
get_user_id(insta_username)