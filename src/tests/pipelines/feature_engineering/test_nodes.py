import numpy as np
import pandas as pd

from flasking_kedro.pipelines.feature_engineering.nodes import split_X_y


def test_split_X_y(sample_data: pd.DataFrame) -> None:
    X, y = split_X_y(df=sample_data, target="species")
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert X.shape == (4, 4)
    assert y.shape == (4,)


def test_split_train_test(sample_data: pd.DataFrame) -> None:
    pass
