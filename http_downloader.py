import urllib.request

url = "https://raw.githubusercontent.com/RDCH106/i-love-firefox/183266a9/I_Love_Firefox_220x56.png"
print ("download start!")
filename, headers = urllib.request.urlretrieve(url, filename="I_Love_Firefox_220x56.png")
print ("download complete!")
print ("download file location: ", filename)
print ("download headers: ", headers)
