import sys
import os
import xml.etree.ElementTree as XMLTree
    
def stringify_attributes(attribs, sep):
    s = ""
    for atrib in attribs:
        s += str(atrib) + sep
    s = s[:-1] # remove the final separator from the string
    s+="\n"
    return s
        
def write_csv_line(f,attribs, sep):
    csv_string = stringify_attributes(attribs,sep)
    f.write(csv_string)

def write_intial_csv_line(csvfile, sep):
	elems = ["Block_Number", "Trial Number", "Item ID" ,"Item Number", "Line ID", "Line Number", "Line_Y_Coordinate", "Token_StartX", "Token_EndX", "Token"]
	s = stringify_attributes(elems, sep)
	csvfile.write(s)


def parse_xml_file(csvfile, listfile, fname,Block_Number):
	trial_number = 0
	line_number = 0
	line_y_coord = 0
	line_id = 0
	token_startX = 0
	token_endX = 0
	item_number = 0
	item_id = ''
	token = ''
	
	tree = XMLTree.parse(fname)
	root = tree.getroot()

	for elem in root.iter():
	    if elem.tag == 'trial':
	        trial_number +=1
	        item_number = 0
	        line_number = 0
	    if elem.tag == 'item':
	        item_number +=1
	        item_id = elem.attrib['id']
	        line_number = 0
	    if elem.tag == 'line':
	        line_number +=1
	        line_id +=1
	        line_y_coord = elem.attrib['Y']
	    if elem.tag == 'token':
	        token_startX = elem.attrib['S']
	        token_startY = elem.attrib['E']
	        token = elem.text.strip()
	        #print(token)
	        write_csv_line(csvfile,[Block_Number,trial_number, item_id,item_number, line_id, line_number, line_y_coord, token_startX, token_startY, token], separator)
	        listfile.write(str(token) + "\n")


if len(sys.argv) < 2:
	raise('No filename provided to look for the xml file!')
	sys.exit(1)

xml_fname = sys.argv[1]

if len(sys.argv) >=3:
	results_basename = sys.argv[2]
else:
	results_basename = "Tokens"

if len(sys.argv)>=4:
	separator = sys.argv[3]
else:
	separator = "\t"

# create the files! - could do error handling
csvfile = open(results_basename+'_datafile.csv', 'a+')
listfile = open(results_basename +'_list.txt', 'a+')

write_intial_csv_line(csvfile, separator)

splits = xml_fname.split('.') # check it's not already an xml filename
if len(splits) > 1 and splits[-1] == 'xml':
	parse_xml_file(csvfile, listfile, xml_fname)
else:
	block_number = 0	
	for subdir, dirs, files in os.walk(xml_fname):	
		for file in files:
			splits = file.split('.')
			if splits[-1] == 'xml':
				block_number +=1
				print("Parsing file: " + str(file) + " " + str(block_number))
				filepath = subdir + os.sep + file
				parse_xml_file(csvfile, listfile, filepath, block_number)

print("All files parsed!")

csvfile.close()
listfile.close()