#importing required libraries
import praw       #Python Reddit API Wrapper
import c3onfig    #Config details of bot
import time       #To put program to sleep
import warnings 
warnings.filterwarnings('ignore')

def bot_login():
    r = praw.Reddit(
        user_agent='chatori club',
        username=c3onfig.username,
        password=c3onfig.password,
        client_id=c3onfig.client_id,
        client_secret=c3onfig.client_secret
        
    )
    return r

our_subreddit="chatori_jabalpur"
def find_word(r,word_to_find):
    word_to_find=word_to_find.lower()
    for comment in r.subreddit(our_subreddit).comments(limit=25):
        if word_to_find in comment.body:
            print(comment.body)

def testing_reply(r,word_to_find):

    for comment in r.subreddit(our_subreddit).comments(limit=25):
        if word_to_find in comment.body and (word_to_find=="ninja" or word_to_find=="NINJA"):
            comment.reply("Beyblade fight in Hexagon, let's assemble")
            print('Done')

        elif word_to_find in comment.body and (word_to_find=="BitByte" or word_to_find=='bitbyte'):
            comment.reply("🐲🐱‍👤 Literally the best club on campus 🎇💖")
            print('Done, bitbyte reply')

        elif word_to_find in comment.body and word_to_find=='test':
            comment.reply("Testing complete, 🍕 being delivered")
            print('Test complete, logged in succesfully as DMJ-Bot')
def upvote_test(r,word_to_find):
    for comment in r.subreddit(our_subreddit).comments(limit=10):
        if word_to_find in comment.body: #and (word_to_find=='BitByte' or word_to_find=="bitbyte"):
            comment.upvote()
            print('Upvoted comment')
r=bot_login()
upvote_test(r,"test")
testing_reply(r,"test")