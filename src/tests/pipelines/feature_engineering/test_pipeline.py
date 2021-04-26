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
This is a boilerplate test file for pipeline 'feature_engineering'
generated using Kedro 0.17.2.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""
from kedro.io import DataCatalog
from kedro.runner import SequentialRunner

from flasking_kedro.pipelines.feature_engineering import create_pipeline


def test_feature_engineering_pipeline(
    sample_data_catalog_train: DataCatalog, runner: SequentialRunner
):
    train_pipeline = create_pipeline(
        output_X_train_normalized="sample_iris_X_train_normalized",
        output_X_test_normalized="sample_iris_X_test_normalized",
        output_y_train="sample_iris_y_train",
        output_y_test="sample_iris_y_test",
        normalizer="sample_normalizer",
    )

    output = runner.run(pipeline=train_pipeline, catalog=sample_data_catalog_train)

    assert output["sample_iris_X_train_normalized"].shape == (3, 4)
    assert output["sample_iris_X_test_normalized"].shape == (1, 4)
    assert output["sample_iris_y_train"].shape == (3,)
    assert output["sample_iris_y_test"].shape == (1,)

    # predict_pipeline = pipeline(
    #     create_pipeline(
    #         output_X_test_normalized="sample_iris_X_test_normalized",
    #         normalizer="sample_normalizer",
    #     ).only_nodes_with_tags("prediction"),
    #     inputs={
    #         "sample_iris_X_test_normalized": "sample_iris_X_test_normalized",
    #         "sample_normalizer": "sample_normalizer",
    #     },
    #     namespace="predict",
    # )
