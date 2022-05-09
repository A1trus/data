"""
Retreives the data and exposes it as 'raw_data'
"""

import pandas as pd
import numpy as np
from .constants import RANDOM_SEED

# Generate sample data until we get the real data
def generate_sample_data() -> pd.DataFrame:
    np.random.seed(RANDOM_SEED)
    data = pd.DataFrame(np.random.normal(size=(10000, 20)), columns=[f'Column {i + 1}' for i in range(20)])
    data['Category'] = np.random.choice(['category a', 'category b', 'category c'], size=10000, replace=True)
    return data

raw_data = generate_sample_data()
