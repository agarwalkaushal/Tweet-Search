import tweepy

consumer_key = "9wMMydVttqCGk3ALuh4ZMTkQC"
consumer_secret = "GYB4CJEZs5Jf29L7ZoFyENYdWAdn7Q83ERMe3dSlRW5z9EsiI4"
access_token = "4681694112-j2EKYY58p3367gFmLfwx480bdfxr3KIB80drM7I"
access_token_secret = "AeAJl5svwqeR542JICufARaC8FrZnNSbrv1GlgQ7uBW9S"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def myFollowers():
    print()

    followers = api.followers_ids()
    if followers:
        print("You have ",len(followers), " followers.")
        print()
    for user in tweepy.Cursor(api.followers).items(200):
        print(user.screen_name," ",user.name)
       

def myFriends():
    print()
    
    friends = api.friends_ids()
    if friends:
        print("You have ",len(friends), " friends.")
        print()
    for user in tweepy.Cursor(api.friends).items(200):
        print(user.screen_name," ",user.name)

def myTweets():
    print()

    """
    #This only returns the 20 most recent tweets

    tweets = api.user_timeline() 
    tweets = [tweet.text for tweet in tweets]
    c = 1
    for j in tweets: 
        print(c,". ",j)
        c+=1
    """

    tweets = []
    c = 1
    for status in tweepy.Cursor(api.user_timeline).items(200):
        print(c,". ",status.text)
        tweets.append(status.text)
        c+=1

    print()
    print("Enter your search text: ",end="")
    query = input().lower()
    print()
    print("Search results: ")
    print()
    for j in tweets:
        
        if query in j.lower():
            print(j)

def homeTweets():
    print()
    """
    #This only returns the 20 most recent tweets

    public_tweets = api.home_timeline()
    c = 1
    for tweet in public_tweets:
        print(c,". ",tweet.text)
        c+=1
    """
    
    tweets = []
    c = 1
    for status in tweepy.Cursor(api.home_timeline).items(200):
        print(c,". ",status.text)
        tweets.append(status.text)
        c+=1

    print()
    print("Enter your search text: ",end="")
    query = input().lower()
    print()
    print("Search results: ")
    print()
    for j in tweets:
        
        if query in j.lower():
            print(j)


def usersTweets():
    print()
    username = input("Enter username: ")
    """
    #This only returns the 20 most recent tweets

    tweets = api.user_timeline(screen_name=username) 
    tweets = [tweet.text for tweet in tweets] 
    c = 1
    for j in tweets: 
        print(c,". ",j) 
        c+=1
    """
    
    tweets = []
    c = 1
    for status in tweepy.Cursor(api.user_timeline, id=username).items(200):
        print(c,". ",status.text)
        tweets.append(status.text)
        c+=1
    
    print()
    print("Enter your search text: ",end="")
    query = input().lower()
    print()
    print("Search results: ")
    print()
    for j in tweets:
        
        if query in j.lower():
            print(j)



while True:

    print()
    print("What would you like Tweet-Search to do? ")
    print()
    print("1. Display my Followers")
    print("2. Get my Friends (who you follow)")
    print("3. Retrieve my tweets")
    print("4. Home tweets")
    print("5. Get a [USER]'s tweets")
    print()
    print("Press CTRL+C to stop anytime!")

    option = input()

    if option == "1":
        myFollowers()
    elif option == "2":
        myFriends()
    elif option == "3":
        myTweets()
    elif option == "4":
        homeTweets()
    elif option == "5":
        usersTweets()
    else:
        print("Thank you for using Tweet-Search")
        break