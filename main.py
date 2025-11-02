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
    """Generates an image with a quote overlay.

    This function takes an image, crops it to a specific size, and overlays a randomly selected quote on it. 
    The resulting image is then saved to the 'Mount/output' directory.

    The function performs the following steps:
    1. Retrieves an image path and a quote using the `get_files` function.
    2. Opens and crops the image to 1080x1350 pixels.
    3. Wraps the quote text to fit the image width.
    4. Draws the wrapped text onto the center of the image.
    5. Saves the final image with a filename derived from the quote.
    6. Deletes the original image file.

    Raises:
        FileNotFoundError: If the font file 'Chiefland.ttf' is not found.
        IOError: If there is an issue with image processing or saving.
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

    os.remove(imgpath)
    

def get_files() -> list:
    """Retrieves a random image path and a random quote.

    This function selects a random image from the 'Mount/img' directory and a random quote from the 'Mount/quotes.txt' file.

    Returns:
        list: A list containing the following two items:
            - str: The path to a randomly selected image file.
            - str: A randomly selected quote.

    Raises:
        FileNotFoundError: If the 'Mount/img' directory or the 'Mount/quotes.txt' file is not found.
        IndexError: If the 'Mount/img' directory is empty.
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
    files = True

    while files:
        generate()
        if len(os.listdir('Mount/img')) > 0:
            files = True
        else:
            files = False
    # schedule.every().day.at("07:00:00").do(generate)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)