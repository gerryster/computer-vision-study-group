import math
import matplotlib
import matplotlib.pyplot as plt
import numpy


class PlotGallery:
  """
  Create a "gallery" of items in a specified number of rows using MatPlotLib.
  """
  def __init__(self, title, columns=1):
    if columns < 1: raise ValueError('columns can not be less than 1')
    self.columns = columns
    self.title = title
    self.exhibits = []

  def add_exhibit(self, exhibit):
    self.exhibits.append(exhibit)

  def open(self):
    # TODO: figure out a better way of modifying DPI:
    dpi_orig = matplotlib.rcParams['figure.dpi']
    matplotlib.rcParams['figure.dpi'] = 300

    fig, axes = plt.subplots(self.rows(), self.columns)
    fig.suptitle(self.title)

    # Reudce vertical space after the title. This is magic to me at this point.
    plt.subplots_adjust(top=1.2)

    self._plot_axes(axes)

    plt.show()

    matplotlib.rcParams['figure.dpi'] = dpi_orig

  def rows(self):
    return math.ceil(len(self.exhibits) / self.columns)

  def _plot_axes(self, axes):
    # Flatten the potentially 2D array for ease of processing:
    flat_axes = numpy.array(axes).flatten()

    for i in range(len(self.exhibits)):
      axis = flat_axes[i]
      exhibit = self.exhibits[i]

      axis.set_title(exhibit.title, fontsize=8)
      axis.imshow(exhibit.image)
      axis.axis(exhibit.axis)



class Exhibit:
  """
  An item to display in a PlotGallery.
  """
  def __init__(self, image, title, axis = 'off'):
    self.axis = axis
    self.image = image
    self.title = title
