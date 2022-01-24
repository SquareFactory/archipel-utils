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

import numpy as np
import pytest

import archipel_utils as utils


@pytest.mark.parametrize(
    "array",
    [
        np.random.randint(0, 256, (500, 500, 3), np.uint8),
        np.random.randint(0, 65536, (500, 500, 3), np.uint16),
        np.random.rand(500, 500, 3).astype(np.float32),
        np.random.randint(0, 256, (10, 500, 500, 3), np.uint8),
    ],
)
def test_serialize_deserialize_array(array):
    """Test serialized and deserialized array.

    Tested:
        - 8 bits int img (0256)
        - 16 bits int img (0-65536)
        - 32 bits float img (0-1)
        - 8 bits video [FRAMExWxLxC]
    """

    serialized_array = utils.serialize_array(array)
    assert isinstance(serialized_array, bytes)

    deserialized_array = utils.deserialize_array(serialized_array)
    assert isinstance(deserialized_array, np.ndarray)

    assert np.equal(array, deserialized_array).all()
