import requests
from constants import APP_ACCESS_TOKEN,BASE_URL
def self_info():
    #Logic of The Function
    request_url=(BASE_URL+'users/self/?access_token=%s')%(APP_ACCESS_TOKEN)
    print 'GET request url:%s'%(request_url)
    user_info=requests.get(request_url).json()
    if user_info['meta']['code']==200:
        if len(user_info['data']):
            print 'User Name:%s'%(user_info['data']['User Name'])
            print 'No.Of Followers:%s'%(user_info['data']['counts']['followed By'])
            print 'No.Of People You Are Following:%s'%(user_info['data']['counts']['follows'])
            print 'No. Of Posts:%s' %(user_info['data']['counts']['media'])
        else:
            print 'User Doesnot Exist!'
    else:
        print 'Status Code Other Then 200 Received'




