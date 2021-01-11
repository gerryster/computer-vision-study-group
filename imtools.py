#
# Based on "Programming Computer Vision with Python" by Jan Erik Solem
# (O'Reilly Media, 2012)
#
import os
import numpy as np
from PIL import Image
from pylab import *
from scipy.ndimage import filters

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

def resize(im, factor):
  return im.resize((int(im.width * factor), int(im.height * factor)))

# TODO: test me
# def to_image(image_like):
  # Image.fromarray(image_like)

# Perform gaussian blur
# Works on both color and grayscale images
# Stolen from https://github.com/donjwood/ComputerVision/blob/9e8458aa8deeceeba8ca5a671e7af2e196086ab7/common/imtools.py#L28
def gaussian_blur(im, sigma):
  if len(im.shape) == 3:
    im_blur = np.empty_like(im)
    for i in range(3):
      im_blur[:,:,i] = filters.gaussian_filter(im[:,:,i],sigma)
      im_blur = np.uint8(im_blur)
  else:
    im_blur = filters.gaussian_filter(im,sigma)
  return im_blur
