PersonalScripts
===============

How to Install:
===============
```bash
git clone git://github.com/besirkurtulmus/PersonalScripts/PersonalScripts.git
```

### 1. MergePdf.py

Merges pdf files in a given directory. Merges the pdf files alphabetically.

Usage:
```bash
$ python MergePdf.py {directory}
```

Help:
```bash
$ python MergePdf.py --help
```

Example:
```bash
$ python MergPdf.py ~/Desktop/pdfFiles/
Pdf files merged in ~/Desktop/pdfFiles/allPdfPages.pdf
```
### 2. DepleteBandwidth.py

Depletes and wastes the bandwidth of the given web server.

Usage:
```bash
$ python DepleteBandwidth.py {url} {number_requests} {number_cycles}
```

Help:
```bash
$ python DepleteBandwidth.py --help
```

Example:
```bash
$ python DepleteBandwidth.py http://example.com/file.zip 1000 1100
Amount of total bandwidth wasted: 554 MB
Amount of total bandwidth wasted: 1108 MB
```
