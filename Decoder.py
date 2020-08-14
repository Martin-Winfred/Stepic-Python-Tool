'''
Martin made
'''
import stepic
from PIL import Image
img=(input("Full file name"))
im=Image.open(img)
data=stepic.decode(im)
print(str(data))