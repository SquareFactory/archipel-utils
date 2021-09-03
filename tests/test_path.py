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

from pathlib import Path

import archipel_utils as utils


def test_cd():
    """Test change current working during through context manager."""
    initial_path = Path.cwd().resolve()
    new_path = Path("archipel_utils").resolve()
    with utils.cd(new_path):
        assert str(new_path) == str(Path.cwd())
    assert str(initial_path) == str(Path.cwd())
