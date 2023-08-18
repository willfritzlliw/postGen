import random
from time import time
import time
from datetime import datetime
import schedule
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap3

def generate():
    """
        Generates post from picture and text file
    """
    imgpath, quote = get_files()

    #image processing 
    img = Image.open(str(imgpath))

    #image cropping
    width, height = img.size   # Get dimensions
    new_width = 1080
    new_height = 1350
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    # Crop the center of the image
    img = img.crop((left, top, right, bottom))

    #adding text
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Chiefland.ttf',50)
    width, height = img.size
    newquote = textwrap3.wrap(quote,width=35)
    quote = "\n".join(newquote)
    _, _, w, h = draw.textbbox((0, 0), quote, font=font)
    draw.text(((width-w)/2,(height-h)/2),quote,(255,255,255),font)
    img.save(f'Mount/output/{quote[:15].replace(" ","-")}.jpg')

def get_files() -> list:
    """
       Retrives image and quote files for post generation
    """
    
    imgpath = os.listdir('Mount/img')
    randimgnum = random.randint(0,(len(imgpath)-1))
    randimgpath = 'Mount/img/'+imgpath[randimgnum]

    randquote = 'Stay Hard!'

    with open('Mount\quotes.txt') as f:
        content = f.readlines()
        num_quotes = len(content)
        randquotenum = random.randint(0,(num_quotes-1))
        randquote = content[randquotenum]

    return randimgpath, randquote

##########################    Job Scheduling     ################################ 

if __name__ == '__main__':
    generate()
    # schedule.every().day.at("07:00:00").do(generate)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)