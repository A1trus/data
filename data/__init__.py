"""
Data module
Contains everything to do with the data prior to use in the model
    - Retrevial (get_data)
    - Data Cleaning (clean_data)
    - Train / Validation / Test split (split_data)

Usage of this module looks like this:
```
from data import train_x, train_y, validate_x, validate_y, test_x, test_y
```
"""


from .get_data import raw_data
from .clean_data import clean
from .split_data import split_tvt

# Clean the data
cleaned_data = clean(raw_data)

# Split the data
train_x, train_y, validate_x, validate_y, test_x, test_y = split_tvt(cleaned_data, 0.2)

# Variables to be exported from this module
__all__ = [
    'raw_data',
    'cleaned_data',
    'train_x',
    'train_y',
    'validate_x',
    'validate_y',
    'test_x',
    'test_y'
]