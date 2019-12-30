# Import the necessary methods from tweepy library
import tweepy
import json

#Variables that contains the user credentials to access Twitter API
access_token = '2167568887-D7A9l184JSeFPEC1iMGCTQwoCUlBHzH7f6HZyLS'
access_token_secret = 'hMSuVEVPNkTMzITfhXtvDDFAV07X9ryKwHN5Rdhxlb099'
consumer_key = 'Jkd62ikb3DTlU2L8eHJIxfrHY'
consumer_secret = 'SZbNKbg8KB0pARDcEvHAdpBBZJ8ECJNGCbQoDMLqhdU08fo4r2'


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
     #get tweets by hbs 
    osctweets = api.user_timeline('OMAStormChasers',count=1000)

    #get tweets about disney
    query = 'OMAStormChasers -filter:retweets'
    max_tweets = 1000
    aboutosctweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
    print(aboutosctweets)
    try:
        with open('oschasers.json', 'a') as f:
            json.dump([status._json for status in osctweets], f)
            #json.dump(abouthbstweets,f)

    except BaseException as e:
        print("Error writing: %s" % str(e))
