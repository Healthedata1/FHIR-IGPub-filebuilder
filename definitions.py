#! /usr/bin/env python3.7

# create ig definition file with all value sets in the /resources directory
import json, os, sys, logging, re, csv, ig_templates as ig
import rR_dict as r
from lxml import etree
from pdb import set_trace as bp
#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.info('Start of program')
logging.info('The logging module is working.')
# create the ig.json file template as dictoinary

logging.info('create the ig.json file template as dictionary')

# globals
igpy = {}
root_dir = os.getcwd() + '/' # current root_dir
logging.info('root dir = ' + root_dir)

try:
    source_dir =  '../{}/'.format(sys.argv[1])  # current source_dir
except IndexError:  # current root_dir
    source_dir = ''

logging.info('relative address of source_dir = ' + source_dir)

# the following paths are defined in the definitions file and the order for this is important - resources path is assumed to be the first item and examples the second see below
resources_path = root_dir  # initializes to root
examples_path = root_dir
pages_path = root_dir
# Function definitions here

def init_igpy():
    # read  non array csv file
    global igpy
    try:
        defn_csv = '{}definitions.csv'.format(source_dir) # if csv in external directory
    except IndexError:
        defn_csv = 'definitions.csv'  # in root
    logging.info('definitions.csv file is at: {}'.format(defn_csv))
    with open(defn_csv) as defnfile:  # grab a 2 column CSV file and cycle through to update igpy
        reader = csv.reader(defnfile, dialect='excel')
        next(defnfile) # header
        tabs_def = next(reader)

        if tabs_def[0] == 'onlyJson':
            igpy = ig.igpy2 if tabs_def[1]=="TRUE" else ig.igpy  # choose which template to use based on first row item 'onlyJson'
        else:
            raise SystemExit('Need to add "onlyJson,TRUE|FALSE" to first row of definitions.csv!!  (see IG-Template2 for exmmple)')
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
                        igpy[row_key0][row_key1].append(itemz)
                        logging.info('updating ig.json with this: { "' + row_key0 + '" { "' + row_key1 + '": ["' + itemz + '",...] } }')

                except IndexError: # unnested dict elements
                    # deal with lists first : append csv element to dict value
                    for (itemz) in (row[1].split('|')):  # loop over list of dependencies
                        try:  # deal with lists first : append csv element to dict value
                            igpy[row[0]].append(itemz)
                            logging.info('updating ig.json with this:  { "' + row[0] + '": [..."' + itemz + '",...] }')
                        except (AttributeError, KeyError):  # simple key value pairs
                            igpy[row[0]] = itemz  # add/replace csv element to existing dict file
                            logging.info('updating ig.json with this:  { "' + row[0] + '": "' + itemz + '" }')
                except AttributeError: # nested dict elements
                    # todo - deal with nested list elements
                    igpy[row_key0][row_key1] = row[1] # add/replace csv element to existing dict fil
                    logging.info('updating ig.json with this: { "' + row_key0 + '" { "' + row_key1 + '": "' + row[1] + '" } }')
                except TypeError: # unnested list of objects
                    for (item,itemz) in enumerate(row[1].split('|')):  # loop over list of dependencies
                        try:
                            igpy[row_key0][item][row_key1]=itemz # create an object for each item in cell
                        except IndexError:
                            igpy[row_key0].append({row_key1:itemz}) # create an object for each item in cell
                        logging.info('updating ig.json with this: { "' + row_key0 + '"[' + str(item) + ']' +':{ "' + row_key1 + '": "' + itemz + '",... }')

    return

def scrub_igpy():  #scrub any rows that are blank.
    igpy_copy = igpy
    Empteez = ['',[],None,{},[{}]]
    for k in list(igpy):
        if igpy[k] in Empteez:
            logging.info("element {} is empty!".format(k))
            del igpy_copy[k]
    return(igpy_copy)


def make_op_frag(frag_id):  # create [id].md file for new operations

    # check if files already exist before writing files
    frag = '{}/_includes/{}-example.md'.format(pages_path, frag_id)
    fragf = open('{frag}'.format(frag=frag), 'w')
    fragf.write('source: _includes/{frag_id}-example.md file\n{frag_text}'.format(frag_id=frag_id, frag_text=ig.op_frag))
    logging.info('added opdef fragment file: {frag}'.format(frag=frag))
    fragf.close()
    return


