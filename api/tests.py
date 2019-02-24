from django.test import TestCase


# Create your tests here.
class TestDjangoTests(TestCase):

    def tests_ten_equals_ten(self):
        self.assertEqual(10, 10)

    def test_ten_almost_equals_nine(self):
        self.assertAlmostEqual(10, 9, delta=1)
