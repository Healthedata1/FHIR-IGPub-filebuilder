# FHIR-IGPub-filebuilder

This reads from the resource and example directory and definitions.csv file to creates two files called ig.json and ig.xml needed to run the [FHIR ig Publisher](http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation)

to run from command line:

`>python3.5 definition.py`

templates: `ig_template.py`

Assumptions and Preconditions:

source directory needs to have a definitions.csv file ( an example is provided above )  **which should be modified in a text editor and not excel** (unless you import and export the data) since excel will mess it up.


Needs to be python 3.5 (not sure about 3.6)

'requirements.txt' - contains list of external libraries

screenhots.. todo
