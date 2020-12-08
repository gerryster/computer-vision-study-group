#
# Based on "Programming Computer Vision with Python" by Jan Erik Solem
# (O'Reilly Media, 2012)
#
import os
from PIL import Image
from pylab import *

def get_imlist(path, extention='.jpg'):
  """ Returns a list of filenames for all jpg images in a directory. """
  return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(extention)]

def imresize(im,sz):
  """
  Resize an image array using PIL.

  :param im: A ndarray of image data
  :param sz: The requested size in pixels, as a 2-tuple: (width, height).
  """
  pil_im = Image.fromarray(im.astype(np.uint8))

  # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize
  return array(pil_im.resize(sz))
