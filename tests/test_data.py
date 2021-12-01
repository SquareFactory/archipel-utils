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


def test_serialize_deserialize_img():
    """Test serialized and deserialized img."""
    fake_img = np.random.randint(0, 255, (600, 600, 3)).astype(np.uint8)
    serialized_img = utils.serialize_img(fake_img)
    deserialized_img = utils.deserialize_img(serialized_img)
    assert np.equal(fake_img, deserialized_img).all()


@pytest.mark.parametrize(
    "img",
    [
        np.random.randint(0, 1024, (600, 600, 3)),  # 32 bits image
        np.random.rand(600, 600, 3),  # 0-1, float image
    ],
)
def test_serialize_img_fail(img):
    """Test serialized img with wrong data."""
    with pytest.raises(ValueError):
        utils.serialize_img(img)


def test_deserialize_img_fail(mocker):
    """Test deserialized img with wrong data."""
    mocker.patch("cv2.imdecode", return_value=None)
    with pytest.raises(ValueError):
        img = np.random.randint(0, 255, (600, 600, 3))
        serialized_img = utils.serialize_img(img)
        utils.deserialize_img(serialized_img)
