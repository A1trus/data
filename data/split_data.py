"""
Contains functions to split the dataset into its parts like
training, validation, testing, and x and y
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from .constants import LABEL_COLUMNS, RANDOM_SEED

def split_xy(data: pd.DataFrame) -> 'tuple[pd.DataFrame, ...]':
    """
    Split a dataframe into two dataframes, one containing all the x
    variables and the other containing the y variables.  Which columns
    are considered y variables comes from the LABEL_COLUMNS constant

    RETURNS a tuple of dataframes representing x, y
    """
    x = data.drop(columns=LABEL_COLUMNS).copy()
    y = data[LABEL_COLUMNS].copy()
    return x, y

def split_tvt(data: pd.DataFrame, perc: float) -> 'tuple[pd.DataFrame, ...]':
    """
    Splits a dataframe into train_x, train_y, validate_x, validate_y, test_x, test_y
    perc is the percentage of the data (from 0 to 1) that will be in the test set
    Returns a tuple of dataframes in the order listed above 
    """
    train, test = train_test_split(data, test_size=perc, shuffle=True, random_state=RANDOM_SEED)
    train, validate = train_test_split(train, test_size=perc, shuffle=True, random_state=RANDOM_SEED)
    train_x, train_y = split_xy(train)
    validate_x, validate_y = split_xy(validate)
    test_x, test_y = split_xy(test)
    return train_x, train_y, validate_x, validate_y, test_x, test_y
