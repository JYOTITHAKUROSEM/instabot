#Main file
# Sandbox Users :-
                     # Admin Name:- jyotithakur15111
                     # Friends list:-
                    #  1)juhi 2494
                    # 2) vikasraj7027
                   # 3)sudikshchandel
                   # 4)sharmatanu9878
from constants import BASE_URL,APP_ACCESS_TOKEN
#imports base_url and access token
from self_info import self_info
#Fetching Own Information
from get_own_post import get_own_post
#Fetching our own recent Data
from get_user_id import get_user_id
# Getting the another user id
from get_user_info import get_user_info
#getting the user info
from get_users_post import get_user_post
# Fetching the user recent post
from get_post_id import get_post_id
# Fetching the user recent post id
from like_a_post import like_a_post
# like the user recent post
from post_a_comment import post_a_comment
# comment the user recent post
from delete_negative_comment import delete_negative_comment
# Delete  the user neagtive comment automatically but it understood only english language if you type bad cooment in hindi then it doesnot remove these comment.
from list_of_comments import comment_list
#comments  of like
from like_list import list_a_like
# like list
from hashtag import analyse_user
while True:
    print '\n'
    print 'Hey! Welcome to InstaBot!'
    print 'choose menu options:'
    print "1.Get your own details\n"
    print "2.Get details of a user by username\n"
    print "3.Get your own recent post\n"
    print "4.Get the recent post of a user by username\n"
    print "5.Like the recent post of a user\n"
    print "6.Make a comment on the recent post of a user\n"
    print "7.Get a list of like on the recent post of the user\n"
    print "8.Get a list of comments on the recent post of a user\n"
    print "9.Delete negative comments from the recent post of a user\n"
    print "10.User Interest On the basis of user post"
    print "11.Exit"
    choice = raw_input("Enter your choice: ")
    if choice == "1":
        self_info()
    elif choice == "2":
        insta_username = raw_input("Enter the username of the user: ")
        get_user_info(insta_username)
    elif choice == "3":
        get_own_post()
    elif choice == "4":
        insta_username = raw_input("Enter the username of the user: ")
        get_user_post(insta_username)
    elif choice == "5":
        insta_username = raw_input("Enter the username of the user: ")
        like_a_post(insta_username)
    elif choice == "6":
        insta_username = raw_input("Enter the username of the user: ")
        post_a_comment(insta_username)
    elif choice == "7":
        insta_username = raw_input("Enter the username of the user: ")
        list_a_like(insta_username)
    elif choice == "8":
        insta_username = raw_input("Enter the username of the user: ")
        comment_list(insta_username)
    elif choice == "9":
        insta_username = raw_input("Enter the user name: ")
        delete_negative_comment(insta_username)
    elif choice == "10":
        insta_username = raw_input("Enter the user name: ")
        analyse_user(get_user_id(insta_username))
    elif choice == "11":
        exit()
    else:
        print "Your choose wrong choice plz choose again......."