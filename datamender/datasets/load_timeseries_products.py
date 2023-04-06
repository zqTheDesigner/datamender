import pandas as pd

def load_timeseries_products():
    """Load the timeseries products dataset.

    Returns
    -------
    df : pandas.DataFrame
        The timeseries products dataset.
    """
    return pd.read_csv(
        os.path.join(os.path.dirname(__file__), 'data/timeseries_products.csv'),
        parse_dates=['date'],
        index_col=['date'],
    )