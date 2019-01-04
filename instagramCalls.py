from InstagramAPI import InstagramAPI
import time
import datetime
import json

def postProgressImage(postPercentage):
    instagramAPI = InstagramAPI("Username", "Password")
    instagramAPI.login()

    imagePath = 'progress images/progress.jpg'
    caption = str(postPercentage) + "% of the year completed.\nFollow @yearprogress for regular updates.\n\n#yearprogress"
    instagramAPI.uploadPhoto(imagePath, caption = caption)

def getLastUploadDate():
    instagramAPI = InstagramAPI("Username", "Password")
    instagramAPI.login()

    minTimeStamp = int(time.time()) - (86400*10)
    stringLast2Posts = instagramAPI.getTotalUserFeed(instagramAPI.username_id, minTimeStamp)
    jsonLast2Posts = json.loads(json.dumps(stringLast2Posts))
    
    if jsonLast2Posts == []:
        print("list is null")
        return datetime.datetime.fromtimestamp(0).date(), 0
    else:
        lastPost = jsonLast2Posts[0]
        lastPercent = lastPost['caption']['text']
        lastPercent = lastPercent.split('%')
        lastPercent = int(lastPercent[0])
        return datetime.datetime.fromtimestamp(int(lastPost['taken_at'])).date(), lastPercent