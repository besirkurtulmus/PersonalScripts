#!/usr/bin/python
# coding: utf-8
'''
The MIT License (MIT)

Copyright (c) 2014 Ahmet Besir Kurtulmus

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import glob
import sys

from pyPdf import PdfFileReader, PdfFileWriter


class MergePdf:
	'''
	Description: Merges pdf pages into a single pdf document, in the given
		directory.

	Arguments:
		Directory (String type): The directory of the pdf files

	Example:
	>>> merge = MergePdf('/usr/root/Desktop/pdfFiles/')
	Pdf files merged in /usr/root/Desktop/allPdfPages.pdf
	'''
	def __init__(self, directory):
		self.directory = directory

	def Merge(self):
		pdfFiles = glob.glob(self.directory + '*.pdf')

		allPages = PdfFileWriter()

		for pdfPage in pdfFiles:
			page = PdfFileReader(file(pdfPage))
			for i in range(page.getNumPages()):
				allPages.addPage(page.getPage(i))

		newPdf = file(self.directory + "allPdfPages.pdf", "wb")
		allPages.write(newPdf)
		newPdf.close()

		print "Pdf files merged in " + self.directory + "allPdfPages.pdf"

if (len(sys.argv) == 2) and (sys.argv[1] == "--help"):
	print """\nUSAGE: $ python MergePdf.py [directory]
	directory (String type): The directory of the pdf files.

EXAMPLE:
	$ python MergePdf.py ~/Desktop/pdfFiles/
	"""
elif len(sys.argv) == 2:
	if sys.argv[1][len(sys.argv[1])-1] != "/":
		directory = sys.argv[1] + "/"
	else:
		directory = sys.argv[1]
	newPdf = MergePdf(directory)
	newPdf.Merge()
else:
	print "\nFor help, type the --help command."
