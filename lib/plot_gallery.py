import matplotlib.pyplot as plt

""" Create a "gallery" of items in a specified number of rows using MatPlotLib.
"""
class PlotGallery:
  def __init__(self, title, columns=1):
    self.columns = columns
    self.title = title
    self.exhibits = []

  def add_exhibit(self, exhibit):
    self.exhibits.append(exhibit)

  def open(self):
    # rcParams['figure.dpi'] = 300
    fig, axes = plt.subplots(1, 4)
    fig.suptitle(self.title)

    # Reudce vertical space after the title. This is magic to me at this point.
    plt.subplots_adjust(top=1.2)

    # ax1.set_title('Original', fontsize=8)
    # ax1.imshow(im)
    # ax1.axis('off')

    # ax2.set_title('X Derivative', fontsize=8)
    # ax2.imshow(Image.fromarray(abs(imx).round(0).astype(np.uint8)))
    # ax2.axis('off')

    # ax3.set_title('Y Derivative', fontsize=8)
    # ax3.imshow(Image.fromarray(abs(imy).round(0).astype(np.uint8)))
    # ax3.axis('off')

    # ax4.set_title('Magnitude', fontsize=8)
    # ax4.imshow(Image.fromarray(abs(magnitude).round(0).astype(np.uint8)))
    # ax4.axis('off')

    plt.show()

    # rcParams['figure.dpi'] = 72