def make_frags(frag_id):  # create [id]-intro.md, [id]-search.md turned off [id]-diff2.md  [id]-summary.md files since not supported for now
    frags = ['intro', 'search']
    for f in frags:
        frag = '{}/_includes/{}-{}.md'.format(pages_path, frag_id, f)
        if not os.path.exists(frag):  # check if files already exist before writing files
            fragf = open(frag, 'w')
            fragf.write('{}'.format(getattr(ig, f)))
            logging.info('added file: {}'.format(frag))
            fragf.close()
    return

def update_sd(i, type, logical):
    namespaces = {'o': 'urn:schemas-microsoft-com:office:office',
                  'x': 'urn:schemas-microsoft-com:office:excel',
                  'ss': 'urn:schemas-microsoft-com:office:spreadsheet', }
    igpy['spreadsheets'].append(i)
    logging.info('cwd = ' + root_dir)
    logging.info('adding ' + i + ' to spreadsheets array')
    sd_file = open('{}/{}'.format(resources_path,i))  # for each spreadsheet in /resources open value and read  SD id and create and append dict struct to definiions file
    sdxml = etree.parse(sd_file)  # lxml module to parse excel xml
    if logical:
        sdid = sdxml.xpath('/ss:Workbook/ss:Worksheet[2]/ss:Table/ss:Row[2]/ss:Cell[2]/ss:Data',                       namespaces=namespaces)  # use xpath to get the id from the spreadsheet sheet2 "metadata" row2 column2" and retain case
        temp_id = sdid[0].text
        update_igxml('StructureDefinition','logical' , temp_id) # add to ig.xml as an SD  TODO update the pages directory
    else:
        sdid = sdxml.xpath('/ss:Workbook/ss:Worksheet[2]/ss:Table/ss:Row[11]/ss:Cell[2]/ss:Data',
                       namespaces=namespaces)  # use xpath to get the id from the spreadsheet sheet2 "metadata" row11  column2" and lower case
        temp_id = sdid[0].text.lower()
        update_igxml('StructureDefinition','conformance', temp_id) # add to ig.xml as an SD
    update_igjson(type, temp_id) # add base to definitions file
    update_igjson(type, temp_id, 'defns') # add base to definitions file
    logging.info('looking for file = {}/_includes/{}-intro.md'.format(pages_path, temp_id))
    make_frags(temp_id)
    sd_file.close()
    return

def make_title(title): # strip Type and make title case
    new_title = []
    for word in title.split('-'):
        if word.lower() not in r.r_list:
            if any(x.isupper() for x in word):
                new_title.append(word)
            else:
                new_title.append(word.capitalize())
        else:
            new_title.append(r.r_map[word.lower()])
    return(' '.join(new_title))


def update_igxml(type, purpose, id):
    logging.info('++++++++id = {id}'.format(id=id))
    ev = 'false'
    kind = 'resource'
    generation = 'generated'
    if purpose == "example":
        ev = 'true'
        kind = 'example'

    #################################
    if igpy['version'] in ['1.0.2','3.0.1']:
        vsxml_1 = '<resource><example value="{ev}"/><sourceReference><reference value="{type}/{id}"/></sourceReference></resource>'.format(ev=ev,type=type,id=id)  # concat id into appropriate string for resourceType
        vsxml_2 =   '<page><source value="{type}-{id}.html"/><title value="{type} {title}"/><kind value="{kind}"/></page>'.format(type=type,id=id,title=make_title(id),kind=kind)  # add resource to ig resource  # concat id into appropriate string for page

    else:
        vsxml_1 = '<resource><reference><reference value="{type}/{id}"/></reference><exampleBoolean value="{ev}"/></resource>'.format(ev=ev,type=type,id=id)  # concat id into appropriate string
        vsxml_2 =   '<page><nameUrl value="{type}-{id}.html"/><title value="{type} {title}"/><generation value="{generation}"/></page>'.format(type=type,id=id,title=make_title(id),generation=generation)  # add resource to ig resource  # concat id into appropriate string for page
    ################################


    # global ig.igxml
    # add resources
    ig.igxml = ig.igxml.replace('<!-- insert resources -->','<!-- insert resources -->{vsxml}'.format(vsxml=vsxml_1))  # add resource to ig resource
    logging.info('adding {type} {vsxml} to resources in ig.xml'.format(type=type, vsxml=vsxml_1))
    # add pages
    if kind == 'resource':
        if 'extension' in id.lower():
            ig.igxml = ig.igxml.replace('<!-- insert extensions -->','<!-- insert extensions -->{vsxml}'.format(vsxml=vsxml_2))  # add extensions to ig resource
        elif type.lower() == 'structuredefinition':
            ig.igxml = ig.igxml.replace('<!-- insert profiles -->','<!-- insert profiles -->{vsxml}'.format(vsxml=vsxml_2))  # add profiles to ig resource
        else:
            ig.igxml = ig.igxml.replace('<!-- insert {type}s -->'.format(type=type.lower()),'<!-- insert {type}s -->{vsxml}'.format(type=type.lower(), vsxml=vsxml_2))  # add other conformnance resources to ig resource


    logging.info('adding {type} {vsxml} to pages in ig.xml'.format(type=type, vsxml=vsxml_2))




    return()


