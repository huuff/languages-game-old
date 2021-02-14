from pathlib import Path
import os
from ...lib.testcase import SimpleTestCase

this_file_path = Path(os.path.dirname(__file__))
def test_cases():
    print(this_file_path / "files/emails")
    return [
            SimpleTestCase(this_file_path / "files/emails", [
                "address1@domain1.net",
                "address2@domain2.org",
                "address3@domain1.net",
                "address4@domain3.com"
                ])
            ]
