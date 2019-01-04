from PIL import Image, ImageDraw, ImageFont
import instagramCalls as insta
import random
from time import sleep
import datetime
import math

def generateStyleString(progressPercent):
    low = '-'
    high = "#"
    numberOfHighs = math.floor(progressPercent//4)
    progressString = '['
    for i in range (0, 25):
        if i < numberOfHighs:
            progressString += high
        else:
            progressString += low
    
    return progressString + "]"

def generateAndSave(progressPercent):
    Width = 500
    Height = 500

    imageBg = [(21,32,43), (255, 105, 31), (250, 184, 30), 
    (232, 28, 79), (25, 207, 134), (27, 149, 224), (245, 142, 168)]
    
    white = (255,255,255)

    image = Image.new('RGB', (500,500), color = imageBg[random.randint(0,6)])
    draw = ImageDraw.Draw(image)

    fntGraph = ImageFont.truetype('fonts/digital7.ttf', 35)
    fntPercent = ImageFont.truetype('fonts/digital7.ttf', 100)
    fntTitle = ImageFont.truetype('fonts/Product Sans Regular.ttf', 30)
    fntUsername = ImageFont.truetype('fonts/Product Sans Regular.ttf', 15)

    title = "Year Progress!"
    w, h = fntTitle.getsize(title)
    draw.text(((Width-w)/2, h), title, fill=white, font=fntTitle)
    
    percent = str(progressPercent) + "%"
    w, h = fntPercent.getsize(percent)
    draw.text(((Width-w)/2, (Height-h)/2 - 40), percent, fill=white, font=fntPercent)

    progressString = generateStyleString(progressPercent)
    w, h = fntGraph.getsize(progressString)
    draw.text(((Width-w)/2, (Height-h)/2 + 60), progressString, fill=white, font=fntGraph)

    username = "@yearprogress"
    w, h = fntUsername.getsize(username)
    draw.text((Width - (w+10),Height - 30), username, fill=white, font=fntUsername)

    # image.show()
    image.save("progress images/progress.jpg", format='JPEG', subsampling=0, quality=100)
    sleep(2)
    insta.postProgressImage(progressPercent)