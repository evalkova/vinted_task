import unittest
from etl import extract
from mock import MagicMock, patch, Mock


class TestExtract(unittest.TestCase):

    def setUp(self):
        data_sources = MagicMock()
        self.extractor = extract.Extractor(data_sources)

    # TODO:
    def test_load_json_files_to_df(self):
        pass


if __name__ == '__main__':
    unittest.main()
