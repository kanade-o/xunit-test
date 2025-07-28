import os
import unittest

from xunit_test.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))

    def test_read_each(self):
        printer = CSVPrinter("sample.csv")
        count = 0
        for line in printer.read():
            count += 1
        self.assertEqual(3, count)

    def test_is_exist_file(self):
        with self.assertRaises(RuntimeError):
            CSVPrinter("sample2.csv")



if __name__ == '__main__':
    unittest.main()
