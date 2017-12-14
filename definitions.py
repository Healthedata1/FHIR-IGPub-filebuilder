#! /usr/bin/env python3.5

# create ig definition file with all value sets in the /resources directory
import json, os, sys, logging, re, csv, ig_templates as ig
from lxml import etree
#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.info('Start of program')
logging.info('The logging module is working.')
# create the ig.json file template as dictoinary

logging.info('create the ig.json file template as dictionary')

# globals

root_dir = os.getcwd() + '/' # current root_dir
logging.info('root dir = ' + root_dir)
# the following paths are defined in the definitions file and the order for this is important - resources path is assumed to be the first item and examples the second see below
resources_path = root_dir  # initializes to root
examples_path = root_dir
pages_path = root_dir
# Function definitions here

def init_igpy():
    # read  non array csv file
    with open('definitions.csv') as defnfile:  # grab a 2 column CSV file and cycle through to update igpy
        reader = csv.reader(defnfile, dialect='excel')
        next(defnfile)
        for row in reader:  # each row equal row of 2 column csv file as ignoring  header
            logging.info('k,v = {}, {}'.format(row[0],row[1]))  # row[0] = row[0] and row[1] = row[row-key]
            if row[1] == 'FALSE' or row[1] == 'TRUE':  # clean up excel propensity to change the string true/false to TRUE/FALSE
                row[1] = row[1].lower()
            if row[1] != "":  # ignore blank rows
                try: # deal with nested elements first
                    row_key0 = row[0].split(".")[0]
                    row_key1 = row[0].split(".")[1]
                    # deal with lists first : append csv element to dict value
                    for itemz in row[1].split('|'):
                        ig.igpy[row_key0][row_key1].append(itemz)
                        logging.info('updating ig.json with this: { "' + row_key0 + '" { "' + row_key1 + '": ["' + itemz + '",...] } }')

                except IndexError: # unnested dict elements
                    # deal with lists first : append csv element to dict value
                    for (itemz) in (row[1].split('|')):  # loop over list of dependencies
                        try:  # deal with lists first : append csv element to dict value
                            ig.igpy[row[0]].append(itemz)
                            logging.info('updating ig.json with this:  { "' + row[0] + '": [..."' + itemz + '",...] }')
                        except AttributeError:  # simple key value pairs
                            ig.igpy[row[0]] = itemz  # add/replace csv element to existing dict file
                            logging.info('updating ig.json with this:  { "' + row[0] + '": "' + itemz + '" }')
                except AttributeError: # nested dict elements
                    # todo - deal with nested list elements
                    ig.igpy[row_key0][row_key1] = row[1] # add/replace csv element to existing dict fil
                    logging.info('updating ig.json with this: { "' + row_key0 + '" { "' + row_key1 + '": "' + row[1] + '" } }')
                except TypeError: # unnested list of objects
                    for (item,itemz) in enumerate(row[1].split('|')):  # loop over list of dependencies
                        try:
                            ig.igpy[row_key0][item][row_key1]=itemz # create an object for each item in cell
                        except IndexError:
                            ig.igpy[row_key0].append({row_key1:itemz}) # create an object for each item in cell
                        logging.info('updating ig.json with this: { "' + row_key0 + '"[' + str(item) + ']' +':{ "' + row_key1 + '": "' + itemz + '",... }')
    # check if dependencyList is empty since this will lead to error GF#
    if ig.igpy['dependencyList'] == [{}]:
        logging.info("dependencyList is empty!")
        del ig.igpy['dependencyList']
    return

def make_op_frag(frag_id):  # create [id].md file for new operations

    # check if files already exist before writing files
    frag = '{}/{}'.format(pages_path, frag_id)
    fragf = open(frag + '.md', 'w')
    fragf.write('source: {}.md file\n{}'.format(frag_id, ig.op_frag))
    logging.info('added file: ' + frag + '.md')
    fragf.close()
    return

