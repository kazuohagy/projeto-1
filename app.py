from PIL import Image 

image1 = Image.open('banner-box-1.jpg')
image1.save('banner-box-2.webp', format='webp',quality=85)