import cv2
from matplotlib import pyplot as plt
from PIL import Image as ImgPil
from IPython.display import Image
import numpy

img = ImgPil.open("saltAndPepperNoise1.png").convert("L")
arr = numpy.array(img)
print('...')