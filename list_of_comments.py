#import files
import requests
from constants import BASE_URL,APP_ACCESS_TOKEN
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from get_post_id import get_post_id
from get_user_id import get_user_id
def comment_list(insta_username):
    #fuction logic here
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s'%(request_url)
    comment_info = requests.get(request_url).json()
    if comment_info['meta']['code']== 200:
       for x in range(0, len(comment_info['data'])):
               comment_id = comment_info['data'][x]['id']
               comment_text = comment_info['data'][x]['text']
               blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
               if(blob.sentiment.p_neg > blob.sentiment.p_pos):
                   print 'Negative comment : %s'%(comment_text)
               else:
                   print "Positive comment : %s\n" % (comment_text)
#comment_list(insta_username="vikasraj7027")
