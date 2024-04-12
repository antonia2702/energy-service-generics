"""
Collection of data that can be used for testing parts of this package.

Data is only contained if it can be expected to be useful beyond testing
the corresponding models. Any testdata that just required for testing
the a model should reside in the test file belonging to the model.

For each data type (i.e. often the message types) several representations of
the same object are provided (e.g. as python objects or JSON strings). This
allows writing tests that convert from one type to the other very rapidly.

Available Representations:
--------------------------
Python:
    The data items are in a format that would be normally be used by the
    Python programs.
    Note that Python representations are not provided for invalid messages
    as there should exist no such representation by definition.
JSONable:
    A representation of that item in JSON, but after loaded with json.loads.
    This is due to the fact that comparing JSON strings would cause unintended
    errors, for e.g. the ordering of dicts or differences in whitespace.
BEMCom:
    As JSONable above, but a representation following the BEMCom message format
    of the messages. This is only relevant for models defined in
    `esg.models.datapoint` as these all messages exchanged with BEMCom are
    defined there.

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

from datetime import datetime, timezone, timedelta

"""
Templates for copy paste:

valid = [
    {
        "Python": {},
        "JSONable": {},
        "BEMCom": {},
    },
]

invalid = [
    {
        "JSONable": {},
    },
]

"""


###############################################################################
#
# Models defined in `esg.models.datapoint`
#
###############################################################################

# Note, we don't define BEMCom representations here as this representation is
# not different apart from that `origin` and `origin_id` are not defined.
# However, these need to be matched and cannot be simply translated.
datapoints = [
    # The minimum amount of information forming a valid datapoint.
    {
        # fmt: off
        "Python": {
            "type": "Sensor",
        },
        # fmt: on
        "JSONable": {
            "id": None,
            "origin": None,
            "origin_id": None,
            "short_name": None,
            "type": "Sensor",
            "data_format": "Unknown",
            "description": "",
            "allowed_values": None,
            "min_value": None,
            "max_value": None,
            "unit": "",
        },
    },
    # Fields populated with non-default values.
    {
        # fmt: off
        "Python": {
            "id": 1337,
            "origin": "HoLL BEMCom Instance",
            "origin_id": "42",
            "short_name": "T_zone_f",
            "type": "Actuator",
            "data_format": "Continuous Numeric",
            "description": "Setpoint temperature first floor.",
            "allowed_values": None,
            "min_value": 13.37,
            "max_value": 42.0,
            "unit": "°C",
        },
        # fmt: on
        "JSONable": {
            "id": 1337,
            "origin": "HoLL BEMCom Instance",
            "origin_id": "42",
            "short_name": "T_zone_f",
            "type": "Actuator",
            "data_format": "Continuous Numeric",
            "description": "Setpoint temperature first floor.",
            "allowed_values": None,
            "min_value": 13.37,
            "max_value": 42.0,
            "unit": "°C",
        },
    },
    # Allowed values set with JSON encoded floats..
    {
        # fmt: off
        "Python": {
            "type": "Sensor",
            "data_format": "Discrete Numeric",
            "allowed_values": [21.0, 21.5, 22.0],
        },
        # fmt: on
        "JSONable": {
            "id": None,
            "origin": None,
            "origin_id": None,
            "short_name": None,
            "type": "Sensor",
            "data_format": "Discrete Numeric",
            "description": "",
            "allowed_values": [21.0, 21.5, 22.0],
            "min_value": None,
            "max_value": None,
            "unit": "",
        },
    },
]

invalid_datapoints = []

value_messages = [
    # A value message holding a float value. This float must be converted into
    # a string for JSON as OpenAPI cannot handle fields with dynamic types.
    {
        "Python": {
            "value": 21.0,
            "time": datetime(2022, 2, 22, 2, 52, tzinfo=timezone.utc),
        },
        # fmt: off
        "JSONable": {
            "value": 21.0,
            "time": "2022-02-22T02:52:00Z",
        },
        "BEMCom": {
            "value": "21.0",
            "timestamp": 1645498320000,
        },
        # fmt: on
    },
    # Nones should be communicated too I guess.
    {
        "Python": {
            "value": None,
            "time": datetime(2022, 2, 22, 2, 56, tzinfo=timezone.utc),
        },
        # fmt: off
        "JSONable": {
            "value": None,
            "time": "2022-02-22T02:56:00Z",
        },
        "BEMCom": {
            "value": "null",
            "timestamp": 1645498560000,
        },
        # fmt: on
    },
]

invalid_value_messages = [
    # fmt: off
    # Value message must contain a value.
    {
        "JSONable": {
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # Value message must contain a time.
    {
        "JSONable": {
            "value": 21.0,
        },
    },
    # Value message can't be empty
    {
        "JSONable": {},
    },
    # Time can't be None.
    {
        "JSONable": {
            "value": 21.0,
            "time": None,
        },
    },
    # Time must be parsable to datetime
    {
        "JSONable": {
            "value": 21.0,
            "time": "Not related to time.",
        },
    },
    # fmt: on
]

value_message_by_datapoint_ids = [
    # Contains all valid value message with an arbitrary ID.
    {
        "Python": {str(i): m["Python"] for i, m in enumerate(value_messages)},
        "JSONable": {
            str(i): m["JSONable"] for i, m in enumerate(value_messages)
        },
        "BEMCom": {str(i): m["BEMCom"] for i, m in enumerate(value_messages)},
    },
]

invalid_value_message_by_datapoint_ids = []
# Every invalid value message can't be part of valid message here.
for invalid_value_msg in invalid_value_messages:
    invalid_value_message_by_datapoint_ids.append(
        {"JSONable": {"1": invalid_value_msg}}
    )
invalid_value_message_by_datapoint_ids += [
    # Valid values/times but not a dict.
    {
        "JSONable": [m["JSONable"] for m in value_messages],
    },
]

value_message_lists = [
    # A list of all valid messages defined above.
    {
        "Python": [m["Python"] for m in value_messages],
        "JSONable": [m["JSONable"] for m in value_messages],
        "BEMCom": [m["BEMCom"] for m in value_messages],
    },
]

invalid_value_message_lists = []
# A list of valid messages and a single invalid one can't be valid.
for invalid_value_msg in invalid_value_messages:
    valid_msg_list = [m["JSONable"] for m in value_messages]
    invalid_value_message_lists.append(
        {"JSONable": valid_msg_list + [invalid_value_msg]}
    )
# Extend here if needed.
invalid_value_message_lists += []

value_message_list_by_datapoint_ids = [
    # Every valid item in `value_message_list` should correspond
    # to valid instance here too.
    {
        "Python": {
            str(i): m["Python"] for i, m in enumerate(value_message_lists)
        },
        "JSONable": {
            str(i): m["JSONable"] for i, m in enumerate(value_message_lists)
        },
        "BEMCom": {
            str(i): m["BEMCom"] for i, m in enumerate(value_message_lists)
        },
    },
    # Extended example with more then one series.
    {
        "Python": {
            "42": [
                {
                    "value": 33.5,
                    "time": datetime(2022, 2, 22, 2, 52, tzinfo=timezone.utc),
                },
                {
                    "value": None,
                    "time": datetime(2022, 2, 22, 2, 53, tzinfo=timezone.utc),
                },
                {
                    "value": 32.8,
                    "time": datetime(2022, 2, 22, 2, 54, tzinfo=timezone.utc),
                },
            ],
            "1337": [
                {
                    "value": 7881.12,
                    "time": datetime(
                        2022, 2, 22, 2, 52, 14, tzinfo=timezone.utc
                    ),
                },
                {
                    "value": 231203,
                    "time": datetime(
                        2022, 2, 22, 2, 53, 15, tzinfo=timezone.utc
                    ),
                },
                {
                    "value": None,
                    "time": datetime(
                        2022, 2, 22, 2, 54, 15, tzinfo=timezone.utc
                    ),
                },
            ],
        },
        "JSONable": {
            "42": [
                {
                    "value": 33.5,
                    "time": "2022-02-22T02:52:00Z",
                },
                {
                    "value": None,
                    "time": "2022-02-22T02:53:00Z",
                },
                {
                    "value": 32.8,
                    "time": "2022-02-22T02:54:00Z",
                },
            ],
            "1337": [
                {
                    "value": 7881.12,
                    "time": "2022-02-22T02:52:14Z",
                },
                {
                    "value": 231203,
                    "time": "2022-02-22T02:53:15Z",
                },
                {
                    "value": None,
                    "time": "2022-02-22T02:54:15Z",
                },
            ],
        },
        "BEMCom": {
            "42": [
                {
                    "value": "33.5",
                    "timestamp": 1645498320000,
                },
                {
                    "value": "null",
                    "timestamp": 1645498380000,
                },
                {
                    "value": "32.8",
                    "timestamp": 1645498440000,
                },
            ],
            "1337": [
                {
                    "value": "7881.12",
                    "timestamp": 1645498334000,
                },
                {
                    "value": "231203.0",
                    "timestamp": 1645498395000,
                },
                {
                    "value": "null",
                    "timestamp": 1645498455000,
                },
            ],
        },
    },
]

invalid_value_message_list_by_datapoint_ids = []
# Every invalid value message list should be invalid here too.
for invalid_value_msg_list in invalid_value_message_lists:
    invalid_value_message_list_by_datapoint_ids.append(
        {"JSONable": {"1": invalid_value_msg_list["JSONable"]}}
    )
invalid_value_message_list_by_datapoint_ids += [
    # Valid value lists but not a dict.
    {
        "JSONable": [m["JSONable"] for m in value_message_lists],
    },
]

value_data_frames = []
for value_message_list in value_message_lists:
    # Every valid item in `value_message_list` should correspond
    # to valid instance here too.
    value_data_frames.append(
        {
            "Python": {
                "values": {
                    "42": [m["value"] for m in value_message_list["Python"]]
                },
                "times": [m["time"] for m in value_message_list["Python"]],
            },
            "JSONable": {
                "values": {
                    "42": [m["value"] for m in value_message_list["JSONable"]]
                },
                "times": [m["time"] for m in value_message_list["JSONable"]],
            },
        },
    )
value_data_frames += [
    # Extended example, more then one series.
    {
        "Python": {
            "values": {
                "42": [31.1, 32.2, 33.3],
                "not a number": [131.1, None, 233.3],
            },
            "times": [
                datetime(2022, 2, 22, 2, 52, 14, tzinfo=timezone.utc),
                datetime(2022, 2, 22, 2, 53, 15, tzinfo=timezone.utc),
                datetime(2022, 2, 22, 2, 54, 15, tzinfo=timezone.utc),
            ],
        },
        "JSONable": {
            "values": {
                "42": [31.1, 32.2, 33.3],
                "not a number": [131.1, None, 233.3],
            },
            "times": [
                "2022-02-22T02:52:14Z",
                "2022-02-22T02:53:15Z",
                "2022-02-22T02:54:15Z",
            ],
        },
    },
]

invalid_value_data_frames = [
    # Note that we ignore the first three invalid messages as those have
    # missing entries for `time` and/or `value`
    # TODO: Replace this with one DF per invalid value message to make
    # sure that every invalid value is caught.
    {
        "JSONable": {
            "values": {
                "1": [
                    m["JSONable"]["value"] for m in invalid_value_messages[3:]
                ],
                "2": [
                    m["JSONable"]["value"] for m in invalid_value_messages[3:]
                ],
            },
            "times": [
                m["JSONable"]["time"] for m in invalid_value_messages[3:]
            ],
        },
    },
    # This is invalid as the size of the index and the columns mismatch.
    {
        "JSONable": {
            "values": {
                "1": [m["JSONable"]["value"] for m in value_messages],
                "2": [m["JSONable"]["value"] for m in value_messages],
            },
            "times": [m["JSONable"]["time"] for m in value_messages[1:]],
        },
    },
    # This is invalid as the size of the columns mismatch.
    {
        "JSONable": {
            "values": {
                "1": [m["JSONable"]["value"] for m in value_messages],
                "2": [m["JSONable"]["value"] for m in value_messages[1:]],
            },
            "times": [m["JSONable"]["time"] for m in value_messages],
        },
    },
]

schedule_messages = [
    # A minimal valid schedule message holding an empty schedule.
    {
        "Python": {
            "schedule": [],
            "time": datetime(2022, 2, 22, 2, 52, tzinfo=timezone.utc),
        },
        # fmt: off
        "JSONable": {
            "schedule": [],
            "time": "2022-02-22T02:52:00Z",
        },
        "BEMCom": {
            "schedule": [],
            "timestamp": 1645498320000,
        },
        # fmt: on
    },
    # A schedule with one schedule item.
    {
        "Python": {
            "schedule": [
                {
                    "from_timestamp": datetime(
                        2022, 2, 22, 3, 0, tzinfo=timezone.utc
                    ),
                    "to_timestamp": datetime(
                        2022, 2, 22, 3, 15, tzinfo=timezone.utc
                    ),
                    "value": 21.0,
                },
            ],
            "time": datetime(2022, 2, 22, 2, 52, tzinfo=timezone.utc),
        },
        "JSONable": {
            "schedule": [
                {
                    "from_timestamp": "2022-02-22T03:00:00Z",
                    "to_timestamp": "2022-02-22T03:15:00Z",
                    "value": 21.0,
                },
            ],
            "time": "2022-02-22T02:52:00Z",
        },
        "BEMCom": {
            "schedule": [
                {
                    "from_timestamp": 1645498800000,
                    "to_timestamp": 1645499700000,
                    "value": "21.0",
                },
            ],
            "timestamp": 1645498320000,
        },
    },
    # A schedule with multiple item, bool like floats as values and Nones
    # for `from_timestamp` and `to_timestamp`.
    {
        "Python": {
            "schedule": [
                {
                    "from_timestamp": None,
                    "to_timestamp": datetime(
                        2022, 2, 22, 3, 0, tzinfo=timezone.utc
                    ),
                    "value": None,
                },
                {
                    "from_timestamp": datetime(
                        2022, 2, 22, 3, 0, tzinfo=timezone.utc
                    ),
                    "to_timestamp": None,
                    "value": 0.0,
                },
            ],
            "time": datetime(2022, 2, 22, 2, 52, tzinfo=timezone.utc),
        },
        "JSONable": {
            "schedule": [
                {
                    "from_timestamp": None,
                    "to_timestamp": "2022-02-22T03:00:00Z",
                    "value": None,
                },
                {
                    "from_timestamp": "2022-02-22T03:00:00Z",
                    "to_timestamp": None,
                    "value": 0.0,
                },
            ],
            "time": "2022-02-22T02:52:00Z",
        },
        "BEMCom": {
            "schedule": [
                {
                    "from_timestamp": None,
                    "to_timestamp": 1645498800000,
                    "value": "null",
                },
                {
                    "from_timestamp": 1645498800000,
                    "to_timestamp": None,
                    "value": "0.0",
                },
            ],
            "timestamp": 1645498320000,
        },
    },
]

invalid_schedule_messages = [
    # fmt: off
    # Schedule message must contain `schedule`.
    {
        "JSONable": {
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # Schedule message must contain `time`.
    {
        "JSONable": {
            "schedule": [],
        },
    },
    # `schedule` cannot be None.
    {
        "JSONable": {
            "schedule": None,
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # fmt: on
    # Schedule item must contain `from_timestamp`.
    {
        "JSONable": {
            "schedule": [
                # fmt: off
                {
                    "to_timestamp": "2022-02-22T03:15:00Z",
                    "value": 21.0,
                },
                # fmt: on
            ],
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # Schedule item must contain `to_timestamp`.
    {
        "JSONable": {
            "schedule": [
                # fmt: off
                {
                    "from_timestamp": "2022-02-22T03:00:00Z",
                    "value": 21.0,
                },
                # fmt: on
            ],
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # Schedule item must contain `value`.
    {
        "JSONable": {
            "schedule": [
                # fmt: off
                {
                    "from_timestamp": "2022-02-22T03:00:00Z",
                    "to_timestamp": "2022-02-22T03:15:00Z",
                },
                # fmt: on
            ],
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # Schedule item values can't be strings.
    {
        "JSONable": {
            "schedule": [
                # fmt: off
                {
                    "from_timestamp": "2022-02-22T03:00:00Z",
                    "to_timestamp": "2022-02-22T03:15:00Z",
                    "value": "a string",
                },
                # fmt: on
            ],
            "time": "2022-02-22T02:52:00Z",
        },
    },
]

setpoint_messages = [
    # A minimal valid setpoint message holding an empty setpoint definition.
    {
        "Python": {
            "setpoint": [],
            "time": datetime(2022, 2, 22, 2, 52, tzinfo=timezone.utc),
        },
        # fmt: off
        "JSONable": {
            "setpoint": [],
            "time": "2022-02-22T02:52:00Z",
        },
        "BEMCom": {
            "setpoint": [],
            "timestamp": 1645498320000,
        },
        # fmt: on
    },
    # A setpoint with one setpoint item and `min_values` and `max_value` set.
    {
        "Python": {
            "setpoint": [
                {
                    "from_timestamp": datetime(
                        2022, 2, 22, 3, 0, tzinfo=timezone.utc
                    ),
                    "to_timestamp": datetime(
                        2022, 2, 22, 3, 15, tzinfo=timezone.utc
                    ),
                    "preferred_value": 21.0,
                    "min_value": 17.4,
                    "max_value": 23.2,
                },
            ],
            "time": datetime(2022, 2, 22, 2, 52, tzinfo=timezone.utc),
        },
        "JSONable": {
            "setpoint": [
                {
                    "from_timestamp": "2022-02-22T03:00:00Z",
                    "to_timestamp": "2022-02-22T03:15:00Z",
                    "preferred_value": 21.0,
                    "acceptable_values": None,
                    "min_value": 17.4,
                    "max_value": 23.2,
                },
            ],
            "time": "2022-02-22T02:52:00Z",
        },
        "BEMCom": {
            "setpoint": [
                {
                    "from_timestamp": 1645498800000,
                    "to_timestamp": 1645499700000,
                    "preferred_value": "21.0",
                    "acceptable_values": None,
                    "min_value": 17.4,
                    "max_value": 23.2,
                },
            ],
            "timestamp": 1645498320000,
        },
    },
    # A schedule with multiple items, a bool representation as values,
    # `acceptable_values` field used and Nones for `from_timestamp`
    # and `to_timestamp`.
    {
        "Python": {
            "setpoint": [
                {
                    "from_timestamp": None,
                    "to_timestamp": datetime(
                        2022, 2, 22, 3, 0, tzinfo=timezone.utc
                    ),
                    "preferred_value": None,
                },
                {
                    "from_timestamp": datetime(
                        2022, 2, 22, 3, 0, tzinfo=timezone.utc
                    ),
                    "to_timestamp": None,
                    "preferred_value": 0.0,
                    "acceptable_values": [0.0, 1.0],
                },
            ],
            "time": datetime(2022, 2, 22, 2, 52, tzinfo=timezone.utc),
        },
        "JSONable": {
            "setpoint": [
                {
                    "from_timestamp": None,
                    "to_timestamp": "2022-02-22T03:00:00Z",
                    "preferred_value": None,
                    "acceptable_values": None,
                    "min_value": None,
                    "max_value": None,
                },
                {
                    "from_timestamp": "2022-02-22T03:00:00Z",
                    "to_timestamp": None,
                    "preferred_value": 0.0,
                    "acceptable_values": [0.0, 1.0],
                    "min_value": None,
                    "max_value": None,
                },
            ],
            "time": "2022-02-22T02:52:00Z",
        },
        "BEMCom": {
            "setpoint": [
                {
                    "from_timestamp": None,
                    "to_timestamp": 1645498800000,
                    "preferred_value": "null",
                    "acceptable_values": None,
                    "min_value": None,
                    "max_value": None,
                },
                {
                    "from_timestamp": 1645498800000,
                    "to_timestamp": None,
                    "preferred_value": "0.0",
                    "acceptable_values": ["0.0", "1.0"],
                    "min_value": None,
                    "max_value": None,
                },
            ],
            "timestamp": 1645498320000,
        },
    },
]

invalid_setpoint_messages = [
    # fmt: off
    # Setpoint message must contain `setpoint`.
    {
        "JSONable": {
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # Setpoint message must contain `time`.
    {
        "JSONable": {
            "setpoint": [],
        },
    },
    # `setpoint` cannot be None.
    {
        "JSONable": {
            "setpoint": None,
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # fmt: on
    # Schedule item must contain `from_timestamp`.
    {
        "JSONable": {
            "setpoint": [
                # fmt: off
                {
                    "to_timestamp": "2022-02-22T03:15:00Z",
                    "preferred_value": 21.0,
                },
                # fmt: on
            ],
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # Schedule item must contain `to_timestamp`.
    {
        "JSONable": {
            "setpoint": [
                # fmt: off
                {
                    "from_timestamp": "2022-02-22T03:00:00Z",
                    "preferred_value": 21.0,
                },
                # fmt: on
            ],
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # Schedule item must contain `preferred_value`.
    {
        "JSONable": {
            "setpoint": [
                # fmt: off
                {
                    "from_timestamp": "2022-02-22T03:00:00Z",
                    "to_timestamp": "2022-02-22T03:15:00Z",
                },
                # fmt: on
            ],
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # Schedule items with strings as values.
    {
        "JSONable": {
            "setpoint": [
                {
                    "from_timestamp": "2022-02-22T03:00:00+00:00",
                    "to_timestamp": "2022-02-22T03:15:00+00:00",
                    "preferred_value": "true",
                    "acceptable_values": ["true", "other string"],
                    "min_value": None,
                    "max_value": None,
                },
            ],
            "time": "2022-02-22T02:52:00Z",
        },
    },
]


forecast_messages = [
    # A minimum valid forecast message.
    {
        "Python": {
            "mean": 21.0,
            "time": datetime(2022, 2, 22, 2, 52, tzinfo=timezone.utc),
        },
        # As usual, we have to specify all optional fields here too, not
        # because they would be required to parse the model from JSON, but
        # just because they will be created when going from Python to JSON.
        "JSONable": {
            "mean": 21.0,
            "std": None,
            "p05": None,
            "p10": None,
            "p25": None,
            "p50": None,
            "p75": None,
            "p90": None,
            "p95": None,
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # A forecast message with `std` set.
    {
        "Python": {
            "mean": 21.0,
            "std": 0.71,
            "time": datetime(2022, 2, 22, 2, 53, tzinfo=timezone.utc),
        },
        "JSONable": {
            "mean": 21.0,
            "std": 0.71,
            "p05": None,
            "p10": None,
            "p25": None,
            "p50": None,
            "p75": None,
            "p90": None,
            "p95": None,
            "time": "2022-02-22T02:53:00Z",
        },
    },
    # A forecast message with percentiles set..
    {
        "Python": {
            "mean": 21.0,
            "p05": 19.35,
            "p10": 19.72,
            "p25": 20.33,
            "p50": 21.0,
            "p75": 21.67,
            "p90": 22.28,
            "p95": 22.65,
            "time": datetime(2022, 2, 22, 2, 54, tzinfo=timezone.utc),
        },
        "JSONable": {
            "mean": 21.0,
            "std": None,
            "p05": 19.35,
            "p10": 19.72,
            "p25": 20.33,
            "p50": 21.0,
            "p75": 21.67,
            "p90": 22.28,
            "p95": 22.65,
            "time": "2022-02-22T02:54:00Z",
        },
    },
]

invalid_forecast_messages = [
    # `mean` and `time` fields must always be provided, as those define
    # the bare minimum of a valid forecast.
    # fmt: off
    {
        "JSONable": {
            "time": "2022-02-22T02:52:00Z",
        },
    },
    {
        "JSONable": {
            "mean": 21.0,
        },
    },
    # `mean` cannot be set to `None`, we really want that forecasted value!
    {
        "JSONable": {
            "mean": None,
            "time": "2022-02-22T02:52:00Z",
        },
    },
    # Same fore `time`, there can't be a forecast at unknown time.
    {
        "JSONable": {
            "mean": 21.0,
            "time": None,
        },
    },
    # fmt: on
]

put_summaries = [
    # A valid message.
    {
        # fmt: off
        "Python": {
            "objects_created": 1,
            "objects_updated": 10,
        },
        "JSONable": {
            "objects_created": 1,
            "objects_updated": 10,
        },
        # fmt: on
    },
]

invalid_put_summaries = [
    # fmt: off
    # None as value not allowed.
    {
        "JSONable": {
            "objects_created": None,
            "objects_updated": 10,
        },
    },
    {
        "JSONable": {
            "objects_created": 0,
            "objects_updated": None,
        },
    },
    # Float or string as value not allowed.
    {
        "JSONable": {
            "objects_created": 1,
            "objects_updated": "Nope",
        },
    },
    {
        "JSONable": {
            "objects_created": "Hallo",
            "objects_updated": 10,
        },
    },
    # Both fields must be present.
    {
        "JSONable": {
            "objects_created": 1,
        },
    },
    {
        "JSONable": {
            "objects_updated": 10,
        },
    },
]
###############################################################################
#
# Models defined in `esg.models.metadata`
#
###############################################################################
geographic_positions = [
    # fmt: off
    # Position with height not specified.
    {
        "Python": {
            "latitude": 49.01365,
            "longitude": 8.40444,
            "height": None,
        },
        "JSONable": {
            "latitude": 49.01365,
            "longitude": 8.40444,
            "height": None,
        },
    },
    # Position with height specified.
    {
        "Python": {
            "latitude": 52.52094,
            "longitude": 13.40949,
            "height": 368.03,
        },
        "JSONable": {
            "latitude": 52.52094,
            "longitude": 13.40949,
            "height": 368.03,
        },
    },
    # Position with negative values for both lat and lon.
    {
        "Python": {
            "latitude": -22.95158,
            "longitude": -43.21074,
            "height": 30.0,
        },
        "JSONable": {
            "latitude": -22.95158,
            "longitude": -43.21074,
            "height": 30.0,
        },
    },
    # fmt: on
]

invalid_geographic_positions = [
    # fmt: off
    # Position must have latitude
    {
        "Python": {
            "longitude": -43.21074,
            "height": 30.0,
        },
        "JSONable": {
            "longitude": -43.21074,
            "height": 30.0,
        },
    },
    # Position must have longitude
    {
        "Python": {
            "latitude": -22.95158,
            "height": 30.0,
        },
        "JSONable": {
            "latitude": -22.95158,
            "height": 30.0,
        },
    },
    # Longitude cannot be larger 180°
    {
        "Python": {
            "latitude": -22.95158,
            "longitude": 181.1,
            "height": 30.0,
        },
        "JSONable": {
            "latitude": -22.95158,
            "longitude": 181.1,
            "height": 30.0,
        },
    },
    # Longitude cannot be smaller -180°
    {
        "Python": {
            "latitude": -22.95158,
            "longitude": -180.1,
            "height": 30.0,
        },
        "JSONable": {
            "latitude": -22.95158,
            "longitude": -180.1,
            "height": 30.0,
        },
    },
    # Longitude cannot be None
    {
        "Python": {
            "latitude": -22.95158,
            "longitude": None,
            "height": 30.0,
        },
        "JSONable": {
            "latitude": -22.95158,
            "longitude": None,
            "height": 30.0,
        },
    },
    # Longitude must not be string.
    {
        "Python": {
            "latitude": -22.95158,
            "longitude": "Not a float!",
            "height": 30.0,
        },
        "JSONable": {
            "latitude": -22.95158,
            "longitude": "Not a float!",
            "height": 30.0,
        },
    },
    # Latitude cannot be larger 90°
    {
        "Python": {
            "latitude": 90.1,
            "longitude": -22.95158,
            "height": 30.0,
        },
        "JSONable": {
            "latitude": 90.1,
            "longitude": -22.95158,
            "height": 30.0,
        },
    },
    # Latitude cannot be smaller -90°
    {
        "Python": {
            "latitude": -90.1,
            "longitude": -22.95158,
            "height": 30.0,
        },
        "JSONable": {
            "latitude": -90.1,
            "longitude": -22.95158,
            "height": 30.0,
        },
    },
    # Latitude cannot be None
    {
        "Python": {
            "latitude": None,
            "longitude": -22.95158,
            "height": 30.0,
        },
        "JSONable": {
            "latitude": None,
            "longitude": -22.95158,
            "height": 30.0,
        },
    },
    # Latitude must not be string.
    {
        "Python": {
            "latitude": "Not a float!",
            "longitude": -22.95158,
            "height": 30.0,
        },
        "JSONable": {
            "latitude": "Not a float!",
            "longitude": -22.95158,
            "height": 30.0,
        },
    },
    # Height must be float.
    {
        "Python": {
            "latitude": -22.95158,
            "longitude": -43.21074,
            "height": "Not a float!",
        },
        "JSONable": {
            "latitude": -22.95158,
            "longitude": -43.21074,
            "height": "Not a float!",
        },
    },
    # fmt: on
]

pv_systems = [
    # pv_system typical
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
    },
    # pv_system with floats
    {
        "Python": {
            "azimuth_angle": 5.4,
            "inclination_angle": 25.62,
            "nominal_power": 15.4,
            "power_datapoint_id": 2,
        },
        "JSONable": {
            "azimuth_angle": 5.4,
            "inclination_angle": 25.62,
            "nominal_power": 15.4,
            "power_datapoint_id": 2,
        },
    },
    # pv_system with 0 values
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": 0,
            "nominal_power": 0,
            "power_datapoint_id": 3,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": 0,
            "nominal_power": 0,
            "power_datapoint_id": 3,
        },
    },
    # pv_system with negative azimuth angle
    {
        "Python": {
            "azimuth_angle": -35,
            "inclination_angle": 90,
            "nominal_power": 15,
            "power_datapoint_id": 4,
        },
        "JSONable": {
            "azimuth_angle": -35,
            "inclination_angle": 90,
            "nominal_power": 15,
            "power_datapoint_id": 4,
        },
    },
]

invalid_pv_systems = [
    # pv_system must have azimuth angle
    {
        # fmt: off
        "Python": {
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        # fmt: on
    },
    # azimuth angle cannot be larger 90°
    {
        "Python": {
            "azimuth_angle": 180,
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 180,
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
    },
    # azimuth angle cannot be smaller -90°
    {
        "Python": {
            "azimuth_angle": -95,
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": -95,
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
    },
    # azimuth angle cannot be None
    {
        "Python": {
            "azimuth_angle": None,
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": None,
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
    },
    # azimuth angle must not be string.
    {
        "Python": {
            "azimuth_angle": "This is a string",
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": "This is a string",
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
    },
    # pv_system must have inclination angle
    {
        # fmt: off
        "Python": {
            "azimuth_angle": 0,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        # fmt: on
    },
    # inclination angle cannot be larger 90°
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": 95,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": 95,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
    },
    # inclination angle cannot be smaller 0°
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": -20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": -20,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
    },
    # inclination angle cannot be None
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": None,
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": None,
            "nominal_power": 15,
        },
    },
    # inclination angle must not be string.
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": "This is a string",
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": "This is a string",
            "nominal_power": 15,
            "power_datapoint_id": 1,
        },
    },
    # pv_system must have nominal power
    {
        # fmt: off
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "power_datapoint_id": 1,
        },
        # fmt: on
    },
    # nominal power cannot be smaller 0pkW
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": -15,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": -15,
            "power_datapoint_id": 1,
        },
    },
    # nominal power cannot be None
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": None,
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": None,
            "power_datapoint_id": 1,
        },
    },
    # nominal power must not be string.
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": "This is a string",
            "power_datapoint_id": 1,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": "This is a string",
            "power_datapoint_id": 1,
        },
    },
    # `power_datapoint_id` must exist and cannot be None.
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": 15,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": 15,
        },
    },
    {
        "Python": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": None,
        },
        "JSONable": {
            "azimuth_angle": 0,
            "inclination_angle": 20,
            "nominal_power": 15,
            "power_datapoint_id": None,
        },
    },
]

plants = [
    # fmt: off
    {
        # Minimal valid example for plant.
        "Python": {
            "id": None,
            "name": "Name",
        },
        "JSONable": {
            "id": None,
            "name": "Name",
            "product_ids": [],
            "geographic_position": None,
            "pv_system": None,
        },
    },
    # fmt: on
    {
        # Plant with geographic position defined.
        "Python": {
            "id": None,
            "name": "Name",
            "geographic_position": geographic_positions[0]["Python"],
        },
        "JSONable": {
            "id": None,
            "name": "Name",
            "product_ids": [],
            "geographic_position": geographic_positions[0]["JSONable"],
            "pv_system": None,
        },
    },
    {
        # Plant with pv system defined.
        # fmt: off
        "Python": {
            "id": None,
            "name": "Name",
            "pv_system": pv_systems[0]["Python"],
        },
        "JSONable": {
            "id": None,
            "name": "Name",
            "product_ids": [],
            "geographic_position": None,
            "pv_system": pv_systems[0]["JSONable"],
        },
        # fmt: on
    },
    {
        # Plant with geographic position and pv system defined.
        "Python": {
            "id": None,
            "name": "Name",
            "geographic_position": geographic_positions[0]["Python"],
            "pv_system": pv_systems[1]["Python"],
        },
        "JSONable": {
            "id": None,
            "name": "Name",
            "product_ids": [],
            "geographic_position": geographic_positions[0]["JSONable"],
            "pv_system": pv_systems[1]["JSONable"],
        },
    },
    {
        # Plant with product defined.
        "Python": {
            "id": None,
            "name": "Name",
            "product_ids": [1, 2],
            "geographic_position": geographic_positions[0]["Python"],
        },
        "JSONable": {
            "id": None,
            "name": "Name",
            "product_ids": [1, 2],
            "geographic_position": geographic_positions[0]["JSONable"],
            "pv_system": None,
        },
    },
    # fmt: off
    {
        # Plant with ID.
        "Python": {
            "id": 42,
            "name": "Name",
        },
        "JSONable": {
            "id": 42,
            "name": "Name",
            "product_ids": [],
            "geographic_position": None,
            "pv_system": None,
        },
    },
    # fmt: on
    # GOTCHA: If you define additional examples below, you have to set ID
    # as else the tests in django_models/test_django_metadata.py::TestPlant
    # will fail
]

invalid_plants = [
    # fmt: off
    {
        # Empty name is not allowed, b/c not expressive.
        "Python": {
            "name": "",
        },
        "JSONable": {
            "name": "",
        },
    },
    {
        # Name field must always be provided.
        "Python": {
            "geographic_position": None,
        },
        "JSONable": {
            "geographic_position": None,
        },
    },
    # fmt: on
]

products = [
    {
        # Minimal valid example for plant with a simple 24h coverage.
        "Python": {
            "name": "PVForecast",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": timedelta(days=0),
            "coverage_to": timedelta(days=1),
        },
        "JSONable": {
            "id": None,
            "name": "PVForecast",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": "PT0S",
            "coverage_to": "P1D",
        },
    },
    {
        # With more interesting timedelta values.
        "Python": {
            "name": "PVForecast2",
            "service_url": "http://example.com/product_service/v1/",
            # This is `-P0DT0H15M0S` might be realistic for PVForecast.
            "coverage_from": timedelta(days=0, seconds=-4500),
            # This is `P1DT0H59M0S` might be realistic for PVForecast.
            "coverage_to": timedelta(days=1, seconds=3540),
        },
        "JSONable": {
            "id": None,
            "name": "PVForecast2",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": "-PT1H15M",
            "coverage_to": "P1DT59M",
        },
    },
    {
        # With ID set..
        "Python": {
            "id": 42,
            "name": "PVForecast3",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": timedelta(days=0),
            "coverage_to": timedelta(days=1),
        },
        "JSONable": {
            "id": 42,
            "name": "PVForecast3",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": "PT0S",
            "coverage_to": "P1D",
        },
    },
]

invalid_products = [
    # Checks that all fields are required.
    {
        "Python": {
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": timedelta(days=0),
            "coverage_to": timedelta(days=1),
        },
        "JSONable": {
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": 0.0,
            "coverage_to": 86400,
        },
    },
    {
        "Python": {
            "name": "PVForecast",
            "coverage_from": timedelta(days=0),
            "coverage_to": timedelta(days=1),
        },
        "JSONable": {
            "name": "PVForecast",
            "coverage_from": 0.0,
            "coverage_to": 86400,
        },
    },
    {
        "Python": {
            "name": "PVForecast",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_to": timedelta(days=1),
        },
        "JSONable": {
            "name": "PVForecast",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_to": 86400,
        },
    },
    {
        "Python": {
            "name": "PVForecast",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": timedelta(days=0),
        },
        "JSONable": {
            "name": "PVForecast",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": 0.0,
        },
    },
    # Checks that fields cannot be None
    {
        "Python": {
            "name": None,
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": timedelta(days=0),
            "coverage_to": timedelta(days=1),
        },
        "JSONable": {
            "name": None,
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": 0.0,
            "coverage_to": 86400,
        },
    },
    {
        "Python": {
            "name": "PVForecast",
            "service_url": None,
            "coverage_from": timedelta(days=0),
            "coverage_to": timedelta(days=1),
        },
        "JSONable": {
            "name": "PVForecast",
            "plant_ids": [],
            "service_url": None,
            "coverage_from": 0.0,
            "coverage_to": 86400,
        },
    },
    {
        "Python": {
            "name": "PVForecast",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": None,
            "coverage_to": timedelta(days=1),
        },
        "JSONable": {
            "name": "PVForecast",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": None,
            "coverage_to": 86400,
        },
    },
    {
        "Python": {
            "name": "PVForecast",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": timedelta(days=0),
            "coverage_to": None,
        },
        "JSONable": {
            "name": "PVForecast",
            "service_url": "http://example.com/product_service/v1/",
            "coverage_from": 0.0,
            "coverage_to": None,
        },
    },
]

product_runs = [
    {
        # Minimal valid example for product run with a simple 24h coverage.
        "Python": {
            "product_id": 1,
            "available_at": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
            "coverage_from": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
            "coverage_to": datetime(2022, 5, 2, 0, tzinfo=timezone.utc),
        },
        "JSONable": {
            "id": None,
            "product_id": 1,
            "plant_ids": [],
            "available_at": "2022-05-01T00:00:00Z",
            "coverage_from": "2022-05-01T00:00:00Z",
            "coverage_to": "2022-05-02T00:00:00Z",
        },
    },
    {
        # With ID set.
        "Python": {
            "id": 2,
            "product_id": 1,
            "available_at": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
            "coverage_from": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
            "coverage_to": datetime(2022, 5, 2, 0, tzinfo=timezone.utc),
        },
        "JSONable": {
            "id": 2,
            "product_id": 1,
            "plant_ids": [],
            "available_at": "2022-05-01T00:00:00Z",
            "coverage_from": "2022-05-01T00:00:00Z",
            "coverage_to": "2022-05-02T00:00:00Z",
        },
    },
    {
        # With plant ids set..
        "Python": {
            "product_id": 1,
            "plant_ids": [1, 2, 42],
            "available_at": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
            "coverage_from": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
            "coverage_to": datetime(2022, 5, 2, 0, tzinfo=timezone.utc),
        },
        "JSONable": {
            "id": None,
            "product_id": 1,
            "plant_ids": [1, 2, 42],
            "available_at": "2022-05-01T00:00:00Z",
            "coverage_from": "2022-05-01T00:00:00Z",
            "coverage_to": "2022-05-02T00:00:00Z",
        },
    },
]

invalid_product_runs = [
    # Checks that required fields can't miss.
    {
        "Python": {
            "id": 2,
            "available_at": datetime(2022, 4, 1, 0, tzinfo=timezone.utc),
            "coverage_from": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
            "coverage_to": datetime(2022, 5, 2, 0, tzinfo=timezone.utc),
        },
        "JSONable": {
            "id": 2,
            "available_at": "2022-04-01T00:00:00Z",
            "coverage_from": "2022-05-01T00:00:00Z",
            "coverage_to": "2022-05-02T00:00:00Z",
        },
    },
    {
        "Python": {
            "id": 2,
            "product_id": 1,
            "available_at": datetime(2022, 4, 1, 0, tzinfo=timezone.utc),
            "coverage_to": datetime(2022, 5, 2, 0, tzinfo=timezone.utc),
        },
        "JSONable": {
            "id": 2,
            "product_id": 1,
            "plant_id": 1,
            "available_at": "2022-04-01T00:00:00Z",
            "coverage_to": "2022-05-02T00:00:00Z",
        },
    },
    {
        "Python": {
            "id": 2,
            "product_id": 1,
            "available_at": datetime(2022, 4, 1, 0, tzinfo=timezone.utc),
            "coverage_from": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
        },
        "JSONable": {
            "id": 2,
            "product_id": 1,
            "available_at": "2022-04-01T00:00:00Z",
            "coverage_from": "2022-05-01T00:00:00Z",
        },
    },
    # Check not null constraints.
    {
        "Python": {
            "id": 2,
            "product_id": None,
            "available_at": datetime(2022, 4, 1, 0, tzinfo=timezone.utc),
            "coverage_from": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
            "coverage_to": datetime(2022, 5, 2, 0, tzinfo=timezone.utc),
        },
        "JSONable": {
            "id": 2,
            "product_id": None,
            "available_at": "2022-04-01T00:00:00Z",
            "coverage_from": "2022-05-01T00:00:00Z",
            "coverage_to": "2022-05-02T00:00:00Z",
        },
    },
    {
        "Python": {
            "id": 2,
            "product_id": 1,
            "available_at": None,
            "coverage_from": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
            "coverage_to": datetime(2022, 5, 2, 0, tzinfo=timezone.utc),
        },
        "JSONable": {
            "id": 2,
            "product_id": 1,
            "available_at": None,
            "coverage_from": "2022-05-01T00:00:00Z",
            "coverage_to": "2022-05-02T00:00:00Z",
        },
    },
    {
        "Python": {
            "id": 2,
            "product_id": 1,
            "available_at": datetime(2022, 4, 1, 0, tzinfo=timezone.utc),
            "coverage_from": None,
            "coverage_to": datetime(2022, 5, 2, 0, tzinfo=timezone.utc),
        },
        "JSONable": {
            "id": 2,
            "product_id": 1,
            "available_at": "2022-04-01T00:00:00Z",
            "coverage_from": None,
            "coverage_to": "2022-05-02T00:00:00Z",
        },
    },
    {
        "Python": {
            "id": 2,
            "product_id": 1,
            "available_at": datetime(2022, 4, 1, 0, tzinfo=timezone.utc),
            "coverage_from": datetime(2022, 5, 1, 0, tzinfo=timezone.utc),
            "coverage_to": None,
        },
        "JSONable": {
            "id": 2,
            "product_id": 1,
            "available_at": "2022-04-01T00:00:00Z",
            "coverage_from": "2022-05-01T00:00:00Z",
            "coverage_to": None,
        },
    },
]
