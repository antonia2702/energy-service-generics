"""
Due to short deadlines it was not possible to implement dedicated unit
tests for most of the endpoints provided in `esg.api_client.emp`

Copyright 2024 FZI Research Center for Information Technology

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

SPDX-FileCopyrightText: 2024 FZI Research Center for Information Technology
SPDX-License-Identifier: Apache-2.0
"""

from datetime import timedelta

import pytest

from esg.clients.emp import EmpClient
from esg.clients.emp import ServiceList
from esg.clients.emp import RequestTaskList
from esg.clients.emp import PlantList
from esg.models.datapoint import DatapointList
from esg.models.datapoint import PutSummary
from esg.models.datapoint import ValueDataFrame
from esg.models.datapoint import ValueMessageByDatapointId
from esg.models.datapoint import ValueMessageListByDatapointId
from esg.models.metadata import Service
from esg.test import data as td
from generic import GenericCheckConnectionTests
from generic import GenericGetTests
from generic import GenericPutTests


class TestEmpClientCheckConnection(GenericCheckConnectionTests):
    """
    Tests for `EmpClient.check_connection`
    """

    client_class = EmpClient
    base_path = "/emp/api/"


class TestEmpClientGetDatapointMetadataLatest(GenericGetTests):
    """
    Tests for `EmpClient.get_datapoint_metadata_latest`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/datapoint/metadata/latest/"
    tested_client_method = "get_datapoint_metadata_latest"
    get_data_jsonable = [d["JSONable"] for d in td.datapoints]
    get_data_pydantic = DatapointList([d["Python"] for d in td.datapoints])
    all_test_kwargs = [{"query_params": {"test123": "456"}}]
    all_expected_query_params = [{"test123": "456"}]


class TestEmpClientPutDatapointMetadataLatest(GenericPutTests):
    """
    Tests for `EmpClient.put_datapoint_metadata_latest`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/datapoint/metadata/latest/"
    tested_client_method = "put_datapoint_metadata_latest"
    put_data_pydantic = DatapointList([d["Python"] for d in td.datapoints])
    put_data_jsonable = [d["JSONable"] for d in td.datapoints]
    response_data_pydantic = DatapointList([d["Python"] for d in td.datapoints])
    response_data_jsonable = [d["JSONable"] for d in td.datapoints]


class TestEmpClientGetDatapointValueLatest(GenericGetTests):
    """
    Tests for `EmpClient.get_datapoint_value_latest`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/datapoint/value/latest/"
    tested_client_method = "get_datapoint_value_latest"
    get_data_jsonable = {
        str(i): d["JSONable"] for i, d in enumerate(td.value_messages)
    }
    get_data_pydantic = ValueMessageByDatapointId(
        {str(i): d["Python"] for i, d in enumerate(td.value_messages)}
    )
    all_test_kwargs = [{"query_params": {"test123": "456"}}]
    all_expected_query_params = [{"test123": "456"}]


class TestEmpClientPutDatapointValueLatest(GenericPutTests):
    """
    Tests for `EmpClient.put_datapoint_value_latest`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/datapoint/value/latest/"
    tested_client_method = "put_datapoint_value_latest"
    put_data_pydantic = ValueMessageByDatapointId(
        {str(i): d["Python"] for i, d in enumerate(td.value_messages)}
    )
    put_data_jsonable = {
        str(i): d["JSONable"] for i, d in enumerate(td.value_messages)
    }
    response_data_jsonable = td.put_summaries[0]["JSONable"]
    response_data_pydantic = PutSummary(**td.put_summaries[0]["Python"])


class TestEmpClientGetDatapointValueHistory(GenericGetTests):
    """
    Tests for `EmpClient.get_datapoint_value_history`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/datapoint/value/history/"
    tested_client_method = "get_datapoint_value_history"
    get_data_jsonable = {
        "23": [v["JSONable"] for v in td.value_messages],
        "42": [v["JSONable"] for v in td.value_messages],
    }
    get_data_pydantic = ValueMessageListByDatapointId(
        {
            "23": [v["Python"] for v in td.value_messages],
            "42": [v["Python"] for v in td.value_messages],
        }
    )
    all_test_kwargs = [{"query_params": {"test123": "456"}}]
    all_expected_query_params = [{"test123": "456"}]


class TestEmpClientPutDatapointValueHistory(GenericPutTests):
    """
    Tests for `EmpClient.put_datapoint_value_history`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/datapoint/value/history/"
    tested_client_method = "put_datapoint_value_history"
    put_data_pydantic = ValueMessageListByDatapointId(
        {
            "23": [v["Python"] for v in td.value_messages],
            "42": [v["Python"] for v in td.value_messages],
        }
    )
    put_data_jsonable = {
        "23": [v["JSONable"] for v in td.value_messages],
        "42": [v["JSONable"] for v in td.value_messages],
    }
    response_data_jsonable = td.put_summaries[0]["JSONable"]
    response_data_pydantic = PutSummary(**td.put_summaries[0]["Python"])


