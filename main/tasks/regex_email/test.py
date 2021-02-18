from pathlib import Path
from ...lib.testcase import SimpleTestCase
from ...lib.expectation import ListExpectation
import os


# TODO: get unordered expectations (set?), remove sorts

emails_path = Path(os.path.dirname(__file__)) / "files/emails"

def test_cases():
    return [
            SimpleTestCase(["address", emails_path], ListExpectation([
                "address1@domain1.net",
                "address2@domain2.org",
                "address3@domain1.net",
                "address4@domain3.com"
                ])),
            SimpleTestCase(["domains", emails_path], ListExpectation([
                "domain1.net",
                "domain2.org",
                "domain3.com"
                ])),
            SimpleTestCase(["tlds", emails_path], ListExpectation([
                "com",
                "net",
                "org"
                ]))
            ]
