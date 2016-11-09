import xml.etree.ElementTree as ET

tree = ET.parse('LRG_241.xml')

root = tree.getroot()

print(root)


	
for fixed in root.findall('fixed_annotation'):
	sequence = fixed.find('sequence').text
	trans = fixed.get('transcript')
	print (sequence) 
	
"""
for exon in root.findall('fixed_annotation/transcript/exon'):
	print (exon.attrib)
	for coordinates in root.findall ('fixed_annotation/transcript/exon/coordinates'):
		print (coordinates.attrib)

	exons = fixed.findall('coordinates')
	
	for coordinates in exons:
		print (coordinates.attrib, coordinates.tag)
	
	"""
	
for exon in root.findall('fixed_annotation/transcript/exon'):
	print (exon.attrib)
	list_of_coord = exon.findall('coordinates')
	
	print (list_of_coord[0].attrib)