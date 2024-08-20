import bindle
import pandas as pd
import pytest

class TestBindleAPI:

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_import_bindle(self):
        assert "bindle" in globals()

    def test_data_frane_has_bindle_namespace(self):
        assert hasattr(pd.DataFrame, 'bindle')

    def test_bindle_has_data_namespace(self):
        assert hasattr(pd.DataFrame.bindle, 'data')

    def test_bindle_data_has_from_bigquery(self):
        assert hasattr(pd.DataFrame.bindle.data, 'from_bigquery')

    def test_bindle_data_has_to_bigquery(self):
        assert hasattr(pd.DataFrame.bindle.data, 'to_bigquery')

    def test_bindle_data_has_from_trino(self):
        assert hasattr(pd.DataFrame.bindle.data, 'from_trino')

    def test_bindle_data_has_to_trino(self):
        assert hasattr(pd.DataFrame.bindle.data, 'to_trino')

    def test_bindle_has_model_namespace(self):
        assert hasattr(pd.DataFrame.bindle, 'model')

    def test_bindle_has_plot_namespace(self):
        assert hasattr(pd.DataFrame.bindle, 'plot')

    def test_bindle_has_stats_namespace(self):
        assert hasattr(pd.DataFrame.bindle, 'stats')

if __name__ == "__main__":
    pytest.main()
