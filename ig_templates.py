#! /usr/bin/env python3.5

''' this is the definitions file skeleton you need to modify as needed see ig publisher documenentation at  http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation or more information. NOTE the if the dependencyList is empty then a "Property error" is generated.'''

igpy = {
  "broken-links": "warning",
  "canonicalBase": "http://www.fhir.org/guides/test",
  "defaults": {
      "Any": {
          "template-base": "base.html",
          "template-format": "format.html"
      },
      "CapabilityStatement": {
          "template-base": "base.html"
      },
      "CodeSystem": {
          "template-base": "base.html"
      },
      "ConceptMap": {
          "template-base": "base.html"
      },
      "OperationDefinition": {
          "template-base": "base.html"
      },
      "SearchParameter": {
        "template-base": "base.html"
      },
      "StructureDefinition": {
          "template-base": "sd.html",
          "template-defns": "sd-definitions.html",
          "template-mappings": "sd-mappings.html"
      },
      "StructureMap": {
          "template-base": "ex.html",
          "content": False,
          "script": False,
          "profiles": False
      },
      "ValueSet": {
          "template-base": "base.html"
      }
  },
  "dependencyList": [{}],
  "do-transforms": "false",
  "extraTemplates": [
      "mappings"
  ],
  "fixed-business-version": "0.0.0",
  "gen-examples": "false",
  "html-template": "html-template.html",
  "jurisdiction": "US",
  "no-inactive-codes": "false",
  "paths": {
      "output": "output",
      "pages": [],
      "qa": "qa",
      "resources": [],
      "specification": "http://build.fhir.org",
      "temp": "temp",
      "txCache": "txCache"
  },
  "resources": {},
  "sct-edition": "http://snomed.info/sct/731000124108",
  "source": "ig.xml",
  "special-urls": [],
  "spreadsheets": [],
  "tool": "jekyll",
  "version": "3.1.0",
  "igtemplate-dir": None,
  "title": "Implementation Guide Template",
  "status": "draft",
  "publisher": "Health eData Inc",
  "pub_url": "ehaas@healthedatainc.com",
  "extensions": [],
  "searches": [],
  "codesystems": [],
  "valuesets": [],
  "structuremaps": [],
  "working-dir": None,
  "logging":[]
}


''' this is the ig.xml as string file skeleton may need to modify as needed see ig publisher documenentation at  f http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation or more information. The Cap Case words are variables that are replaced by variables in the definitions file'''

igxml ='''<?xml version="1.0" encoding="UTF-8"?><!--Hidden IG for de facto IG publishing--><ImplementationGuide xmlns="http://hl7.org/fhir"><id value="ig"/><url value="{canonicalBase}/ImplementationGuide/ig"/><name value="{title}"/><status value="{status}"/><experimental value="true"/><publisher value="{publisher}"/><package><name value="base"/></package><page><source value="index.md"/><title value="{title} Homepage"/><kind value="page"/><page><source value="_includes/toc.md"/><title value="{title} Table of Contents"/><kind value="page"/></page></page></ImplementationGuide>'''


# default content for files
intro = '''
    This is the introduction markdown file that gets inserted into the sd.html template.

    This profile sets minimum expectations for blah blah blah

    ##### Mandatory Data Elements and Terminology

    The following data-elements are mandatory (i.e data MUST be present). blah blah blah

    **must have:**

    1. blah
    1. blah
    1. blah

    **Additional Profile specific implementation guidance:**

    #### Examples
'''
srch = '''
    This is the search markdown file that gets inserted into the sd.html Quick Start section for explanation of the search requirements.
'''
sumry = '''
    This is the summary markdown file that gets inserted into the sd.html template. for a more formal narrative summary of constraints.  in future hope to automate this to computer generated code.

    #### Complete Summary of the Mandatory Requirements

    1.
    1.
    1.
'''

# default content for files
op_frag = '''
    This is the  markdown file that gets inserted into the op.html template.
'''
