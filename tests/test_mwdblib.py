import unittest


class TestPublicApi(unittest.TestCase):
    def test_public_api(self):
        """
        This imports are a part of the public API and should never be removed
        """
        from vxdb import MWDB  # noqa
        from vxdb import APIClient # noqa
        from vxdb import MWDBFile  # noqa
        from vxdb import MWDBObject  # noqa
        from vxdb import MWDBConfig  # noqa
        from vxdb import MWDBBlob  # noqa
