import pandas as pd
import os


def load_data():
    """Load the timeseries products dataset.

    Returns
    -------
    df : pandas.DataFrame
        The timeseries products dataset.
    """
    return pd.read_csv(
        './data/timeseries_products.csv',
    )
