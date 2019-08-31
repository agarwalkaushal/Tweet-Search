import tweepy

consumer_key = "9wMMydVttqCGk3ALuh4ZMTkQC"
consumer_secret = "GYB4CJEZs5Jf29L7ZoFyENYdWAdn7Q83ERMe3dSlRW5z9EsiI4"
access_token = "4681694112-j2EKYY58p3367gFmLfwx480bdfxr3KIB80drM7I"
access_token_secret = "AeAJl5svwqeR542JICufARaC8FrZnNSbrv1GlgQ7uBW9S"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
print("-------------------")
user = api.get_user('KAUSHAL1509')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)