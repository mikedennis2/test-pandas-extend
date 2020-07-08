import pandas as pd 


class My_class:
    def __init__(self):
        self.my_attrib = 10
        self.my_other_attrib = 20
        
    def __str__(self):
        return 'my_attrib: {}, my_other_attrib: {}'.format(str(self.my_attrib), str(self.my_other_attrib)) 
    

@pd.api.extensions.register_dataframe_accessor("my_accessor")
class My_class_accessor:
    def __init__(self, pd_object):
        self._validate(pd_object)
        self._obj = pd_object

    @staticmethod
    def _validate(obj):
        # verify there is a column latitude and a column longitude
        if 'my_class_col' not in obj.columns:
            raise AttributeError("Must have 'my_class_col'.")

    def my_method(self):
        return self._obj.my_class_col.iloc[0] 