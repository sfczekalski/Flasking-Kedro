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

from kedro.pipeline import Pipeline, node

from flasking_kedro.pipelines.feature_engineering.nodes import (
    fit_normalizer,
    normalize,
    split_train_test,
    split_X_y,
)


def create_pipeline(
    input_dataset: str = "iris",
    output_X_train_normalized: str = "iris_X_train_normalized",
    output_X_test_normalized: str = "iris_X_test_normalized",
    output_X_train: str = "iris_X_train",
    output_X_test: str = "iris_X_test",
    output_y_train: str = "iris_y_train",
    output_y_test: str = "iris_y_test",
    normalizer: str = "normalizer",
    **kwargs
) -> Pipeline:
    """Create feature engineering pipeline for training and prediction.

    Args:
        # TODO

    Returns:
        Pipeline: Feature engineering pipeline object.
    """
    return Pipeline(
        [
            node(
                func=split_X_y,
                inputs=["iris", "params:target"],
                outputs=["iris_X", "iris_y"],
                tags=["training"],
            ),
            node(
                func=split_train_test,
                inputs=["iris_X", "iris_y", "params:test_fraction", "params:seed"],
                outputs=[output_X_train, output_X_test, output_y_train, output_y_test],
                tags=["training"],
            ),
            node(
                func=fit_normalizer,
                inputs=output_X_train,
                outputs=normalizer,
                tags=["training"],
            ),
            node(
                func=normalize,
                inputs=[output_X_train, normalizer],
                outputs=output_X_train_normalized,
                tags=["training"],
            ),
            node(
                func=normalize,
                inputs=[output_X_test, normalizer],
                outputs=output_X_test_normalized,
                tags=["training", "prediction"],
            ),
        ]
    )
