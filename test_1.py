import unittest

from rectangle import Rectangle

class TestGetAreaRectangle(unittest.TestCase):
  def setUp(self):
      self.rectangle = Rectangle(0, 0)

  def test_normal_case(self):
    self.rectangle.set_width(3)
    self.rectangle.set_height(2)
    self.assertionEqual(self.rectangle.get_area(), 6, "incorrect area")

  def test_normal_case(self):
    self.rectangle.set_width(-1)
    self.rectangle.set_height(2)
    self.assertionEqual(self.rectangle.get_area(), -1, "incorrect area")


if __name__ == "__main__":
  unittest.main()
