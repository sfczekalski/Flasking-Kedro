# Copyright 2021 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.17.2
"""
import logging
from typing import Tuple, Union

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer

logger = logging.getLogger(__name__)


def split_X_y(df: pd.DataFrame, target: str) -> Tuple[np.ndarray, np.ndarray]:
    """Split dataset into features and target.

    Args:
        df (pd.DataFrame): The dataset.
        target (str): Name of the target column.

    Returns:
        Tuple[np.ndarray, np.ndarray]: (dataset features, dataset targets) tuple.
    """
    y = df.pop(target).to_numpy()
    X = df.to_numpy()

    logger.info(f"Splitted dataset into features and {target} target.")
    return X, y


def split_train_test(
    X: np.ndarray, y: np.ndarray, test_fraction: float, seed: int
) -> Union[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Split dataset into train and test samples.

    Args:
        X (np.ndarray): Dataset features.
        y (np.ndarray): Dataset targets.
        test_fraction (float): Fraction of examples in the test set.
        seed (int): Random seed.

    Returns:
        Union[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
            (train features, test features, train targets, test targets).
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_fraction, random_state=seed
    )

    logger.info(
        f"Splitted dataset of size {X.shape[0]} examples into \
            {X_train.shape[0]} training examples and {X_test.shape[0]} testing examples"
    )
    return X_train, X_test, y_train, y_test


def fit_normalizer(X: np.ndarray) -> Normalizer:
    """Fit normalizer on training set.

    Args:
        X (np.ndarray): Training set.

    Returns:
        Normalizer: Fitter normalizer.
    """
    return Normalizer().fit(X)


def normalize(X: np.ndarray, normalizer: Normalizer) -> np.ndarray:
    """Normalize given dataset.

    Args:
        X (np.ndarray): Dataset to normalize.
        normalizer (Normalizer): Fitted normalizer.

    Returns:
        np.ndarray: Normalized dataset.
    """
    return normalizer.transform(X)
