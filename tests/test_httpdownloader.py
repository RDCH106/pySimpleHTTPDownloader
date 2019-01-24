# -*- coding: utf-8 -*-

import unittest
import os
import shutil


class TestPFS(unittest.TestCase):
    def setUp(self):
        path = os.path.dirname(os.path.abspath(__file__)) + "/tmp/download"
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

    def tearDown(self):
        pass

    def test_empty(self):
        print("TO-DO")


if __name__ == '__main__':
    unittest.main(verbosity=2)
