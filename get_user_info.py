import requests,urllib
from get_user_id import get_user_id
from constants import APP_ACCESS_TOKEN,BASE_URL
#insta_username =["sharmatanu9878"]
def get_user_info(insta_username):
    #FUNCTION LOGIC
    user_id = get_user_id(insta_username)
    if user_id == None:
       print 'User Does Not Exist'
       exit()
    request_url=(BASE_URL +'users/%s?access_token=%s')%(user_id, APP_ACCESS_TOKEN)
    #print (request_url)
    print 'GET request url : %s' % (request_url)
    user_info=requests.get(request_url).json()
    if user_info['meta']['code']==200:
       if len(user_info['data']):
           print 'Username:%s' % (user_info['data']['username'])
           print 'No.of followers:%s' % (user_info['data']['counts']['followed_by'])
           print 'No. of People you are following:%s' % (user_info['data']['counts']['follows'])
           print  'No. of Posts:%s' % (user_info['data']['counts']['media'])
       else:
           print "There is no data for this user"
    else:
        print "status code other than 200 received"
#get_user_info(insta_username="sharmatanu9878")