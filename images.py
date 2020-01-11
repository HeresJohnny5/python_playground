from PIL import Image, ImageFilter
im = Image.open('./astro.jpg')

im.thumbnail((300, 300))
im.save('small.png', 'png')
