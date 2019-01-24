# -*- coding: utf-8 -*-

import unittest
import os
import shutil
from pysimplehttpdownloader.http_downloader import HTTPDownloader


path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp", "download")


class TestPFS(unittest.TestCase):

    def setUp(self):
        try:
            os.mkdir(path)
        except OSError:
            print("\nCreation of the directory %s failed" % path)
        else:
            print("\nSuccessfully created the directory %s " % path)

    def tearDown(self):
        try:
            shutil.rmtree(path)
        except IOError:
            print("Deletion of the directory %s failed" % path)
        else:
            print("Successfully deleted the directory %s " % path)

    def test_smart_downloader(self):
        downloader = HTTPDownloader(
            "https://raw.githubusercontent.com/RDCH106/i-love-firefox/183266a9/I_Love_Firefox_220x56.png",
            output_path=path
        )
        filename, headers = downloader.run()
        print("download file location: ", filename)
        print("download headers: ", headers)
        self.assertTrue(os.path.isfile(os.path.join(path, filename)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
