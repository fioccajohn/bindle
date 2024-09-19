import pandas as pd

@pd.api.extensions.register_dataframe_accessor("bindle")
class BindleAccessor:
    "Bindle Pandas Extensions."

    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def moments(self):
        """Describe function for the first four statistical moments."""
        return self._obj.agg(['mean', 'var', 'skew', 'kurt'])
