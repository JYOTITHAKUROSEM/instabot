import requests
from constants import APP_ACCESS_TOKEN,BASE_URL
def self_info():
    #Logic of The Function
    request_url=(BASE_URL+'users/self/?access_token=%s')%(APP_ACCESS_TOKEN)
    print 'GET request url:%s'%(request_url)
    user_info=requests.get(request_url).json()
    if user_info['meta']['code']==200:
        if len(user_info['data']):
            print 'User Name:%s'%(user_info['data']['username'])
            print 'No.of followers:%s'%(user_info['data']['counts']['followed_by'])
            print 'No.of people You Are Following:%s'%(user_info['data']['counts']['follows'])
            print 'No. Of posts:%s' %(user_info['data']['counts']['media'])
        else:
            print 'User Doesnot Exist!'
    else:
        print 'Status Code Other Then 200 Received'
self_info()



