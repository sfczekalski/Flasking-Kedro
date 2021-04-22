import pandas as pd
import pytest
from kedro.io import DataCatalog, MemoryDataSet
from kedro.runner import SequentialRunner


@pytest.fixture
def sample_data() -> pd.DataFrame:
    """Return some data for tests.

    Returns:
        pd.DataFrame: Sample dataset.
    """
    return pd.DataFrame.from_dict(
        {
            "sepal_length": [0.1, 1.2, 3.4, -0.5],
            "sepal_width": [7.1, 2.8, 0.1, 2.2],
            "petal_length": [0.1, 1.2, 3.4, -0.5],
            "petal_width": [7.1, 2.8, 0.1, 2.2],
            "species": ["setosa", "setosa", "versicolor", "virginica"],
        }
    )


@pytest.fixture
def sample_data_catalog_train(sample_data: pd.DataFrame) -> DataCatalog:
    """Generate data catalog for end to end feature engineering pipeline test.

    Args:
        sample_data (pd.DataFrame): Some sample training data.

    Returns:
        DataCatalog: Data catalog with sample training data.
    """
    catalog = DataCatalog()

    catalog.add("iris", MemoryDataSet(data=sample_data))
    catalog.add("params:target", MemoryDataSet(data="species"))
    catalog.add("params:test_fraction", MemoryDataSet(data=0.25))
    catalog.add("params:seed", MemoryDataSet(data=42))

    return catalog


@pytest.fixture
def runner() -> SequentialRunner:
    """Return sample piepline runner for tests.

    Returns:
        SequentialRunner: Sample pipeline runner.
    """
    return SequentialRunner()
