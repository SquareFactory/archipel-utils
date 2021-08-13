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

import msgpack
import pytest

import archipel_utils as utils


def test_encode_msg():
    """Test encode msg."""

    with pytest.raises(ValueError):
        utils.get_encoded_msg("zbl")

    msg = {"status": "success", "data": "zbl"}
    encoded_msg = utils.get_encoded_msg(**msg)
    assert encoded_msg == msgpack.packb(msg)

    msg = {"status": "error", "message": "zbl"}
    encoded_msg = utils.get_encoded_msg(**msg)
    assert encoded_msg == msgpack.packb(msg)


@pytest.mark.parametrize(
    "msg",
    [
        msgpack.packb({"status": "success", "data": "data"}),
        msgpack.packb({"status": "fail", "message": "msg"}),
    ],
)
def test_decode_valid_msg(msg):
    """Test message decode function with valid message."""
    success, error_msg, decoded_msg = utils.get_decoded_msg(msg, {"status"})
    assert success
    assert error_msg == ""
    assert decoded_msg != {}


@pytest.mark.parametrize(
    "msg",
    [
        "zbl",
        b"zbl",
        msgpack.packb(["zbl", "zbl"]),
        msgpack.packb({"zbl": "zbl"}),
        msgpack.packb({"status": "success"}),
        msgpack.packb({"status": "fail"}),
    ],
)
def test_decode_invalid_msg(msg):
    """Test message decode function with invalid message."""
    success, error_msg, decoded_msg = utils.get_decoded_msg(msg, {"status"})
    assert not success
    assert error_msg != ""
    assert decoded_msg == {}


def test_get_obj_size():
    """Test get byte size of an object."""
    assert utils.get_obj_size([]) > 0
    assert utils.get_obj_size("") > 0
    assert utils.get_obj_size({}) > 0


def test_sanitize_inputs():
    """Test sanitize_inputs."""
    assert "-coucou99_" == utils.sanitize_inputs(";-.couCou99_@")
