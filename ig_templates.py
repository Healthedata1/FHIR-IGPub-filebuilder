#! /usr/bin/env python3.5

''' this is the definitions file skeleton you need to modify as needed see ig publisher documenentation at  http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation or more information. NOTE the if the dependencyList is empty then a "Property error" is generated.'''

igpy = {
  "npm-name": "healthedatainc.igtemplate",
  "broken-links": None,
  "canonicalBase": "http://www.fhir.org/guides/test",
  "defaults": {
      "Any": {
          "template-base": "base.html",
          "template-format": "format.html",
          "swagger" : "true"
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
  "jurisdiction": "",
  "license": "CC0-1.0",
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
  "name":"",
  "status": "draft",
  "publisher": "Health eData Inc",
  "pub_url": "ehaas@healthedatainc.com",
  "extensions": [],
  "searches": [],
  "codesystems": [],
  "valuesets": [],
  "structuremaps": [],
  "working-dir": None,
  "logging":[],
  "topofpage": "true",
  "allviews": "true",
  "mappings": "true",
  "swagger" : [{
  "mode" : "single",
  "capabilities" : "server",
 }]
}


''' this is the ig.xml as string file skeleton may need to modify as needed see ig publisher documenentation at  f http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation or more information. The Cap Case words are variables that are replaced by variables in the definitions file'''

igxml ='''<?xml version="1.0" encoding="UTF-8"?>
<!--Hidden IG for de facto IG publishing-->
<ImplementationGuide xmlns="http://hl7.org/fhir">
  <id value="ig"/>
  <url value="{canonicalBase}/ImplementationGuide/ig"/>
  <name value="{title}"/>
  <status value="{status}"/>
  <experimental value="true"/>
  <publisher value="{publisher}"/>
  <package>
    <name value="base"/>
<!-- <resource>   1..* Resource in the implementation guide -->
<!--   <example value="[boolean]"/> 1..1 If not an example, has its normal meaning -->
<!--   <name value="[string]"/> 0..1 Human Name for the resource -->
<!--   <description value="[string]"/> 0..1 Reason why included in guide -->
<!--   <acronym value="[string]"/> 0..1 Short code to identify the resource -->
<!--   <source[x]>1..1 uri|Reference(Any) Location of the resource </source[x]> -->
<!--    <exampleFor> 0..1 Reference(StructureDefinition) Resource this is an example of (if applicable) </exampleFor> -->
<!-- </resource> -->
    <!-- insert resources -->
  </package>
  <page>
    <source value="index.md"/>
    <title value="{title} Homepage"/>
    <kind value="page"/>
  </page>
</ImplementationGuide>'''

igxml2='''<?xml version="1.0" encoding="UTF-8"?>
<!--Hidden IG for de facto IG publishing-->
<ImplementationGuide xmlns="http://hl7.org/fhir">
  <id value="ig"/>
  <url value="{canonicalBase}/ImplementationGuide/ig"/>
  <version value="{fixed-business-version}"/>
  <name value="{name}"/>
  <title value="{title}"/>
  <status value="{status}"/>
  <publisher value="{publisher}"/>
  <copyright value="Used by permission of {publisher}, all rights reserved Creative Commons License"/>
  <!-- 0..1 Use and/or publishing restrictions -->
 <packageId value="{npm-name}"/> <!-- 0..1 NPM Package name for IG -->
<license value="CC0-1.0"/> <!--*****HARDCODED********* 0..1 SPDX license code for this IG (or not-open-source) -->
<fhirVersion value="{version}"/> <!-- 0..1 FHIR Version this Implementation Guide targets -->
 <definition>
<!--  <package> --> <!-- 0..* Grouping used to present related resources in the IG -->
<!--   <name value="[string]"/> --> <!-- 1..1 Descriptive name for the package -->
<!--   <description value="[string]"/> --><!-- 0..1 Human readable text describing the package -->
<!-- </package> -->

    <package>
      <name value="base"/>
    </package>

     <!-- <resource>
       <reference>
             <reference value="[type]/[id]"/>
       </reference>
       <name value="Test Example"/>
       <description value="A test example to show how a implementation guide works"/>
       <exampleCanonical value="http://hl7.org/fhir/us/core/StructureDefinition/patient"/>|<exampleBoolean value="true|false"/>
    </resource>   -->

    <!-- insert resources -->
    <page>
      <nameUrl value="index.md"/>
      <title value="{title} Homepage"/>
      <generation value="markdown"/>
    </page>
  </definition>
</ImplementationGuide>
'''


# default content for files
intro = '''
{% assign id = {{page.id}} %}
source file: source/pages/\_includes/{{id}}-intro.md

{{site.data.structuredefinitions.[id].description}}

#### Scope and Usage

scope and usage text here

#### Mandatory Data Elements and Terminology

The following data-elements are mandatory (i.e data MUST be present). blah blah blah

**must have:**

1. blah
1. blah
1. blah

**Additional Profile specific implementation guidance:**

#### Examples

- list examples here
'''
search = '''
{% assign id = {{page.id}} %}
source file: source/pages/\_includes/{{id}}-search.md

~~~
This is the search markdown file that gets inserted into the sd.html Quick Start section for explanation of the search requirements.
~~~
'''

# not used for now
summary = '''
{% assign id = {{page.id}} %}
source file: source/pages/\_includes/{{id}}-summary.md

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
diff2 = '''
<!-- stubbed file need actual file name of diff fragment {% raw %}
{% assign id = {{include.id}} %}
<p><b>Intermediate Differential View ({{include.type}}-{{include.id}} Profile + {{site.data.structuredefinitions.[id].basename}} Profile)</b></p>
<div id="all-tbl-diff2-inner">
  {% include {{include.type}}-argo-clinicalnotes-diff.xhtml %}
</div>
{% endraw %} -->
'''
