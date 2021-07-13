import unittest
import pandas as pd
import logging
from etl import transform
from mock import MagicMock, patch, Mock


class TestTransform(unittest.TestCase):

    def setUp(self):
        self.transformer = transform.Transformer()

    def test_check_if_unique_id_true(self):
        df = pd.DataFrame({'id': [1, 2, 3, 4, 5]})
        self.assertTrue(self.transformer.check_if_unique_id(df, 'id'))

    def test_check_if_unique_id_false(self):
        df = pd.DataFrame({'id': ['a', 'b', 'a']})
        self.assertFalse(self.transformer.check_if_unique_id(df, 'id'))

    def test_check_missing_values(self):
        df = pd.DataFrame({'id': [1, None, 3, 4, 5]})
        with self.assertLogs() as captured:
            self.transformer.check_missing_values(df)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].levelno, logging.INFO)

    def test_check_missing_values_error(self):
        df = 'string'
        with self.assertLogs() as captured:
            self.transformer.check_missing_values(df)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].levelno, logging.ERROR)

    def test_cleanup_description(self):
        self.assertEqual('2', self.transformer.cleanup_description('Max. 2 kg, 38 × 26,5 × 3,2 cm'))

if __name__ == '__main__':
    unittest.main()
