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

import subprocess
from tempfile import NamedTemporaryFile

import cv2
import numpy as np
import pytest

import archipel_utils as utils

arrays = [
    np.random.randint(0, 256, (500, 500, 1), np.uint8),
    np.random.randint(0, 256, (500, 500), np.uint8),
    np.random.randint(0, 256, (500, 500, 3), np.uint8),
    np.random.randint(0, 65536, (500, 500, 3), np.uint16),
    np.random.rand(500, 500, 3).astype(np.float32),
    np.random.randint(0, 256, (10, 500, 500, 3), np.uint8),
]


@pytest.mark.parametrize("img", [arrays[0]])
def test_serialize_img(img):
    """Test deserialized img."""

    with NamedTemporaryFile(suffix=".txt") as tmp0, NamedTemporaryFile(
        suffix=".png"
    ) as tmp1:
        tmp0.write(utils.serialize_array(img))
        tmp0.seek(0)

        cmd = f"base64 --decode {tmp0.name} > {tmp1.name}"
        subprocess.run(
            cmd,
            shell=True,
            check=True,
        )

        decoded = cv2.imread(tmp1.name)
        assert np.equal(img, decoded).all()


@pytest.mark.parametrize("img", [arrays[0]])
def test_deserialize_img(img):
    """Test deserialized img."""

    with NamedTemporaryFile(suffix=".png") as tmp:
        cv2.imwrite(tmp.name, img)

        out = subprocess.run(
            ["base64", tmp.name], check=True, stdout=subprocess.PIPE, text=True
        )
        serialized_array = out.stdout.strip().encode()

        deserialized_img = utils.deserialize_array(serialized_array)
        assert np.equal(img, deserialized_img).all()


def test_opencv_not_available():
    """Test deserialization when no opencv."""
    utils.data.OPENCV_AVAILABLE = False
    with pytest.raises(ModuleNotFoundError):
        utils.deserialize_array(b"")


@pytest.mark.parametrize("array", arrays)
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


# def test_serialize_deserialize_img():
#     """Test serialized and deserialized img."""

#     img = np.random.randint(0, 256, (500, 500, 3), np.uint8)
#     with pytest.deprecated_call():
#         serialized_img = utils.serialize_img(img)
#     with pytest.deprecated_call():
#         deserialized_img = utils.deserialize_img(serialized_img)
#     assert np.equal(img, deserialized_img).all()
