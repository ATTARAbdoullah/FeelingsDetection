import tweepy
import credentials 
import pandas as pd

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

def searchQuery(q,lang):
    #Search querry q on 7-day limit timeline of recent and popular( result_type = mixed ) tweets 
    searchedQuery = api().search(q,lang=lang)
    for tweet in searchedQuery:
        print(tweet.text+ "\n")
    print("Nombre de tweets: " + str(len(searchedQuery)))
   
def writeSearchedQuery(q,lang):
    #Looking for querry q and write it down on an f file
    f= open("output.txt","w+", encoding="utf-8")
    tweets= api().search(q,lang=lang)
    for tweet in tweets:
        f.write(str(tweet.text) + "\n")
    f.close()   

def temp():
    columns = set()
    allowed_types = [str, int]
    tweets_data = []
    my_timeline=api().home_timeline()
    
    for status in my_timeline:
        #print(status.author.screen_name)
        # print(type(vars(status)))
        status_dict = dict(vars(status))
        keys = status_dict.keys()
        single_tweet_data = {"author": status.author.screen_name}
        for k in keys:
            try:
                v_type = type(status_dict[k])
            except:
                v_type = None
            if v_type != None:
                if v_type in allowed_types:
                    single_tweet_data[k] = status_dict[k]
                    columns.add(k)
        tweets_data.append(single_tweet_data)
     
    header_cols = list(columns)
    header_cols.append('author')
    df = pd.DataFrame(tweets_data, columns=header_cols)
    f= open("output.txt","w+", encoding="utf-8")
    f.write(str(df))
    f.close() 
    return df

def main():
    #temp()
    #timeline(2) #Home Page
    searchQuery("#France","fr")
    writeSearchedQuery("#France","fr")
    

if __name__ == "__main__":
   main()
   

  