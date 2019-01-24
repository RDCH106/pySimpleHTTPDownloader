import sys
import urllib.request


class HTTPDownloader(object):

    def __init__(self, url=None):
        self.__url = url

    @staticmethod
    def __reporthook__(blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if readsofar > totalsize:
            readsofar = totalsize
        if totalsize > 0:
            percent = readsofar * 1e2 / totalsize
            s = "\r%5.1f%% %*d / %d" % (
                percent, len(str(totalsize)), readsofar, totalsize)
            sys.stderr.write(s)
            if readsofar >= totalsize:  # near the end
                sys.stderr.write("\n")
        else:  # total size is unknown
            sys.stderr.write("read %d\n" % (readsofar,))

    def run(self):
        print("download start!")
        filename, headers = urllib.request.urlretrieve(
            self.__url,
            filename="I_Love_Firefox_220x56.png",
            reporthook=self.__reporthook__)
        print("download complete!")
        print("download file location: ", filename)
        print("download headers: ", headers)


if __name__ == "__main__":
    downloader = HTTPDownloader(
        "https://raw.githubusercontent.com/RDCH106/i-love-firefox/183266a9/I_Love_Firefox_220x56.png"
    )
    downloader.run()
