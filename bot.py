import tweepy,requests,time,generator,os
from PIL import Image

def checkStatus(sinceId):
    count = 0
    lastId = sinceId
    mentions = api.mentions_timeline(sinceId)      
    #reverse mentions array to reply to the oldest first
    mentions.reverse()
    for mention in mentions:    
        tweetId = mention.id        
        text = mention.text     
        user = mention.user.screen_name         
        if("#primerdowndd" in text.lower()):
            words = text.lower().split(" ")
            generator.imageCreator(words[2],words[3],"black","test")
            api.update_with_media(filename="test.png",status="@"+user+" There you go",in_reply_to_status_id=tweetId)
            count+=1
        lastId = tweetId
    return (len(mentions),lastId,count)


#Please note that the keys are stored in environment variables
auth = tweepy.OAuthHandler(os.environ["TW_CONSUMER_KEY"],os.environ["TW_CONSUMER_SECRET"])
auth.set_access_token(os.environ["TW_ACCESS_TOKEN"],os.environ["TW_ACCESS_SECRET"])
api = tweepy.API(auth)

while(True):
    try:
        with open("lastId.txt","r") as f:
            lastId = int(f.read().strip())

        mentionsN,newLastId,repliedN = checkStatus(lastId)
        print("Done, mentioned in" + str(mentionsN)+", replied to "+str(repliedN)+" tweets")

        with open("lastId.txt","w") as f:
            f.write(str(retValue[1]))

    except tweepy.RateLimitError as e:
        print("RateLimit: "+e.response.text)
        try:
            sendEmail(e.response.text)
        except Exception:
            print("Unable to send email")
        time.sleep(3600)
    except tweepy.TweepError as e:
        print("Error: "+e.response.text)

    time.sleep(15)
