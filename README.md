# Eyelink_xml_parser
A quick parser for the eyelink xml files containing word stimulus information.

How to use:

On the commandline type: "python eyelink_xml_parser.py "path-to-directory-containing-xml-files" "name-of-results-file-you-want" "csv-file-separator"
  
The last two arguments are optional. By default the name of results file will be "Tokens", and the default csv separator is a tab.

The program will produce two files. The first called $yourname$_datafile.csv is the csv file containing all the important metadata from the xml. The second called $yourname$_list.txt is simply a list of the tokens.
  
The example.R is a minimal example of how to load the csv file into R successfully.

Hope this helps!
