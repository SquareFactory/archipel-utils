"""Copyright Alpine Intuition Sàrl team.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from argparse import Namespace

import archipel_utils as utils


def test_get_vram(mocker):
    """Test get vram usages of one or more pids."""
    mocker.patch("subprocess.run", return_value=Namespace(stdout="1031, 57571"))
    assert utils.get_vram_usages(10) == {10: 0}
    assert utils.get_vram_usages([10, 11]) == {10: 0, 11: 0}


def test_get_ram():
    """Test get ram usages of one or more pids."""
    results = {10: {"used": 0, "virt": 0}}
    assert utils.get_ram_usages(10) == results
    results = {10: {"used": 0, "virt": 0}, 11: {"used": 0, "virt": 0}}
    assert utils.get_ram_usages([10, 11]) == results
