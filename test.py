import my_class 
from my_class import My_class
import pandas as pd  

test_df = pd.DataFrame({'col' : [0], 
    'my_class_col' : [My_class()]})

print(test_df.my_accessor.my_method()) 
# prints: my_attrib: 10, my_other_attrib: 20

