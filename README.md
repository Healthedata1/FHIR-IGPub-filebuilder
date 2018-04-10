# FHIR-IGPub-filebuilder

This reads from the resource and example directory and definitions.csv file to creates two files called ig.json and ig.xml needed to run the [FHIR ig Publisher](http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation)

to run from command line:

  
run definitions maker with optional source directory name as first argument

  python3.5 ${path}definitions.py {path/SOURCE}

if no source directory if provided will look for the the definitions.csv and source files in the current directory


Assumptions and Preconditions:

source directory needs to have a definitions.csv file ( an example is provided above )  **which should be modified in a text editor and not excel** (unless you import and export the data) since excel will mess it up.

Needs to be python 3.5 (not sure about 3.6)

templates: `ig_template.py` needs to be in local directory



'requirements.txt' - contains list of external libraries

screenhots.. todo
