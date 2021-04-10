import pandas as pd
import pytest


@pytest.fixture
def test_data() -> pd.DataFrame:
    """Return some data for testing purposes.

    Returns:
        pd.DataFrame: Test dataset.
    """
    return pd.DataFrame.from_dict(
        {
            "x1": [0.1, 1.2, 3.4, -0.5],
            "x2": [7.1, 2.8, 0.1, 2.2],
            "y": ["first_class", "first_class", "second_class", "second_class"],
        }
    )
