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


import pytest

import archipel_utils as utils


def test_get_num_gpus():
    """Test get number of gpus."""
    utils.get_num_gpus()


def test_get_device_vram_usage(mocker):
    """Test get device vram usage."""

    # No gpus

    utils.process.GPUS_AVAILABLE = False

    with pytest.raises(RuntimeError):
        utils.get_device_vram_usage(0)

    # One gpu

    utils.process.GPUS_AVAILABLE = True
    utils.process.NUM_GPUS = 1

    with pytest.raises(ValueError):
        utils.get_device_vram_usage(2)

    with pytest.raises(ValueError):
        utils.get_device_vram_usage(-1)

    mocker.patch("py3nvml.py3nvml.nvmlDeviceGetHandleByIndex")

    class FakeInfo:
        free = 2000000
        used = 3000000

    mocker.patch("py3nvml.py3nvml.nvmlDeviceGetMemoryInfo", return_value=FakeInfo)

    assert utils.get_device_vram_usage(0, free=False) == 2  # 300000 >> 20
    assert utils.get_device_vram_usage(0, free=True) == 1  # 200000 >> 20


def test_get_devices_vram_usage(mocker):
    """Test get devices vram usage."""

    vrams = [1, 2]
    mocker.patch("archipel_utils.process.get_device_vram_usage", side_effect=vrams)

    utils.process.NUM_GPUS = 2

    usages = utils.get_devices_vram_usage()
    assert len(usages) == 2
    assert usages[0] == vrams[0]
    assert usages[1] == vrams[1]


def test_get_vram(mocker):
    """Test get vram usages of one or more pids."""

    mocker.patch("py3nvml.py3nvml.nvmlDeviceGetHandleByIndex")

    class DumpProcess:
        def __init__(self, pid, mem):
            self.pid = pid
            self.usedGpuMemory = mem

    processes = [DumpProcess(1, 2), DumpProcess(3, 4), DumpProcess(6, 7)]

    mocker.patch(
        "py3nvml.py3nvml.nvmlDeviceGetComputeRunningProcesses", return_value=processes
    )

    usages = utils.get_vram_usages(1)
    assert usages[1] == 2

    pids = [1, 3, 5]
    usages = utils.get_vram_usages(pids)

    assert len(usages) == len(pids)
    assert usages[3] == 4
    assert usages[5] == 0


def test_get_ram():
    """Test get ram usages of one or more pids."""
    results = {10: {"used": 0, "virt": 0}}
    assert utils.get_ram_usages(10) == results
    results = {10: {"used": 0, "virt": 0}, 11: {"used": 0, "virt": 0}}
    assert utils.get_ram_usages([10, 11]) == results
