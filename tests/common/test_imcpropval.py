# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from imcsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit
from imcsdk.mometa.power.PowerBudget import PowerBudget


@pytest.fixture
def setup_func():
    return ComputeRackUnit(parent_mo_or_dn="sys", server_id="1")


def test_001_set_ro_property(setup_func):
    # This is a read only property
    # Should fail with an exception
    with pytest.raises(Exception):
        setup_func.available_memory = "22334"


def test_002_set_rw_property(setup_func):
    # This is a read write property.
    # Should happen without any issues
    setup_func.status = "created"
    assert setup_func.status == "created"


def test_003_set_naming_property(setup_func):
    # This is a naming property. so, it is create only
    # Should fail with an exception
    with pytest.raises(Exception):
        setup_func.server_id = "15"


def test_004_set_rw_ro_property():
    obj = PowerBudget(parent_mo_or_dn="sys/rack-unit-1")
    obj.status = "modified"

    obj = PowerBudget(parent_mo_or_dn="sys/chassis-1/server-1")
    obj.status = "modified"
