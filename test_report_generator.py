import unittest
from io import StringIO
import sys
import report_generator

class TestReportGenerator(unittest.TestCase):

    def test_calculate_month_total_january(self):
        total, count = report_generator.calculate_month_total("January")
        expected_total = 100.50 + 200.75 + 300.00 + 400.00 + 728.47
        self.assertEqual(total, expected_total)
        self.assertEqual(count, 5)

    def test_calculate_month_total_february(self):
        total, count = report_generator.calculate_month_total("February")
        expected_total = 100.50 + 200.75 + 300.00 + 400.00 + 728.47
        self.assertEqual(total, expected_total)
        self.assertEqual(count, 5)

    def test_calculate_month_total_march(self):
        total, count = report_generator.calculate_month_total("March")
        self.assertEqual(total, 0)
        self.assertEqual(count, 0)

    def test_generate_report_output(self):
        # Capture the output of generate_report
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            report_generator.generate_report()
            output = captured_output.getvalue()
            expected_lines = [
                "January Total:  $1729.72 (5 txns)",
                "February Total: $1729.72 (5 txns)",
                "Q1 Total:       $3459.44 (10 txns)"
            ]
            actual_lines = output.strip().split('\n')
            for expected, actual in zip(expected_lines, actual_lines):
                self.assertEqual(actual, expected)
        finally:
            sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