class TestEmpClientGetDatapointValueHistoryAtInterval(GenericGetTests):
    """
    Tests for `EmpClient.get_datapoint_value_history_at_interval`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/datapoint/value/history/at_interval/"
    tested_client_method = "get_datapoint_value_history_at_interval"
    get_data_jsonable = {
        "values": {
            "23": [v["JSONable"]["value"] for v in td.value_messages],
            "42": [v["JSONable"]["value"] for v in td.value_messages],
        },
        "times": [v["JSONable"]["time"] for v in td.value_messages],
    }
    get_data_pydantic = ValueDataFrame(
        **{
            "values": {
                "23": [v["Python"]["value"] for v in td.value_messages],
                "42": [v["Python"]["value"] for v in td.value_messages],
            },
            "times": [v["Python"]["time"] for v in td.value_messages],
        }
    )
    # Account for `interval`, a required argument.
    all_test_kwargs = [
        {"interval": timedelta(minutes=15)},
        {"interval": timedelta(minutes=15), "query_params": {"ts": "456"}},
    ]
    all_expected_query_params = [
        {"interval": "0 days 900 seconds"},
        {"interval": "0 days 900 seconds", "ts": "456"},
    ]


class TestEmpClientGetServiceLatest(GenericGetTests):
    """
    Tests for `EmpClient.get_service_latest`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/service/latest/"
    tested_client_method = "get_service_latest"
    get_data_jsonable = [p["JSONable"] for p in td.services]
    get_data_pydantic = ServiceList([p["Python"] for p in td.services])
    all_test_kwargs = [{"query_params": {"test123": "456"}}]
    all_expected_query_params = [{"test123": "456"}]


class TestGetServiceByName:
    """
    Tests for `EmpClient.get_service_by_name`
    """

    def test_single_service_returned(self, httpserver):
        """
        Check that the regex query string is forwarded and that a response
        containing a single service is returned.
        """
        expected_request = httpserver.expect_oneshot_request(
            "/emp/api/service/latest/",
            query_string={"name__regex": "^test124$"},
        )
        expected_request.respond_with_json([td.services[0]["JSONable"]])

        client = EmpClient(
            base_url=httpserver.url_for("/emp/api/"),
            check_on_init=False,
        )
        actual_return = client.get_service_by_name(name="test124")

        expected_return = Service(**td.services[0]["Python"])

        assert actual_return == expected_return
        httpserver.check_assertions()

    def test_empty_response_raises(self, httpserver):
        """
        The method is expected to raise a `ValueError` if no service
        is matched.
        """
        expected_request = httpserver.expect_oneshot_request(
            "/emp/api/service/latest/",
            query_string={"name__regex": "^test124$"},
        )
        expected_request.respond_with_json([])

        client = EmpClient(
            base_url=httpserver.url_for("/emp/api/"),
            check_on_init=False,
        )

        with pytest.raises(ValueError):
            _ = client.get_service_by_name(name="test124")


class TestEmpClientPutServiceLatest(GenericPutTests):
    """
    Tests for `EmpClient.put_service_latest`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/service/latest/"
    tested_client_method = "put_service_latest"
    put_data_pydantic = ServiceList([p["Python"] for p in td.services])
    put_data_jsonable = [p["JSONable"] for p in td.services]
    response_data_jsonable = [p["JSONable"] for p in td.services]
    response_data_pydantic = ServiceList([p["Python"] for p in td.services])


class TestEmpClientGetRequestTaskLatest(GenericGetTests):
    """
    Tests for `EmpClient.get_request_task_latest`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/request_task/latest/"
    tested_client_method = "get_request_task_latest"
    get_data_jsonable = [p["JSONable"] for p in td.request_tasks]
    get_data_pydantic = RequestTaskList([p["Python"] for p in td.request_tasks])
    all_test_kwargs = [{"query_params": {"test123": "456"}}]
    all_expected_query_params = [{"test123": "456"}]


class TestEmpClientPutRequestTaskLatest(GenericPutTests):
    """
    Tests for `EmpClient.put_request_task_latest`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/request_task/latest/"
    tested_client_method = "put_request_task_latest"
    put_data_pydantic = RequestTaskList([p["Python"] for p in td.request_tasks])
    put_data_jsonable = [p["JSONable"] for p in td.request_tasks]
    response_data_jsonable = [p["JSONable"] for p in td.request_tasks]
    response_data_pydantic = RequestTaskList(
        [p["Python"] for p in td.request_tasks]
    )


class TestEmpClientGetPlantLatest(GenericGetTests):
    """
    Tests for `EmpClient.get_plant_latest`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/plant/latest/"
    tested_client_method = "get_plant_latest"
    get_data_jsonable = [p["JSONable"] for p in td.plants]
    get_data_pydantic = PlantList([p["Python"] for p in td.plants])
    all_test_kwargs = [{"query_params": {"test123": "456"}}]
    all_expected_query_params = [{"test123": "456"}]


class TestEmpClientPutPlantLatest(GenericPutTests):
    """
    Tests for `EmpClient.put_plant_latest`
    """

    client_class = EmpClient
    base_path = "/emp/api/"
    endpoint_path = "/emp/api/plant/latest/"
    tested_client_method = "put_plant_latest"
    put_data_pydantic = PlantList([p["Python"] for p in td.plants])
    put_data_jsonable = [p["JSONable"] for p in td.plants]
    response_data_jsonable = [p["JSONable"] for p in td.plants]
    response_data_pydantic = PlantList([p["Python"] for p in td.plants])
