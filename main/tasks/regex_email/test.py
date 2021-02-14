from pathlib import Path
import os
from ...lib.testcase import SimpleTestCase

this_file_path = Path(os.path.dirname(__file__))
def test_cases():
    print(this_file_path / "files/emails")
    return [
            SimpleTestCase(this_file_path / "files/emails", "asdf")
            ]
