import requests
from constants import APP_ACCESS_TOKEN,BASE_URL
from get_post_id import get_post_id
def post_a_comment(insta_username):
    media_id=get_post_id(insta_username)
    comment_text=raw_input("Your Comment: ")
    payload={"access_token":APP_ACCESS_TOKEN, "text" : comment_text}
    request_url=(BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s ' % (request_url)
    make_comment=requests.post(request_url,payload).json()
    if make_comment['meta']['code'] ==200:
        print "sucessfully added a new comment"
    else:
        print "Sorry You Are Unable To add Comment. plz.. Try Again!"
#post_a_comment(insta_username="sharmatanu9878")