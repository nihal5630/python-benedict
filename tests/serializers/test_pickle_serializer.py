# -*- coding: utf-8 -*-

from benedict.serializers import Base64Serializer
from benedict.serializers import PickleSerializer

import datetime as dt
import unittest


class pickle_serializer_test_case(unittest.TestCase):

    # def test_decode_pickle(self):
    #     s = 'gAN9cQBYBAAAAGRhdGVxAWNkYXRldGltZQpkYXRldGltZQpxAkMKB8EEAwAAAAAAAHEDhXEEUnEFcy4='
    #     d = Base64Serializer().decode(s, subformat='pickle')
    #     r = {
    #         'date': dt.datetime(year=1985, month=4, day=3),
    #     }
    #     self.assertEqual(d, r)

    def test_encode_decode_pickle(self):
        d = {
            'date': dt.datetime(year=1985, month=4, day=3),
        }
        serializer = Base64Serializer()
        s = serializer.encode(d, subformat='pickle')
        r = serializer.decode(s, subformat='pickle')
        self.assertEqual(d, r)
