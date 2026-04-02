import unittest
from unittest.mock import patch
import io
import report_generator


class TestReportGenerator(unittest.TestCase):
    def test_calculate_total_empty(self):
        self.assertEqual(report_generator.calculate_total([]), 0)

    def test_calculate_total_with_values(self):
        transactions = [
            {"date": "2026-03-01", "amount": 100},
            {"date": "2026-03-02", "amount": 50.5},
            {"date": "2026-03-03", "amount": -25},
        ]
        self.assertAlmostEqual(report_generator.calculate_total(transactions), 125.5)

    def test_filter_by_month_matches(self):
        transactions = [
            {"date": "2026-04-01", "amount": 10},
            {"date": "2026-04-15", "amount": 20},
            {"date": "2026-05-01", "amount": 30},
        ]
        april = report_generator.filter_by_month(transactions, "2026-04")
        self.assertEqual(len(april), 2)
        self.assertEqual(april[0]["date"], "2026-04-01")
        self.assertEqual(april[1]["amount"], 20)

    def test_filter_by_month_no_matches(self):
        transactions = [
            {"date": "2026-06-01", "amount": 40},
        ]
        self.assertEqual(report_generator.filter_by_month(transactions, "2026-07"), [])

    def test_generate_report_prints_expected_summary(self):
        sample_transactions = [
            {"date": "2026-01-05", "amount": 100},
            {"date": "2026-01-10", "amount": 150},
            {"date": "2026-02-01", "amount": 125},
        ]

        expected_output = (
            "January Total:  $250 (2 txns)\n"
            "February Total: $125 (1 txns)\n"
            "Q1 Total:       $375 (3 txns)\n"
        )

        with patch.object(report_generator, "transactions", sample_transactions):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                report_generator.generate_report()
                self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
