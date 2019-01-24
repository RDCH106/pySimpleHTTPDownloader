# -*- coding: utf-8 -*-

import unittest
import os
import shutil


path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"tmp", "download")


class TestPFS(unittest.TestCase):

    def setUp(self):
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

    def tearDown(self):
        try:
            shutil.rmtree(path)
        except IOError:
            print("Deletion of the directory %s failed" % path)
        else:
            print("Successfully deleted the directory %s " % path)

    def test_empty(self):
        print("TO-DO")


if __name__ == '__main__':
    unittest.main(verbosity=2)
