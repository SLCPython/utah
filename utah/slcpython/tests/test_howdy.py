from contextlib import contextmanager
from io import StringIO
import sys

from unittest import TestCase
from unittest.mock import patch

from utah.slcpython import howdy


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestHowdy(TestCase):
    @patch('utah.slcpython.meetup.api')
    def test_howdy_prints_info(self, client):
        with captured_output() as (out, err):
            howdy()
        output = out.getvalue()
        print(output)
        msg = """
        Howdy, Salt Lake City!
        "Our next meetup is on:"
        "Wednesday, September 5th, at 6:30 p.m."
        "and is about:"
        "A trio of python talks: Beginning / Intermediate / Advanced"
        """
        self.assertEquals(output.strip(), msg.strip())
