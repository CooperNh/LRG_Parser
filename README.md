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

Exon information is extracted for all exons in all transcripts. 

The output file name will {LRG-ID}{today's date}.txt and will be saved in your current directory.

Installation
------------
The parser requires a Python installation to run. Install Python version 2 or above. The LRG Parser has been tested on Python 2.7 and 3.5.

Clone all files from https://github.com/CooperNh/LRG_Parser.git

cd into LRG_Parser directory.


Usage
-----
To run the LRG Parser, run the following command within your terminal:

python xml_lrg_parser.py {input-lrg}.xml



