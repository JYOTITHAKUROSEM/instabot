import requests
from constants import APP_ACCESS_TOKEN,BASE_URL
from get_user_id import get_user_id
def get_user_info(insta_username):
    #FUNCTION LOGIC
    user_id=get_user_id(insta_username)
    if user_id==None:
       print 'User Does Not Exist'
       exit()
    request_url=(BASE_URL + 'user/%?access_token=%s')%(user_id,APP_ACCESS_TOKEN)
    print 'GET request url:%s' %(request_url)
    user_info=requests.get(request_url).json()
    if user_info['meta']['code']==200:
       if len(user_info['data']):
           print 'username:%s'%(user_info['data']['username'])
           print 'No.of Followers:%s'%(user_info['data']['counts']['Followed_By'])
           print 'No. of People you are following.%s'%(user_info['data']['counts']['Follows'])
           print'No. of Posts:%s'(user_info['data']['count']['media'])

