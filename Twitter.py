import tweepy
import credentials 

def api():
    # Create the authentication object
    authenticate = tweepy.OAuthHandler(credentials.consumerKey, credentials.consumerSecret) 

    # Set the access token and access token secret
    authenticate.set_access_token(credentials.accessToken, credentials.accessTokenSecret) 

    # Creating the API object while passing in auth information
    api = tweepy.API(authenticate)

    return api

def timeline(n):
    #print the last n tweets in the timeline
    print('Welcome to your timeline \n')
    public_tweets = api().home_timeline(count=n)
    for tweet in public_tweets:
        print(tweet.text + "\n")

def searchQuery(q):
    #Search querry q on 7-day limit timeline of recent and popular( result_type = mixed ) tweets 
    return api().search(q)
    
def writeSearchedQuery(q):
    #Looking for querry q and write it down on an f file
    f= open("output.txt","w+", encoding="utf-8")
    tweets=searchQuery(q)
    f.write(str(tweets))
    f.close()   

def main():
    api()
    timeline(2)
    #print(searchQuery("#MAR"))
    writeSearchedQuery("#MAR")
    

if __name__ == "__main__":
   main()

  