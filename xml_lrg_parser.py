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
	for fixed in root.findall('fixed_annotation'):
		sequence_source = fixed.find('sequence_source').text
		lrg_id = fixed.find('id').text
		hgnc_id = fixed.find('hgnc_id').text
	
	annotation_sets = root.findall("./updatable_annotation/annotation_set")
	try:
		for set in annotation_sets:
			if set.attrib ['type'] == 'lrg':	
				gene_name = set.findall("lrg_locus")
	except:
		gene_name = 'Gene name not found'
			
		

		

			
	return [sequence_source, lrg_id, hgnc_id, gene_name[0].text]
	
def create_text_file(gene_data, all_data, transcript_num):
	time_stamp = datetime.datetime.now().strftime('%Y-%m-%d')
	file = open((gene_data[1] + " " + time_stamp +  ".txt"), 'w')
	if transcript_num > 1:
		file.write("WARNING: This file has more than one transcript!" + "\n")
	
	
	
	file.write("Gene Name:" + " " + gene_data[3] + "\n")
	file.write("Refseq ID:" + " " + gene_data[0]+"\n")
	file.write("LRG ID:" + " " + gene_data[1]+"\n")
	file.write("HGNC ID:" + " " + gene_data[2]+"\n")
	file.write(" "+"\n")

	
	for exon in all_data:
	
		file.write("Exon ID:" + " " + exon[0]+"\n")
		file.write("Exon Start:" + " " + str(exon[1])+"\n")
		file.write("Exon End:" + " " + str(exon[2])+"\n")
		file.write("Exon Sequence:" + " " + exon[3]+"\n")
		file.write("Exon Transcript:" + " " + exon[4]+"\n")

		
		
		file.write(" "+"\n")
	
	file.close()
		
	
def count_transcripts(root):
		list= root.findall('fixed_annotation/transcript')
		
		return len(list)
			
	


def get_exons(root):

	all_exons =[]
	
	
	for transcript in root.findall('fixed_annotation/transcript'):
	
		transcript_name = transcript.attrib
		
		for exon in transcript.findall('exon'):
			
			exon_label = exon.attrib
			list_of_coord = exon.findall('coordinates')
	
			coordinates = list_of_coord[0].attrib
	
			all_exons.append([exon_label, coordinates, transcript_name])

		
	return all_exons




	
def get_exon_sequence(sequence, exon_list):
	exon_label = exon_list[0]['label']
	exon_start = exon_list[1]['start']
	exon_end = exon_list[1]['end']
	exon_transcript = exon_list[2]['name']
	
	exon_start = int(exon_start)
	exon_end = int(exon_end)
	exon_start = exon_start - 1
	exon_end = exon_end 
	
	exon_sequence = sequence [exon_start:exon_end]
	
	assert exon_end > exon_start, 'Exon end is greater than exon start'
	
	return [exon_label, exon_start + 1, exon_end, exon_sequence, exon_transcript]
	
		
		
		
		
		
		
		

def main():

	try:
		tree = ET.parse(sys.argv[1])
	
	except:
		print ('Error: please load an XML file')
		return None
		
	root = tree.getroot()

	sequence = get_sequence(root)

	exons = get_exons(root)
	
	gene_data = get_gene_data(root)
	
	all_exon_data =[]
	
	for exon in exons:
		
		exon_data = get_exon_sequence(sequence, exon)
		
		all_exon_data.append(exon_data)
		
	transcript_count = (count_transcripts(root))
		

	create_text_file(gene_data, all_exon_data, transcript_count)
	
	
	
	"""
	print (get_gene_data(root))
	print (sequence)
	print (type(sequence))
	
	for exon in exons:
		exon_data = (get_exon_sequence(sequence, exon))
		print ('Exon ', exon_data[0])
		print ('Start ', exon_data[1])	
		print ('End ', exon_data[2])
		print ('Sequence ', exon_data[3])			
		
		print (' ')
	
	"""
	
	
	
		
if __name__ =='__main__':
	main()


	
	
	
	
	