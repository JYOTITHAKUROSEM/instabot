#Import Files
import requests
from textblob import TextBlob
from constants import BASE_URL,APP_ACCESS_TOKEN
from get_post_id import get_post_id
from textblob.sentiments import NaiveBayesAnalyzer
def delete_negative_comment(insta_username):
    #Function Logic Here
    media_id=get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s')%(media_id,APP_ACCESS_TOKEN)
    print 'GET request url : %s' %(request_url)
    comment_info = requests.get(request_url).json()
    if comment_info['meta']['code'] ==200:
        if len(comment_info['data']):
           #Here's a naive implementation of how to delete the negative comments
           for x in range(0,len(comment_info['data'])):
               comment_id = comment_info['data'][x]['id']
               comment_text = comment_info['data'][x]['text']
               blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
               if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                   print 'Negative comment : %s' % (comment_text)
                   delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%')
                   print 'DELETE request url : %s' % (delete_url)
                   delete_info = requests.delete(delete_url).json()
                   if delete_info['meta']['code'] ==200:
                       print 'Comment Successfully deleted!\n'
                   else:
                       print 'SORRY! Unable To Delete comment!'
               else:
                   print "Positive comment : %s\n" % (comment_text)
        else:
             print 'Already Have comments on the post!'
    else:
         print("Status code other than 200 received!")
delete_negative_comment(insta_username="sharmatanu9878")