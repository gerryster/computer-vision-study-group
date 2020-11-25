#
# Based on "Programming Computer Vision with Python" by Jan Erik Solem
# (O'Reilly Media, 2012)
#
import os

def get_imlist(path, extention='.jpg'):
  """ Returns a list of filenames for all jpg images in a directory. """
  return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(extention)
