from PIL import Image, ImageDraw, ImageFont
import sys

def imageCreator(name,number,color):
    img = Image.open("Assets/Black.png") if color=="black" else Image.open("Assets/White.png")
    cnv = ImageDraw.Draw(img)

    font_path = "Assets/big_noodle_titling.ttf"
    numberFont = ImageFont.truetype(font_path, 1000)
    nameFont = ImageFont.truetype(font_path,nameFontSize(name,font_path,cnv))

    textCol = "#ffffff" if color=="black" else "#000000"
    cnv.text((center(cnv.textsize(number,font=numberFont)),505),number,textCol,font=numberFont)
    cnv.text((center(cnv.textsize(name,font=nameFont)),190),name,textCol,font=nameFont)
    img.save(name+number+color+".png")

def center(di):
    return int((1080-di[0])/2)

def nameFontSize(name,font_path,cnv):
    if(cnv.textsize(name,ImageFont.truetype(font_path,250))[0]<950): return 250
    else: return int(237500/cnv.textsize(name,ImageFont.truetype(font_path,250))[0]) 

imageCreator(sys.argv[1],sys.argv[2],sys.argv[3])