def update_igjson(type, id, template = 'base', filename = "blah"): # add base to ig.json - can extend for other templates if needed with extra 'template' param
    if template == 'base':
        igpy['resources'][type + '/' + id] = {
            template : type + '-' + id + '.html'}  # concat id into appropriate strings and add valuset base def to resources in def file
        logging.info('adding ' + type + ' ' + id + ' base to resources ig.json')

    if template == 'source':
        igpy['resources'][type + '/' + id][template] =  filename  # concat filename + xml into appropriate strings and add source in def file
        logging.info('adding ' + id + ' source filename to resources ig.json')

    if template == 'defns':
        igpy['resources'][type + '/' + id][template] = type + '-' + id + '-definitions.html'  # concat id into appropriate strings and add sd defitions to in def file
        logging.info('adding ' + type + ' ' +  id  + ' definitions to resources ig.json')
    return


def update_def(filename, type, purpose):  # read either json or xml and update the definitions files
    vsid_re = re.compile(r'<id value="(.*)" */>')  # regex for finding the index in vs
    with open('{}/{}'.format(resources_path, filename), 'r') as f:  # load xml or json file and update string metadata variables and url
        logging.info('file = {}'.format(filename))
        if 'json' in filename:  # open, read id and create and append dict struct to definitions file
            vsjson = json.load(f)  # convert to dict
            logging.info('file = {}'.format(json.dumps(vsjson)))
            vsid = vsjson['id']
        else:  # process as xml using regex
            vsxml = f.read()  # convert to string
            logging.info('file = {}'.format(vsxml))
            vsmo = vsid_re.search(vsxml)  # get match object which contains id
            vsid = vsmo.group(1)  # get id as string
        '''  think this is trying to add publisher and url to conformance files
        try:
            vsxml = vsxml.format(id_value = vsid, res_type = type, **igpy)  # add title, publisher etc to ig.xml and url to conformance resources xml file
            logging.info('updating {} to insert variables for publisher and urls and status = {}'.format(filename, vsxml))
        except KeyError:
            pass
    with open('{}/{}'.format(resources_path, filename), 'w') as f:  # overwrite xml file with updated file
        f.write(vsxml)
    '''
    update_igjson(type, vsid)  # add base to definitions file
    update_igjson(type, vsid, 'source', filename)  # add source filename to definitions file
    if type == 'StructureDefinition':
      update_igjson(type, vsid, 'defns')  # add base to definitions file
      make_frags(vsid)
    if type == 'OperationDefinition':
      logging.info('looking for file = {}/_includes/{}-intro.md'.format(pages_path, vsid))
      if not os.path.exists('{}/_includes/{}-example.md'.format(pages_path, vsid)):  # if file is missing then create new page fragments for extension
        make_op_frag(vsid)
    update_igxml(type, purpose, vsid)
    return


def update_example(type, id, filename):
    update_igxml(type, 'example', id)  # add example to ig.xml file
    update_igjson(type, id)  # add example base to definitions file
    update_igjson(type, id,'source', filename) # add source filename to definitions file
    igpy['defaults'][type] = {'template-base': 'ex.html'}  # add example template for type
    logging.info('adding example ' + filename + ' template to type ' +type + ' in ig.json')
    return


def get_file(e):
    ex_file = open('{}/{}'.format(examples_path, e))  # for each example in /examples open
    logging.info('load example xml file {}/{}'.format(examples_path, e))
    return ex_file


