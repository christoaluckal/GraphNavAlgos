from PIL import Image
import numpy as np
import pickle as pk

#PIL loading and getting image data
im = Image.open('world_4k.jpg') #Change this to any image
pix = im.load()
width,height = im.size

coord_list = []

print(width*height)

for i in range(width):
    for j in range(height):
        temp_check = list(pix[i,j])
        # Here we assume that a pixel is valid if it is not completely white. Any color other than white is permitted
        if temp_check[0] < 200 or temp_check[1] < 200 or temp_check[2] < 200:
            coord_list.append((i,height-j))

print(len(coord_list))
pk.dump(coord_list,open("shapes.pkl",'wb'))