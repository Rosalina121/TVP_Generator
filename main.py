import sys
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from random import *

tvp_list = ["tvp.png", "tvp2.png", "tvp3.png"]


def main():
    font = ImageFont.truetype("font.ttf", 25)

    text = input("Tekst: ")

    imageFile = choice(tvp_list)
    im1 = Image.open(imageFile)

    draw = ImageDraw.Draw(im1)
    draw.text((141, 328), text, (255, 255, 255), font=font)
    draw = ImageDraw.Draw(im1)

    im1.save("tvp_out.png")


if __name__ == '__main__':
    main()
