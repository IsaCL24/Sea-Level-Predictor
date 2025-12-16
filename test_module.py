import unittest
import sea_level_predictor
import matplotlib as mpl


class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Rise in Sea Level'")
    
    def test_plot_x_label(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'Year'")

    def test_plot_y_label(self):
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'Sea Level (inches)'")

    def test_plot_num_lines(self):
        actual = len(self.ax.get_lines())
        expected = 2
        self.assertEqual(actual, expected, "Expected two lines on plot.")

    def test_plot_data_shape(self):
        actual = self.ax.get_lines()[0].get_ydata().shape
        expected = (171,)
        self.assertEqual(actual, expected, "Expected different line data.")

    def test_plot_data_shape_2(self):
        actual = self.ax.get_lines()[1].get_ydata().shape
        expected = (51,)
        self.assertEqual(actual, expected, "Expected different line data.")


if __name__ == "__main__":
    unittest.main()
