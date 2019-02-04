# pySimpleHTTPDownloader (shttpd)

[![GitHub](https://img.shields.io/github/license/RDCH106/pySimpleHTTPDownloader.svg)](https://github.com/RDCH106/pySimpleHTTPDownloader/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0500238c437d413bb1d85acff33a43ff)](https://www.codacy.com/app/RDCH106/pySimpleHTTPDownloader?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=RDCH106/pySimpleHTTPDownloader&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/RDCH106/pySimpleHTTPDownloader.svg?branch=master)](https://travis-ci.org/RDCH106/pySimpleHTTPDownloader)

Simple HTTP downloader written in Python

### Installation

You can install or upgrade shttpd with:

`$ pip install shttpd --upgrade`

Or you can install from source with:

```bash
$ git clone https://github.com/RDCH106/pySimpleHTTPDownloader.git --recursive
$ cd pysimplehttpdownloader
$ pip install .
```

### Quick example

```bash
$ shttpd -u https://raw.githubusercontent.com/RDCH106/i-love-firefox/183266a9/I_Love_Firefox_220x56.png
```

The example downloads `I_Love_Firefox_220x56.png` in current path.


### Help

Run the following command to see all options available:

`shttpd --help` or ` shttpd -h`
