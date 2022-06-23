from django.test import SimpleTestCase

from app.calc import add


class CalcTests(SimpleTestCase):
    def test_add(self):
        # Given
        x, y = 3, 4

        # With
        res = add(x, y)

        # Then
        res = 7
