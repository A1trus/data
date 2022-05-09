"""
Contains functions which will clean the data
"""

import pandas as pd

def clean(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the supplied dataframe
    """
    return data.dropna().copy()