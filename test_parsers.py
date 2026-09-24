
import unittest

from models import Planet, Moon, Crater
from parsers import Parser
from errors import ParseError


class TestParserCorrect(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_planet(self):
        p = self.parser.parse_line(
            'planet Земля "Земля" 2024.01.15 4.0 10.0 10.0')
        self.assertIsInstance(p, Planet)
        self.assertEqual(p.name, "Земля")
        self.assertEqual(p.date, "2024.01.15")
        self.assertEqual(p.radius, 4.0)
        self.assertEqual(p.x, 10.0)
        self.assertEqual(p.y, 10.0)

    def test_moon(self):
        m = self.parser.parse_line(
            'moon Луна "Луна" 2024.02.01 "Земля" 384400.0')
        self.assertIsInstance(m, Moon)
        self.assertEqual(m.name, "Луна")
        self.assertEqual(m.planet_name, "Земля")
        self.assertEqual(m.distance, 384400.0)

    def test_crater(self):
        c = self.parser.parse_line(
            'crater Гершель "Гершель" 2024.03.12 "Марс" 120.5 3.2')
        self.assertIsInstance(c, Crater)
        self.assertEqual(c.name, "Гершель")
        self.assertEqual(c.planet_name, "Марс")
        self.assertEqual(c.diameter, 120.5)
        self.assertEqual(c.depth, 3.2)

    def test_case_insensitive_prefix(self):
        p = self.parser.parse_line(
            'PLANET Земля "Земля" 2024.01.15 4.0 10.0 10.0')
        self.assertIsInstance(p, Planet)


class TestParserErrors(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_unknown_type(self):
        with self.assertRaises(ParseError):
            self.parser.parse_line('robot Марс "Марс" 2024.01.15 4.0 10.0')

    def test_no_space(self):
        with self.assertRaises(ParseError):
            self.parser.parse_line('planet')

    def test_no_quotes(self):
        with self.assertRaises(ParseError):
            self.parser.parse_line('planet Земля 2024.01.15 4.0 10.0 10.0')

    def test_empty_quotes(self):
        with self.assertRaises(ParseError):
            self.parser.parse_line('planet "" 2024.01.15 4.0 10.0 10.0')

    def test_bad_date(self):
        with self.assertRaises(ParseError):
            self.parser.parse_line(
                'planet Земля "Земля" 2024-01-15 4.0 10.0 10.0')

    def test_bad_number(self):
        with self.assertRaises(ParseError):
            self.parser.parse_line(
                'planet Земля "Земля" 2024.01.15 abc 10.0 10.0')

    def test_missing_parts(self):
        with self.assertRaises(ParseError):
            self.parser.parse_line(
                'planet Земля "Земля" 2024.01.15 4.0')


if __name__ == "__main__":
    unittest.main()