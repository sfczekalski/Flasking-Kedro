import numpy as np
import pandas as pd

from flasking_kedro.pipelines.feature_engineering.nodes import split_X_y


def test_split_X_y(test_data: pd.DataFrame) -> None:
    X, y = split_X_y(df=test_data, target="y")
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert X.shape == (4, 2)
    assert y.shape == (4,)
