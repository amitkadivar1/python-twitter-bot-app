import tweepy
import time 
print("this is my twitter bot")

CONSUMER_KEY='rxBfzeW6BgxVrunYNAKMc8Dik'
CONSUMER_SECRET='PxQsl9XNDCs4CEPxzPzr6ASrh37IahFqTZ55gyoEBrh8irR8dS'
ACCESS_KEY='4180352178-JXihYJSRm7qndcsGDuDawnHnmBW2x1allA3yEY8'
ACCESS_SECRET='u87LzYp9ijHTwStUUtubRkEfOTStvM4W5eEix6BW2k7No'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    file_last_seen_id = int(f_read.read().strip())
    f_read.close()
    return file_last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    print("file write"+str(last_seen_id))
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print("Replay to tweet .....")
    last_seen_id=retrieve_last_seen_id(FILE_NAME)
    mentions=api.mentions_timeline(last_seen_id,tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + '  -  ' + mention.full_text)
        last_seen_id=mention.id
        store_last_seen_id(last_seen_id,FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print("Found #helloworld")
            print("responding back")
            api.update_status('@'+mention.user.screen_name+" #HelloWorld back to you! ",mention.id)

while True:
    reply_to_tweets()
    time.sleep(2)
