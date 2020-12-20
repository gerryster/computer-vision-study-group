# This was helpful in understanding the project structure:
# https://stackoverflow.com/questions/61151/where-do-the-python-unit-tests-go
#
from lib import plot_gallery
from lib import exhibit

import matplotlib.pyplot as plt

class TestPlotGallery:
  def test_initialize_with_params(self):
    expected_title = 'test title'
    expected_columns = 2

    subject = plot_gallery.PlotGallery(columns=2, title=expected_title)

    assert subject.columns == expected_columns
    assert subject.title == expected_title

  def test_initialize_defaults_to_one_column(self):
    subject = plot_gallery.PlotGallery(title='foo')
    assert subject.columns == 1

  # def test_that_columns_must_be_greater_than_0(self):

  def test_opening_a_single_exhibit(self, monkeypatch):
    class FigureDouble:
      def suptitle(self, title):
        self.title = title

      def __eq__(self, obj):
        return isinstance(obj, FigureDouble) and obj.title == self.title

      def __ne__(self, obj):
        return not self == obj

    gallery_title = 'test gallery'
    expected_fig = FigureDouble()
    expected_fig.suptitle(gallery_title)

    fake_im = [[1,2],[3,4]]

    my_exhibit = exhibit.Exhibit(fake_im, title = 'exhibit 1')
    subject = plot_gallery.PlotGallery(gallery_title)
    subject.add_exhibit(my_exhibit)

    simulator_fig = FigureDouble()
    found_nrows = None
    found_ncols = None
    def mock_subplot(nrows, ncols):
      nonlocal found_nrows
      nonlocal found_ncols
      found_nrows = nrows
      found_ncols = ncols

      return simulator_fig, [42, 43]

    found_adjust_top = None
    def mock_subplots_adjust(top):
      # Note that "nonlocal" is required here but not in the "simulator_fig"
      # variable above since found_adjust_top is assigned. The behavior of
      # assignment is more restrictive/safe.
      nonlocal found_adjust_top
      found_adjust_top = top

    # Setup mocks:
    monkeypatch.setattr(plt, "subplots", mock_subplot)
    monkeypatch.setattr(plt, "subplots_adjust", mock_subplots_adjust)

    subject.open()

    assert simulator_fig.title == expected_fig.title
    assert found_adjust_top == 1.2

    assert found_nrows == 1
    assert found_ncols == 1
