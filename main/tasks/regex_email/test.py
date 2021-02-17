from pathlib import Path
import os
from ...lib.testcase import SimpleTestCase

# TODO: get unordered expectations (set?), remove sorts

emails_path = Path(os.path.dirname(__file__)) / "files/emails"

def test_cases():
    return [
            SimpleTestCase(["address", emails_path], [
                "address1@domain1.net",
                "address2@domain2.org",
                "address3@domain1.net",
                "address4@domain3.com"
                ]),
            SimpleTestCase(["domains", emails_path], [
                "domain1.net",
                "domain2.org",
                "domain3.com"
                ]),
            SimpleTestCase(["tlds", emails_path], [
                "com",
                "net",
                "org"
                ])
            ]
