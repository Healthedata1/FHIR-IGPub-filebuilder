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
      "txCache": "txCache",
      "history": "history"
  },
  "resources": {},
  "sct-edition": "http://snomed.info/sct/731000124108",
  "source": "ig.xml",
  "special-urls": [],
  "spreadsheets": [],
  "bundles": [],
  "tool": "jekyll",
  "version": "",
  "igtemplate-dir": None,
  "title": "Implementation Guide Template",
  "name":"",
  "status": "draft",
  "publisher": "Health eData Inc",
  "contact": [{}],
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
  "swagger" : [{
  "mode" : "single",
  "capabilities" : "server",
 }]
}

igpy2 = {
  "npm-name": "healthedatainc.igtemplate",
  "broken-links": None,
  "canonicalBase": "http://www.fhir.org/guides/test",
  "defaults": {
      "Any": {
          "template-base": "base.html",
          "template-format": "format.html",
          "swagger" : "true",
          "xml": False,
          "ttl": False
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
      "txCache": "txCache",
      "history": "history"
  },
  "resources": {},
  "sct-edition": "http://snomed.info/sct/731000124108",
  "source": "ig.xml",
  "special-urls": [],
  "spreadsheets": [],
  "bundles": [],
  "tool": "jekyll",
  "version": "",
  "igtemplate-dir": None,
  "title": "Implementation Guide Template",
  "name":"",
  "status": "draft",
  "publisher": "Health eData Inc",
  "contact": [{}],
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
  "swagger" : [{
  "mode" : "single",
  "capabilities" : "server",
 }]
}


''' this is the ig.xml as string file skeleton may need to modify as needed see ig publisher documenentation at  f http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation or more information. The Cap Case words are variables that are replaced by variables in the definitions file'''

igxml ='''<?xml version="1.0" encoding="UTF-8"?>
<!--Hidden IG for de facto IG publishing-->
<ImplementationGuide xmlns="http://hl7.org/fhir">
  <id value="{npm-name}"/>
  <url value="{canonicalBase}/ImplementationGuide/{npm-name}"/>
  <version value="{fixed-business-version}"/>
  <name value="{title}"/>
  <status value="{status}"/>
  <experimental value="true"/>
  <publisher value="{publisher}"/>
{contact_list}
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
  <!-- ============ Home Page =============== -->
<page><source value="index.html"/><title value="Home"/><kind value="page"/>

  <!-- ============ Guidance Page =============== -->
  <page><source value="guidance.html"/><title value="General Guidance"/><kind value="page"/></page>

  <!-- ============ Profiles Page =============== -->
  <page><source value="profiles.html"/><title value="Profiles and Extensions"/><kind value="page"/>

     <!-- ============ Profiles and examples=============== -->
     <!-- insert profiles -->
    <!-- ============ End Profiles and examples=============== -->

    <!-- ============ Extensions and examples =============== -->
    <!-- insert extensions -->
    <!-- ============ End Extensions and examples =============== -->

    </page>
  <!-- ============ Operations Page =============== -->
  <page><source value="operations.html"/><title value="Operations"/><kind value="page"/>

    <!-- ============ Operations and examples  =============== -->
    <!-- insert operationdefinitions -->
    <!-- ============ End Operations and examples  =============== -->

  </page>
  <!-- ============ Terminology Page =============== -->

  <page><source value="terminology.html"/><title value="Terminology"/><kind value="page"/>
     <!-- ============ ValueSet   =============== -->
    <!-- insert valuesets -->
    <!-- ============ End ValueSet   =============== -->

    <!-- ============ CodeSystems  =============== -->
    <!-- insert codesystems -->
    <!-- ============ End CodeSystems  =============== -->

    <!-- ============ ConceptMaps   =============== -->
    <!-- insert conceptmaps -->
    <!-- ============ End ConceptMaps   =============== -->

  </page>

  <!-- ============ SearchParameter Page =============== -->
  <page><source value="searchparameters.html"/><title value="Search Parameters"/><kind value="page"/>

  <!-- ============ SearchParameters =============== -->
  <!-- insert searchparameters -->
  <!-- ============ End SearchParameters  =============== -->
  </page>

  <!-- ============ CapabilityStatement Page =============== -->
  <page><source value="capstatements.html"/><title value="Capability Statements"/><kind value="page"/>

  <!-- ============ CapabilityStatements    =============== -->
    <!-- insert capabilitystatements -->
  <!-- ============ End CapabilityStatements    =============== -->

  </page>

  <!-- ============ Security Page =============== -->
  <page><source value="security.html"/><title value="Security"/><kind value="page"/></page>

  <!-- ============ Downloads Page =============== -->
  <page><source value="downloads.html"/><title value="Downloads"/><kind value="page"/></page>

  <!-- ============ Examples Page=============== -->
  <page><source value="all-examples.html"/><title value="All Examples"/><kind value="page"/></page>

  <!-- ============ Table of Contents =============== -->
  <page><source value="toc.html"/><title value="Table of Contents"/><kind value="toc"/></page>

</page>
</ImplementationGuide>'''

igxml2='''<?xml version="1.0" encoding="UTF-8"?>
<!--Hidden IG for de facto IG publishing-->
<ImplementationGuide xmlns="http://hl7.org/fhir">
  <id value="{npm-name}-{fixed-business-version}"/>
  <url value="{canonicalBase}/ImplementationGuide/{npm-name}-{fixed-business-version}"/>
  <version value="{fixed-business-version}"/>
  <name value="{name}"/>
  <title value="{title}"/>
  <status value="{status}"/>
  <publisher value="{publisher}"/>
{contact_list}
  <copyright value="Used by permission of {publisher}, all rights reserved Creative Commons License"/>
  <!-- 0..1 Use and/or publishing restrictions -->
 <packageId value="{npm-name}"/> <!-- 0..1 NPM Package name for IG -->
<license value="CC0-1.0"/> <!--*****HARDCODED********* 0..1 SPDX license code for this IG (or not-open-source) -->
<fhirVersion value="{version}"/> <!-- 0..1 FHIR Version this Implementation Guide targets -->
 <!-- <dependsOn>   0..* Another Implementation guide this depends on
  <uri> 1..1 canonical(ImplementationGuide) Identity of the IG that this depends on </uri>
  <packageId value="[id]"/> 0..1 NPM Package name for IG this depends on
  <version value="[string]"/> 0..1 Version of the IG
 </dependsOn> -->
 <!-- insert dependency -->
 <!-- <global>  0..* Profiles that apply globally
  <type value="[code]"/> 1..1 Type this profile applies to
  <profile> 1..1 canonical(StructureDefinition) Profile that all resources must conform to</profile>
 </global> -->
 <definition>
  <!--  <grouping>  0..* Grouping used to present related resources in the IG -->
  <!-- <name value="[string]"/> 1..1 Descriptive name for the package -->
  <!--   <description value="[string]"/> 0..1 Human readable text describing the package -->
  <!--  </grouping>  -->
    <grouping>
      <name value="base"/>
    </grouping>
    <!-- <resource>
    <reference>
      <reference value="[type]/[id]"/>
    </reference>
    <name value="Test Example"/>
    <description value="A test example to show how a implementation guide works"/>
    <exampleCanonical value="http://hl7.org/fhir/us/core/StructureDefinition/patient"/>|<exampleBoolean value="true|false"/>
  </resource>   -->
  <!--  <groupingId value="[id]"/>  0..1 Grouping this is part of -->
  <!-- insert resources -->

    <!-- ============ Home Page =============== -->
  <page><nameUrl value="index.html"/><title value="Home"/><generation value="markdown"/>

    <!-- ============ Guidance Page =============== -->
    <page><nameUrl value="guidance.html"/><title value="General Guidance"/><generation value="markdown"/></page>

    <!-- ============ Profiles Page =============== -->
    <page><nameUrl value="profiles.html"/><title value="Profiles and Extensions"/><generation value="markdown"/>

     <!-- ============ Profiles and examples=============== -->
     <!-- insert profiles -->
    <!-- ============ End Profiles and examples=============== -->

    <!-- ============ Extensions and examples =============== -->
    <!-- insert extensions -->
    <!-- ============ End Extensions and examples =============== -->

      </page>

     <!-- ============ Bundle Definitions Page =============== -->
     <page><nameUrl value="bundles.html"/><title value="Bundle Definitions"/><generation value="markdown"/>

     <!-- ============ MessagedDefinitions  =============== -->
     <!-- insert messagedefinitions -->
     <!-- ============ End MessagedDefinitions  =============== -->

      <!-- ============ GraphDefinitions  =============== -->
      <!-- insert graphdefinitions -->
      <!-- ============ EndGraphDefinitions  =============== -->

     </page>

    <!-- ============ Operations Page =============== -->
    <page><nameUrl value="operations.html"/><title value="Operations"/><generation value="markdown"/>

    <!-- ============ Operations and examples  =============== -->
    <!-- insert operationdefinitions -->
    <!-- ============ End Operations and examples  =============== -->

    </page>
    <!-- ============ Terminology Page =============== -->

    <page><nameUrl value="terminology.html"/><title value="Terminology"/><generation value="markdown"/>
     <!-- ============ ValueSet   =============== -->
    <!-- insert valuesets -->
    <!-- ============ End ValueSet   =============== -->

    <!-- ============ CodeSystems  =============== -->
    <!-- insert codesystems -->
    <!-- ============ End CodeSystems  =============== -->

    <!-- ============ ConceptMaps   =============== -->
    <!-- insert conceptmaps -->
    <!-- ============ End ConceptMaps   =============== -->

    </page>

    <!-- ============ SearchParameter Page =============== -->
    <page><nameUrl value="searchparameters.html"/><title value="Search Parameters"/><generation value="markdown"/>

  <!-- ============ SearchParameters =============== -->
  <!-- insert searchparameters -->
  <!-- ============ End SearchParameters  =============== -->
    </page>

    <!-- ============ CapabilityStatement Page =============== -->
    <page><nameUrl value="capstatements.html"/><title value="Capability Statements"/><generation value="markdown"/>

  <!-- ============ CapabilityStatements    =============== -->
    <!-- insert capabilitystatements -->
  <!-- ============ End CapabilityStatements    =============== -->
    </page>

    <!-- ============ Security Page =============== -->
    <page><nameUrl value="security.html"/><title value="Security"/><generation value="markdown"/></page>

    <!-- ============ Examples Page=============== -->
    <page><nameUrl value="all-examples.html"/><title value="All Examples"/><generation value="markdown"/></page>

    <!-- ============ Downloads Page =============== -->
    <page><nameUrl value="downloads.html"/><title value="Downloads"/><generation value="markdown"/></page>

    <!-- ============ Table of Contents =============== -->
    <page><nameUrl value="toc.html"/><title value="Table of Contents"/><generation value="html"/></page>

  </page>
  </definition>
</ImplementationGuide>
'''

contact_item = '''
<contact><!-- 0..* ContactDetail Contact details for the publisher -->
    <telecom>
      <system value="{system}"/>
      <value value="{value}"/>
    </telecom>
  </contact>'''

# default content for files
#style 1
xintro = ''' # change var name to 'intro' to use
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
#style2
intro = '''
{% assign base_id = {{page.id}} %}
{% assign base_type = {{site.data.structuredefinitions.[base_id].type}} %}

{{site.data.structuredefinitions.[base_id].description}}

### Mandatory and Must Support Data Elements

The following data-elements are mandatory (i.e data MUST be present) or must be supported if the data is present in the sending system ([Must Support] definition). They are presented below in a simple human-readable explanation.  Profile specific guidance and examples are provided as well.  The [Formal Profile Definition] below provides the  formal summary, definitions, and  terminology requirements.

**Each {{{base_type}} must have:**

1. blah1
1. blah2

**Each {{base_type}} must support:**

1. blah1
1. blah2

### Examples

- [{{base_type}} Example]({{base_type}}-{{base_id}}-01.html

{% include link-list.md %}
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

'''template for generated profile pages and extraTemplates- assume the id is
 [Type]-profile-[id].xml or json and title is from resource title.  profile
  examples id is Type-[id]'''

generated_page = '''
<page>
    <nameUrl value="{generated_id}"/>
    <title value="{generated_title}"/>
    <generation value="generated"/>
    <!-- examples -->
    {profile-examples}
</page>'''

# template for generated profile examples id is Type-[id]
profile_examples = '''
<page>
    <nameUrl value="{id}"/>
    <title value="{ID}"/>
    <generation value="html"/>
    <!-- examples -->
    {profile-examples}
</page>'''

# Another Implementation guide ig.xml depends on
dependsOn ='''
<dependsOn id="{name}">  <!-- 0..* Another Implementation guide this depends on -->
  <uri value="{location}"><!-- 1..1 canonical(ImplementationGuide) Identity of the IG that this depends on --></uri>
  <packageId value="{package}"/><!-- 0..1 NPM Package name for IG this depends on -->
  <version value="{version}"/><!-- 0..1 Version of the IG -->
 </dependsOn>'''
