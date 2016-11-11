import xml.etree.ElementTree as ET
import sys
import datetime


def get_sequence(root):
	"""
	This function extracts the DNA sequence from the LRG file
	returns a string of the sequence	
	"""
	for fixed in root.findall('fixed_annotation'):
		sequence = fixed.find('sequence').text		
		for base in sequence:
			assert base in ['A', 'C', 'T', 'G' ], 'Invalid base - must contain ATGC only'
		return str(sequence)
		
		
def get_gene_data(root):
	""""This function extracts sequence source, LRG ID, HGNC ID and Gene Name from the LRG file
	and returns a list containing all the gene data"""
	for fixed in root.findall('fixed_annotation'):
		sequence_source = fixed.find('sequence_source').text
		lrg_id = fixed.find('id').text
		hgnc_id = fixed.find('hgnc_id').text
	
	annotation_sets = root.findall("./updatable_annotation/annotation_set")
	
	#Not all LRG files will contain a gene name under 'lrg_locus', this try-except will catch any instances where no gene name is found. 
	try:
		for set in annotation_sets:
			if set.attrib ['type'] == 'lrg':	
				gene_name = set.findall("lrg_locus")
	except:
		gene_name = 'Gene name not found'
			
			
	return [sequence_source, lrg_id, hgnc_id, gene_name[0].text]
	
def create_text_file(gene_data, all_data, transcript_num):
	"""This function creates a new text file containing containing a multiple transcipt warning, gene data, data for each exon and exon sequence 
	separated by a new line """
	
	#Each new file will be given the LRG file name and a current date stamp 
	time_stamp = datetime.datetime.now().strftime('%Y-%m-%d')
	file = open((gene_data[1] + " " + time_stamp +  ".txt"), 'w') #file created in current directory
	
	#Checks if transcript count is >1 and puts warning in file if true 
	if transcript_num > 1:
		file.write("WARNING: This file has more than one transcript!" + "\n")
		file.write(" " + "\n")
	
	
	#add data that applies to whole LRG file e.g. gene name
	file.write("Gene Name:" + " " + gene_data[3] + "\n")
	file.write("Refseq ID:" + " " + gene_data[0]+"\n")
	file.write("LRG ID:" + " " + gene_data[1]+"\n")
	file.write("HGNC ID:" + " " + gene_data[2]+"\n")
	file.write(" "+"\n")

	#For each exon in the file insert the exon data and then a new line
	for exon in all_data:
	
		file.write("Exon ID:" + " " + exon[0]+"\n")
		file.write("Exon Start:" + " " + str(exon[1])+"\n")
		file.write("Exon End:" + " " + str(exon[2])+"\n")
		file.write("Exon Sequence:" + " " + exon[3]+"\n")
		file.write("Exon Transcript:" + " " + exon[4]+"\n")
	
		file.write(" "+"\n")
	
	file.close()
		
	
def count_transcripts(root):
	"""Simple function to count the number of transcripts in a LRG file. Input is the root of the LRG file.
	Output is a int value of the transcript count """

	list= root.findall('fixed_annotation/transcript')
		
	return len(list)
			
def get_exons(root):
	"""
	This functions extracts the exon label, exon coordinates (start,end) and transcipt name for each exon.
	
	Input is the root of the LRG XML file
	
	The function returns a list called all_exons which contains another list for each exon containing [exon label, coordinates and transcript_name]

	"""
	all_exons =[]
	
	
	for transcript in root.findall('fixed_annotation/transcript'): # for each transcipt
	
		transcript_name = transcript.attrib
		
		for exon in transcript.findall('exon'): #for each exon in transcipt
			
			exon_label = exon.attrib
			list_of_coord = exon.findall('coordinates')
	
			coordinates = list_of_coord[0].attrib
	
			all_exons.append([exon_label, coordinates, transcript_name]) #add list to master list (all_exons)

		
	return all_exons

	
def get_exon_sequence(sequence, exon_list):

	"""
	This function gets all the information for each exon. For a given exon it will return a list
	containing the exon label, exon start, exon end, exon sequence and exon transcipt name.
	
	The exon sequence is sliced from the main sequence in the LRG file.
	
	Note: The exon_list input is a list containg the information for a single exon.

	"""
	exon_label = exon_list[0]['label']
	exon_start = exon_list[1]['start']
	exon_end = exon_list[1]['end']
	exon_transcript = exon_list[2]['name']
	
	exon_start = int(exon_start)
	exon_end = int(exon_end)
	exon_start = exon_start - 1 #offset to account for the LRG file using 1 based numbering rather than Python's 0.
	exon_end = exon_end 
	
	exon_sequence = sequence [exon_start:exon_end] #slice exon out of main sequence
	
	assert exon_end > exon_start, 'Exon end is greater than exon start' #checks exon end is greater than exon start
	
	return [exon_label, exon_start + 1, exon_end, exon_sequence, exon_transcript]
	
		
def main():

	try:
	
		tree = ET.parse(sys.argv[1]) #attempt to parse XML file and print error if we fail
			
	except:
	
		print ('Error: please load an XML file')
		return None
	
	try:
	
		root = tree.getroot()
		assert root.tag == ('lrg') #assert to catch XML files that are not LRG files
		
	except:
	
		print ('Please load a valid LRG file')
		return None
	
	sequence = get_sequence(root) #get main sequence

	exons = get_exons(root) #get list containg all exon data
	
	gene_data = get_gene_data(root)# get gene data
	
	all_exon_data =[]
	
	for exon in exons: # go through each exon and slice out sequence data and append this as a list to all_exon_data
		
		exon_data = get_exon_sequence(sequence, exon)
		
		all_exon_data.append(exon_data)
		
	transcript_count = (count_transcripts(root)) #get transcript count
		
	create_text_file(gene_data, all_exon_data, transcript_count) #create a text file containing all the extracted information.
	

		
if __name__ =='__main__':
	main()


	
	
	
	
	