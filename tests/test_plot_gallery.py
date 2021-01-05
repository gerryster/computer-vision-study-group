# This was helpful in understanding the project structure:
# https://stackoverflow.com/questions/61151/where-do-the-python-unit-tests-go
#
from lib.plot_gallery import PlotGallery
from lib.plot_gallery import Exhibit

import matplotlib.pyplot as plt
import pytest

# Double of matplotlib.figure.Figure:
class FigureDouble:
  def suptitle(self, title):
    self.title = title

# Double of matplotlib.axes.Axes:
class AxesDouble:
  def __init__(self):
    self.shown = False
    self.axis_setting = None

  def set_title(self, title, fontsize):
    self.title = title
    self.fontsize = fontsize

  def imshow(self, image):
    self.image = image
    self.shown = True

  def axis(self, setting):
      self.axis_setting = setting
class TestPlotGallery:
  def test_initialize_with_params(self):
    expected_title = 'test title'
    expected_columns = 2

    subject = PlotGallery(columns=2, title=expected_title)

    assert subject.columns == expected_columns
    assert subject.title == expected_title

  def test_initialize_defaults_to_zero_columns(self):
    subject = PlotGallery(title='foo')
    assert subject.columns == 0

  def test_that_columns_must_be_greater_than_0(self):
    with pytest.raises(ValueError):
      PlotGallery(columns = -1, title = 'broken')

  @pytest.fixture
  def fake_image(self):
    return [[1,2],[3,4]]

  @pytest.fixture
  def simulator_fig(self):
    return FigureDouble()

  @pytest.fixture
  def subplot_adjust_noop(self, monkeypatch):
    def mock_subplots_adjust(top):
      42
    monkeypatch.setattr(plt, "subplots_adjust", mock_subplots_adjust)

  def test_exhibit_attributes_are_passed_into_matplotlib_axes(
    self, monkeypatch, fake_image, simulator_fig, subplot_adjust_noop):
    gallery_title = 'test gallery'
    expected_fig = FigureDouble()
    expected_fig.suptitle(gallery_title)

    my_exhibit = Exhibit(fake_image, title = 'exhibit 1')
    subject = PlotGallery(gallery_title)
    subject.add_exhibit(my_exhibit)

    simulator_axes = []
    found_nrows = None
    found_ncols = None
    def mock_subplot(nrows, ncols):
      nonlocal found_nrows
      nonlocal found_ncols
      found_nrows = nrows
      found_ncols = ncols

      for i in range(0, nrows * ncols):
        simulator_axes.append(AxesDouble())

      return simulator_fig, simulator_axes

    monkeypatch.setattr(plt, "subplots", mock_subplot)

    subject.open()

    assert simulator_fig.title == expected_fig.title

    assert found_nrows == 1
    assert found_ncols == 1

    assert len(simulator_axes) == 1

    found_axis = simulator_axes[0]
    expected_axis_state = {
      'axis_setting': 'off',
      'fontsize': 8,
      'image': my_exhibit.image,
      'shown': True,
      'title': my_exhibit.title,
    }

    assert found_axis.title == my_exhibit.title
    assert found_axis.__dict__ == expected_axis_state

  def subplot_forward_simulator_axes(self, monkeypatch, simulator_axes):
    """
    Monkey patch plot.subplots to return the passed in simulator_axes
    """
    def mock_subplot(nrows, ncols):
      return FigureDouble(), simulator_axes

    monkeypatch.setattr(plt, "subplots", mock_subplot)

  def test_exhibits_can_opt_into_displaying_axes(self, fake_image, monkeypatch, subplot_adjust_noop):
    simulator_axes = [AxesDouble(), AxesDouble()]
    self.subplot_forward_simulator_axes(monkeypatch, simulator_axes)

    axis_on_exhibit = Exhibit(fake_image, title = 'axis on', axis = 'on')
    default_axis_exhibit = Exhibit(fake_image, title = 'default axis')

    subject = PlotGallery(title = 'test')
    subject.add_exhibit(axis_on_exhibit)
    subject.add_exhibit(default_axis_exhibit)
    subject.open()

    assert simulator_axes[0].axis_setting == 'on'
    assert simulator_axes[1].axis_setting == 'off'

  def test_rendering_multiple_rows(
    self, monkeypatch, fake_image, simulator_fig, subplot_adjust_noop):
    simulator_axes = [
      [AxesDouble(), AxesDouble()],
      [AxesDouble(), AxesDouble()],
    ]
    self.subplot_forward_simulator_axes(monkeypatch, simulator_axes)

    subject = PlotGallery(title = 'two rows', columns = 2)
    subject.add_exhibit(Exhibit(fake_image, '1'))
    subject.add_exhibit(Exhibit(fake_image, '2'))
    subject.add_exhibit(Exhibit(fake_image, '3, on a second row'))
    subject.open()

    assert simulator_axes[0][0].title == '1'
    assert simulator_axes[0][1].title == '2'
    assert simulator_axes[1][0].title == '3, on a second row'

  def test_rendering_one_row_adjusts_the_top_height(
    self, monkeypatch, fake_image, simulator_fig):
    self.subplot_forward_simulator_axes(monkeypatch, [AxesDouble()])

    found_adjust_top = None
    def mock_subplots_adjust(
      left=None, bottom=None, right=None, top=None, wspace=None, hspace=None):
      # Note that "nonlocal" is required here but not in the "simulator_fig"
      # variable above since found_adjust_top is assigned. The behavior of
      # assignment is more restrictive/safe.
      nonlocal found_adjust_top
      found_adjust_top = top
    monkeypatch.setattr(plt, "subplots_adjust", mock_subplots_adjust)

    subject = PlotGallery(title = 'One Row', columns = 1)
    subject.add_exhibit(Exhibit(fake_image, 'does not matter'))
    subject.open()

    assert found_adjust_top == 1.3

  def test_rendering_multiple_rows_uses_no_top_height(
    self, monkeypatch, fake_image, simulator_fig, subplot_adjust_noop):
    self.subplot_forward_simulator_axes(monkeypatch, [AxesDouble(), AxesDouble()])

    found_adjust_top = None
    def mock_subplots_adjust(
      left=None, bottom=None, right=None, top=None, wspace=None, hspace=None):
      nonlocal found_adjust_top
      found_adjust_top = top
    monkeypatch.setattr(plt, "subplots_adjust", mock_subplots_adjust)

    subject = PlotGallery(title = 'Two Rows', columns = 1)
    subject.add_exhibit(Exhibit(fake_image, 'on first row'))
    subject.add_exhibit(Exhibit(fake_image, 'on second row'))
    subject.open()

    assert found_adjust_top == None
