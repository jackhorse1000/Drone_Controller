from PIL import Image, ImageDraw

def genCircle(colour1, colour2, colour3):
    image = Image.new('RGBA', (300, 300))
    draw = ImageDraw.Draw(image)
    draw.ellipse((20, 20, 80, 80), fill=colour1, outline='black')
    draw.point((100, 100), 'red')

    image2 = Image.new('RGBA', (300, 300))
    draw2 = ImageDraw.Draw(image)
    draw2.ellipse((100, 20, 160, 80), fill=colour2, outline='black')
    draw2.point((100, 100), 'red')


    image3 = Image.new('RGBA', (300, 300))
    draw3 = ImageDraw.Draw(image)
    draw3.ellipse((180, 20, 240, 80), fill=colour3, outline='black')
    draw3.point((100, 100), 'red')

    image.save('circles.png')


genCircle('green', 'red', 'green')
