import tweepy
import credentials 

# Create the authentication object
authenticate = tweepy.OAuthHandler(credentials.consumerKey, credentials.consumerSecret) 

# Set the access token and access token secret
authenticate.set_access_token(credentials.accessToken, credentials.accessTokenSecret) 

# Creating the API object while passing in auth information
api = tweepy.API(authenticate)

print('Welcome to your timeline \n')

#print the last 2 tweets in my timeline
public_tweets = api.home_timeline(count=2)
for tweet in public_tweets:
    print(tweet.text + "\n")