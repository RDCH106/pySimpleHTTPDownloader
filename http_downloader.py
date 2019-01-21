import sys
import urllib.request

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))

url = "https://raw.githubusercontent.com/RDCH106/i-love-firefox/183266a9/I_Love_Firefox_220x56.png"
print ("download start!")
filename, headers = urllib.request.urlretrieve(url, filename="I_Love_Firefox_220x56.png", reporthook=reporthook)
print ("download complete!")
print ("download file location: ", filename)
print ("download headers: ", headers)
