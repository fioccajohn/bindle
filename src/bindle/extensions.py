import pandas as pd

@pd.api.extensions.register_dataframe_accessor("bindle")
class BindleAccessor:
    "Bindle Pandas Extensions."

    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def moments(self):
        """Describe function for the first four statistical moments."""
        return self._obj.agg(['mean', 'var', 'skew', 'kurt'])

    def convert_columns_to_type(self, *args, dtype=None, **kwargs):
        if dtype is None:
            raise ValueError("The 'dtype' parameter must be specified.")

        # Create the dictionary comprehension for the columns
        type_mapping = {column: dtype for column in args}

        # Use astype with the mapping and additional kwargs
        return self._obj.astype(type_mapping, **kwargs)

    def assign_group_transform(self, new_column_name, groupby_key, function):
        pass

        # df = self._obj.assign({new_column_name: self._obj.groupby(groupby_key).transform(function)})
        
        # return df
