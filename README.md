LRG_Parser
============
Description: This parser takes an LRG-XML file and extracts key exon information.

More information on LRG files can be found at http://www.lrg-sequence.org/lrg

Authors
-------

The LRG parser was written by Joseph Halstead and Nichola Cooper.

Features
--------
Outputs a .txt file containing information as described below:

A file header containing gene data as shown below:

Gene Name:
Refseq ID:
LRG ID:
HGNC ID:

And then for each exon the following information is inserted into the text file.
 
Exon ID:
Exon Start:
Exon End: 
Exon Sequence:
Exon Transcript: 

Exon information is extracted for all exons in all transcripts. A warning message will be displayed at the top of the output file if more than one transcript is present. 

The output file will be named as {LRG-ID}{today's date}.txt and will be saved in your current directory.

Note: If there is already a file with that name then it will be overwritten.


Installation
------------
The parser requires a Python installation to run. Install Python version 2 or above. The LRG Parser has been tested on Python 2.7 and 3.5.

Clone all files from https://github.com/CooperNh/LRG_Parser.git

cd into LRG_Parser directory.


Usage
-----
To run the LRG Parser, navigate to the LRG Parser directory and run the following command within your terminal:

python xml_lrg_parser.py {input-lrg}.xml

Testing
------

The parser comes with a test suite in  the file tests.py.

The test suite contains a series of unit tests that check whether the software is working correctly.

To run the tests run the following command within your terminal: python tests.py
