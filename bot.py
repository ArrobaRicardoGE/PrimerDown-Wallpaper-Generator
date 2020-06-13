import tweepy,time,generator,os,emailSender,codecs

def checkStatus(sinceId):
    count = 0
    errors = 0
    lastId = sinceId
    mentions = api.mentions_timeline(sinceId)      
    #reverse mentions array to reply to the oldest first
    mentions.reverse()
    for mention in mentions:    
        tweetId = mention.id        
        text = mention.text     
        user = mention.user.screen_name         
        if("#primerdownwpp" in text.lower()):
            try:
                words = text.lower().split(" ")
                if(len(words)!=5 or not words[3].isdigit()):raise Exception
                color = "black" if(words[4]=="negro") else "white"
                generator.imageCreator(words[2],words[3],color,"response")
                api.update_with_media(filename="response.png",status="@"+user+" 😁🏈",in_reply_to_status_id=tweetId)
                count+=1
            except Exception:
                with open("errormsg.txt","r",encoding="utf-8") as f:
                    msg = f.read()
                api.update_status(status="@"+user+" "+msg,in_reply_to_status_id=tweetId)
                errors+=1
        lastId = tweetId
    return (len(mentions),lastId,count,errors)


#Please note that the keys are stored in environment variables
auth = tweepy.OAuthHandler(os.environ["TW_CONSUMER_KEY"],os.environ["TW_CONSUMER_SECRET"])
auth.set_access_token(os.environ["TW_ACCESS_TOKEN"],os.environ["TW_ACCESS_SECRET"])
api = tweepy.API(auth)

while(True):
    try:
        with open("lastId.txt","r") as f:
            lastId = int(f.read().strip())

        mentionsN,newLastId,repliedN,errors = checkStatus(lastId)
        print("Done, mentioned in " + str(mentionsN)+", replied to "+str(repliedN)+" tweets, "+str(errors)+" errors")

        with open("lastId.txt","w") as f:
            f.write(str(newLastId))

    except tweepy.RateLimitError as e:
        print("RateLimit: "+e.response.text)
        try:
            emailSender.sendEmail(e.response.text)
        except Exception:
            print("Unable to send email")
        time.sleep(3600)
    except tweepy.TweepError as e:
        print("Error: "+e.response.text)

    time.sleep(15)
