import unittest

# This was helpful in understanding the project structure:
# https://stackoverflow.com/questions/61151/where-do-the-python-unit-tests-go
#
# Unit testing in general: https://docs.python.org/3/library/unittest.html
from lib import plot_gallery

class TestPlotGallery(unittest.TestCase):

  def test_initialize_with_params(self):
    expected_title = 'test title'
    expected_columns = 2

    subject = plot_gallery.PlotGallery(columns=2, title=expected_title)

    self.assertEqual(subject.columns, expected_columns)
    self.assertEqual(subject.title, expected_title)

  def test_initialize_defaults_to_one_column(self):
    subject = plot_gallery.PlotGallery(title='foo')
    self.assertEqual(subject.columns, 1)