def make_frags(frag_id):  # create [id]-intro.md, [id]-search.md and [id]-summary.md files

    # check if files already exist before writing files
    frag = '{}/{}'.format(pages_path, frag_id)
    fragf = open(frag + '-intro.md', 'w')
    fragf.write('source: {}.md file\n{}'.format(frag_id, ig.intro))
    logging.info('added file: ' + frag + '-intro.md')
    fragf.close()
    fragf = open(frag + '-summary.md', 'w')
    fragf.write('source: {}.md file\n{}'.format(frag_id, ig.sumry))
    logging.info('added file: ' + frag + '-summary.md')
    fragf.close()
    fragf = open(frag + '-search.md', 'w')
    fragf.write('source: {}.md file\n{}'.format(frag_id, ig.srch))
    logging.info('added file: ' + frag + '-search.md')
    fragf.close()
    return

def update_sd(i, type, logical):
    namespaces = {'o': 'urn:schemas-microsoft-com:office:office',
                  'x': 'urn:schemas-microsoft-com:office:excel',
                  'ss': 'urn:schemas-microsoft-com:office:spreadsheet', }
    ig.igpy['spreadsheets'].append(i)
    logging.info('cwd = ' + root_dir)
    logging.info('adding ' + i + ' to spreadsheets array')
    sd_file = open('{}/{}'.format(resources_path,i))  # for each spreadsheet in /resources open value and read  SD id and create and append dict struct to definiions file
    sdxml = etree.parse(sd_file)  # lxml module to parse excel xml
    if logical:
        sdid = sdxml.xpath('/ss:Workbook/ss:Worksheet[2]/ss:Table/ss:Row[2]/ss:Cell[2]/ss:Data',                       namespaces=namespaces)  # use xpath to get the id from the spreadsheet sheet2 "metadata" row2 column2" and retain case
        temp_id = sdid[0].text
        update_igxml('StructureDefinition','logical' , temp_id) # add to ig.xml as an SD
    else:
        sdid = sdxml.xpath('/ss:Workbook/ss:Worksheet[2]/ss:Table/ss:Row[11]/ss:Cell[2]/ss:Data',
                       namespaces=namespaces)  # use xpath to get the id from the spreadsheet sheet2 "metadata" row11  column2" and lower case
        temp_id = sdid[0].text.lower()
    update_igjson(type, temp_id) # add base to definitions file
    update_igjson(type, temp_id, 'defns') # add base to definitions file
    if not os.path.exists('{}/{}-intro.md'.format(pages_path, temp_id)):  # if intro fragment is missing then create new page fragments for extension
        make_frags(temp_id)
    sd_file.close()
    return

def update_igxml(type, purpose, id):
    ev = 'false'
    if purpose == "example":
        ev = 'true'
    vsxml = '<resource><example value="' + ev + '"/><sourceReference><reference value="' + type + '/' + id + '"/></sourceReference></resource>'  # concat id into appropriate string
    # global ig.igxml
    ig.igxml = ig.igxml.replace('name value="base"/>',
                            'name value="base"/>' + vsxml)  # add valueset base def to ig resource
    logging.info('adding ' + type + vsxml + ' to resources in ig.xml')
    return

def update_igjson(type, id, template = 'base', filename = "blah"): # add base to ig.json - can extend for other templates if needed with extra 'template' param
    if template == 'base':
        ig.igpy['resources'][type + '/' + id] = {
            template : type + '-' + id + '.html'}  # concat id into appropriate strings and add valuset base def to resources in def file
        logging.info('adding ' + type + ' ' + id + ' base to resources ig.json')

    if template == 'source':
        ig.igpy['resources'][type + '/' + id][template] =  filename  # concat filename + xml into appropriate strings and add source in def file
        logging.info('adding ' + id + ' source filename to resources ig.json')

    if template == 'defns':
        ig.igpy['resources'][type + '/' + id][template] = type + '-' + id + '-definitions.html'  # concat id into appropriate strings and add sd defitions to in def file
        logging.info('adding ' + type + ' ' +  id  + ' definitions to resources ig.json')
    return