def main():
    global ippy
    global resources_path
    global examples_path
    global pages_path

    igjson = init_igpy()  # read CSV file and update the configuration data
    # global ig.igxml
    # get path for resources and examples which are defined in the definitions file and the order for this is important - resources path is assumed to be the first item and examples the second, the source pages the second item in the list as well. ( the first item is path to the static template pages and assets )
    try:  # if source = argv[1] is external directory then need to update ig.json
        resources_path = '{}{}source/resources'.format(root_dir, source_dir)
        examples_path = '{}{}source/examples'.format(root_dir, source_dir)
        pages_path = '{}{}source/pages'.format(root_dir, source_dir)

        '''
        global resources_path

        resources_path = os.path.join('../{}/source/resources'.format(sys.argv[1]), igpy['paths']['resources'][0])
        global examples_path
        examples_path = os.path.join(igpy['igtemplate-dir'], igpy['paths']['resources'][1])
        global pages_path
        pages_path = os.path.join(igpy['igtemplate-dir'], igpy['paths']['pages'][1], '_includes')
        '''

    except IndexError:
        pass
        resources_path = '{}source/resources'.format(root_dir)
        examples_path = '{}source/examples'.format(root_dir)
        pages_path = '{}source/pages'.format(root_dir)

    logging.info('source resources path = ' + resources_path)
    logging.info('source examples path = ' + examples_path)
    logging.info('source pages path = ' + pages_path)

    #################################
    try:   # allow for multiple contacts
        contact_list = ""
        for i in igpy['contact']:
            contact_list = '{}\n{}'.format(contact_list,ig.contact_item.format(**i))

    except KeyError:
        contact_list = ig.contact_item.format(**igpy)
    logging.info('contact list = ' + contact_list)

    if igpy['version'] in ['1.0.2','3.0.1']:
        ig.igxml = ig.igxml.format(contact_list=contact_list ,**igpy)  # add title, publisher etc to ig.xml

    else:
        igpy['name'] = igpy['title'].replace(' ','')# make name PascalCase assuming no other special character other that spaces
        ig.igxml = ig.igxml2.format(contact_list=contact_list,**igpy)  # add title,name, publisher etc to ig.xml



    ################################

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
    for extension in igpy['extensions']:
        update_igjson('StructureDefinition', extension, 'base')
        update_igjson('StructureDefinition', extension, 'defns')
        update_igxml('StructureDefinition','conformance' , extension) # add to ig.xml as an SD

        logging.info('looking for file = {}/_includes/{}-intro.md'.format(pages_path, extension))
        make_frags(extension)
    # add spreadsheet search parameters
    for search in igpy['searches']:
       update_igjson('SearchParameter', search, 'base')
    # add spreadsheet code systems
    for codesystem in igpy['codesystems']:
       update_igjson('CodeSystem', codesystem, 'base')
       update_igjson('ValueSet', codesystem, 'base')
    # add spreadsheet valuesets
    for valueset in igpy['valuesets']:
       update_igjson('ValueSet', valueset, 'base')
    # add spreadsheet structuremaps
    for structuremap in igpy['structuremaps']:
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

# write ig.json
def write_igjson(path, igjson):
    ig_file = open('{}ig.json'.format(path), 'w')
    ig_file.write(json.dumps(igjson))  # convert dict to json and replace ig.json with this file
    ig_file.close()
    return

# write ig.mxl
def write_igxml(path, igxml):
    ig_file = open('{}/ig.xml'.format(path), 'w')
    ig_file.write(igxml)  # replace ig.xml with this file
    ig_file.close()
    return


# edit front matter for sd.html - bypass this since not needed
def edit_frontmatter(path, igpy):
    pass
    '''
    logging.info('mappings = {}'.format(igpy['mappings']))
    with open('{}/sd.html'.format(path), 'r') as f:
        newline = []  # create new copy
        for line in f:
            line = line.replace('mappings: true', 'mappings: {}'.format(igpy['mappings']))  ## Replace the keyword while you copy.
            line = line.replace('allviews: true', 'allviews: {}'.format(igpy['allviews']))
            newline.append(line)  # Replace the keyword while you copy.
            logging.info('appended this line to copy {}'.format(line))
    with open('{}/sd.html'.format(path), 'w') as f:
        f.writelines(newline)  # replace sd.html with new copy
    '''
    return

#  main

if __name__ == '__main__':
    main()


    logging.info('ig.xml now looks like : ' + ig.igxml)
    # replace ig.xml with this file - write files and copy to source directory
    write_igxml(resources_path,ig.igxml)
    # scrub empty fields out of ig.exjson
    igpy = scrub_igpy()
    logging.info('ig.json now looks like : ' + json.dumps(igpy))
    try:
        write_igjson(source_dir,igpy)  # copy to source directory
    except IndexError:
        pass

    # update sd.html in root_dir if needed

    edit_frontmatter(root_dir, igpy)


    # update ig.json in root
    igpy['paths']['resources'][0] = '{}source/resources'.format(source_dir) # needs to be 1 element
    igpy['paths']['resources'][1] = '{}source/examples'.format(source_dir) # needs to be 2 element, 1st is resource files
    igpy['paths']['pages'][1] = '{}source/pages'.format(source_dir)# needs to be 2 element, 1st is static framework files

    write_igjson(root_dir,igpy)

    logging.info('End of program')
