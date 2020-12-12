from PIL import Image
import sys

path=sys.argv[0]
img=Image.open('1.jpg')

width,heigth=img.size
aspect_ratio=heigth/width
new_width=100
new_height=aspect_ratio*new_width
img=img.resize((new_width,int(new_height)))

img=img.convert('L')
pixel=img.getdata()

character=["@","#","S","%","?","*","+",";",":",",","."]

new_pixel=[character[pixels//25] for pixels in pixel]
new_pixel=''.join(new_pixel)

new_pixel_count=len(new_pixel)
final_image=[new_pixel[index:index+new_width] for index in range(0,new_pixel_count,new_width)]
final_image='\n'.join(final_image)

with open("2.txt","w") as f:
	f.write(final_image)