def update_def(filename, type, purpose):
    vsid_re = re.compile(r'<id value="(.*)"/>')  # regex for finding the index in vs
    with open('{}/{}'.format(resources_path, filename), 'r') as f:  # load xml file and update string metadata variables and url
        vsxml = f.read()  # convert to string
        logging.info('file = {}'.format(filename))
        vsmo = vsid_re.search(vsxml)  # get match object which contains id
        vsid = vsmo.group(1)  # get id as string
        try:
            vsxml = vsxml.format(id_value = vsid, res_type = type, **ig.igpy)  # add title, publisher etc to ig.xml and url to conformance resources xml file
            logging.info('updating {} to insert variables for publisher and urls and status = {}'.format(filename, vsxml))
        except KeyError:
            pass
    with open('{}/{}'.format(resources_path, filename), 'w') as f:  # overwrite xml file with updated file
        f.write(vsxml)
    update_igjson(type, vsid)  # add base to definitions file
    update_igjson(type, vsid, 'source', filename)  # add source filename to definitions file
    if type == 'StructureDefinition':
      update_igjson(type, vsid, 'defns')  # add base to definitions file
      if not os.path.exists('{}/{}-intro.md'.format(pages_path, vsid)):  # if intro file fragment is missing then create new page fragments for extension
          make_frags(vsid)
    if type == 'OperationDefinition':
      if not os.path.exists('{}/{}.md'.format(pages_path, vsid)):  # if file is missing then create new page fragments for extension
        make_op_frag(vsid)
    update_igxml(type, purpose, vsid)
    return


def update_example(type, id, filename):
    update_igxml(type, 'example', id)  # add example to ig.xml file
    update_igjson(type, id)  # add example base to definitions file
    update_igjson(type, id,'source', filename) # add source filename to definitions file
    ig.igpy['defaults'][type] = {'template-base': 'ex.html'}  # add example template for type
    logging.info('adding example template to type ' +type + ' in ig.json')
    return


def get_file(e):
    ex_file = open('{}/{}'.format(examples_path, e))  # for each example in /examples open
    logging.info('load example xml file {}/{}'.format(examples_path, e))
    return ex_file

