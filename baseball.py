# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API
access_token = '2167568887-D7A9l184JSeFPEC1iMGCTQwoCUlBHzH7f6HZyLS'
access_token_secret = 'hMSuVEVPNkTMzITfhXtvDDFAV07X9ryKwHN5Rdhxlb099'
consumer_key = 'Jkd62ikb3DTlU2L8eHJIxfrHY'
consumer_secret = 'SZbNKbg8KB0pARDcEvHAdpBBZJ8ECJNGCbQoDMLqhdU08fo4r2'
#we will need our own individual keys above to access the data


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('baseball.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    twitter_stream = Stream(auth, MyListener())
    print("Writing Tweets")
    #twitter_stream.filter(track=['bollywood'])
    #print("Writing Tweets")

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    twitter_stream.filter(track=['Pacific Coast League', 'player statistics', 'Omaha Storm Chasers', ])