def main():
    init_igpy()  # read CSV file and update the configuration data
    # global ig.igxml
    # get path for resources and examples which are defined in the definitions file and the order for this is important - resources path is assumed to be the first item and examples the second, the source pages the second item in the list as well. ( the first item is path to the static template pages and assets )
    try:
        global resources_path
        resources_path = os.path.join(ig.igpy['igtemplate-dir'], ig.igpy['paths']['resources'][0])
        global examples_path
        examples_path = os.path.join(ig.igpy['igtemplate-dir'], ig.igpy['paths']['resources'][1])
        global pages_path
        pages_path = os.path.join(ig.igpy['igtemplate-dir'], ig.igpy['paths']['pages'][1], '_includes')
    except TypeError:
        global resources_path
        resources_path = os.path.join(root_dir, ig.igpy['paths']['resources'][0])
        global examples_path
        examples_path = os.path.join(root_dir, ig.igpy['paths']['resources'][1])
        global pages_path
        pages_path = os.path.join(root_dir, ig.igpy['paths']['pages'][0], '_includes')

    logging.info('source resources path = ' + resources_path)
    logging.info('source examples path = ' + examples_path)
    logging.info('source pages path = ' + pages_path)

    ig.igxml = ig.igxml.format(**ig.igpy)  # add title, publisher etc to ig.xml
    resources = os.listdir(resources_path)  # get all the files in the resource directory
    for i in range(len(resources)):  # run through all the files looking for spreadsheets and valuesets
        if 'spreadsheet' in resources[i]: # for spreadsheets  append to the igpy[spreadsheet] array.
            if 'logical' in resources[i]:  # check if logical model
                logical = True #   these need to be handled differently
            else:
                logical = False
            update_sd(resources[i], 'StructureDefinition', logical) # append to the igpy[spreadsheet] array.
        if ('valueset' in resources[i]) or ('ValueSet' in resources[i]): # for each vs in /resources open valueset resources and read id and create and append dict struct to definiions file
            update_def(resources[i], 'ValueSet', 'terminology')
        if ('codesystem' in resources[i]) or ('CodeSystem' in resources[i]): # for each vs in /resources open valueset resources and read id and create and append dict struct to definiions file
            update_def(resources[i], 'CodeSystem', 'terminology')
        if ('conceptmap' in resources[i]) or ('ConceptMap' in resources[i]):  # for each vs in /resources open valueset resources and read id and create and append dict struct to definiions file
            update_def(resources[i], 'ConceptMap', 'terminology')
        if ('capabilitystatement' in resources[
            i]) or  ('CapabilityStatement' in resources[
                i]): # for each cs in /resources open, read id and create and append dict struct to definiions file
            update_def(resources[i], 'CapabilityStatement', 'conformance')
        if ('operationdefinition' in resources[i]) or ('OperationDefinition' in resources[i]):  # for each cs in /resources open, read id and create and append dict struct to definiions file
            update_def(resources[i], 'OperationDefinition', 'conformance')
        if ('structuredefinition' in resources[i]) or ('StructureDefinition' in resources[i]):  # for each cs in /resources open, read id and create and append dict struct to definitions file
            update_def(resources[i], 'StructureDefinition', 'conformance')
        if ('structuremap' in resources[i]) or ('SructureMap' in resources[i]):  # for each cs in /resources open, read id and create and append dict struct to definiions file
            update_def(resources[i], 'StructureMap', 'conformance')

        if ('searchparameter' in resources[i]) or ('SearchParameter' in resources[i]): # for each cs in /resources open, read id and create and append dict struct to definiions file
            update_def(resources[i], 'SearchParameter', 'conformance')

   # add spreadsheet extensions
    for extension in ig.igpy['extensions']:
        update_igjson('StructureDefinition', extension, 'base')
        update_igjson('StructureDefinition', extension, 'defns')
        logging.info('intro page = {}/{}-intro.md'.format(pages_path, extension))
        if not os.path.exists('{}/{}-intro.md'.format(pages_path, extension)):  # if intro fragment is missing then create new page fragments for extension
            make_frags(extension)
    # add spreadsheet search parameters
    for search in ig.igpy['searches']:
       update_igjson('SearchParameter', search, 'base')
    # add spreadsheet code systems
    for codesystem in ig.igpy['codesystems']:
       update_igjson('CodeSystem', codesystem, 'base')
       update_igjson('ValueSet', codesystem, 'base')
    # add spreadsheet valuesets
    for valueset in ig.igpy['valuesets']:
       update_igjson('ValueSet', valueset, 'base')
    # add spreadsheet structuremaps
    for structuremap in ig.igpy['structuremaps']:
       update_igjson('StructureMap', structuremap, 'base')

    examples = os.listdir(examples_path)  # get all the examples in the examples directory assuming are in json or xml
    for i in range(len(examples)):  # run through all the examples and get id and resource type
        if 'json' in examples[i]:  # for each cs in /resources open, read id and create and append dict struct to definiions file
            exjson = json.load(get_file(examples[i]))
            extype = exjson['resourceType']
            ex_id = exjson['id']
            update_example(extype, ex_id, examples[i])
        if 'xml' in examples[i]:  # for each cs in /resources open, read id and create and append dict struct to definiions file
            ex_xml = etree.parse(get_file(examples[i]))  # lxml module to parse example xml
            ex_id = ex_xml.xpath('//f:id/@value', namespaces={'f': 'http://hl7.org/fhir'})  # use xpath to get the id
            extype = ex_xml.xpath('name(/*)')  # use xpath to get the type '''
            update_example(extype, ex_id[0], examples[i])
    return()

#  main

if __name__ == '__main__':
    main()

    # write files
    ig_file = open('{}/ig.xml'.format(resources_path), 'w')
    ig_file.write(ig.igxml)  # replace ig.xml with this file
    logging.info('ig.xml now looks like : ' + ig.igxml)
    if ig.igpy['igtemplate-dir']:
        root_dir = ig.igpy['igtemplate-dir']  # change to the ig template path name specified in the csv file if present to write to ig.json file in templates file
        logging.info('copying ig.json to: {}'.format(root_dir))
    ig_file = open(root_dir + 'ig.json', 'w')
    ig_file.write(json.dumps(ig.igpy))  # convert dict to json and replace ig.json with this file
    ig_file.close()
    logging.info('ig.json now looks like : ' + json.dumps(ig.igpy))

    logging.info('End of program')
