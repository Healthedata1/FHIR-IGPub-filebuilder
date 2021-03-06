# change the the case resource name using this mapping dict:
r_map = {
    'account': 'Account',
    'activitydefinition': 'ActivityDefinition',
    'adverseevent': 'AdverseEvent',
    'allergyintolerance': 'AllergyIntolerance',
    'appointment': 'Appointment',
    'appointmentresponse': 'AppointmentResponse',
    'auditevent': 'AuditEvent',
    'basic': 'Basic',
    'binary': 'Binary',
    'biologicallyderivedproduct': 'BiologicallyDerivedProduct',
    'bodystructure': 'BodyStructure',
    'bundle': 'Bundle',
    'capabilitystatement': 'CapabilityStatement',
    'careplan': 'CarePlan',
    'careteam': 'CareTeam',
    'catalogentry': 'CatalogEntry',
    'chargeitem': 'ChargeItem',
    'chargeitemdefinition': 'ChargeItemDefinition',
    'claim': 'Claim',
    'claimresponse': 'ClaimResponse',
    'clinicalimpression': 'ClinicalImpression',
    'codesystem': 'CodeSystem',
    'communication': 'Communication',
    'communicationrequest': 'CommunicationRequest',
    'compartmentdefinition': 'CompartmentDefinition',
    'composition': 'Composition',
    'conceptmap': 'ConceptMap',
    'condition': 'Condition',
    'consent': 'Consent',
    'contract': 'Contract',
    'coverage': 'Coverage',
    'coverageeligibilityrequest': 'CoverageEligibilityRequest',
    'coverageeligibilityresponse': 'CoverageEligibilityResponse',
    'detectedissue': 'DetectedIssue',
    'device': 'Device',
    'devicedefinition': 'DeviceDefinition',
    'devicemetric': 'DeviceMetric',
    'devicerequest': 'DeviceRequest',
    'deviceusestatement': 'DeviceUseStatement',
    'diagnosticreport': 'DiagnosticReport',
    'documentmanifest': 'DocumentManifest',
    'documentreference': 'DocumentReference',
    'domainresource': 'DomainResource',
    'effectevidencesynthesis': 'EffectEvidenceSynthesis',
    'encounter': 'Encounter',
    'endpoint': 'Endpoint',
    'enrollmentrequest': 'EnrollmentRequest',
    'enrollmentresponse': 'EnrollmentResponse',
    'episodeofcare': 'EpisodeOfCare',
    'eventdefinition': 'EventDefinition',
    'evidence': 'Evidence',
    'evidencevariable': 'EvidenceVariable',
    'examplescenario': 'ExampleScenario',
    'explanationofbenefit': 'ExplanationOfBenefit',
    'familymemberhistory': 'FamilyMemberHistory',
    'flag': 'Flag',
    'goal': 'Goal',
    'graphdefinition': 'GraphDefinition',
    'group': 'Group',
    'guidanceresponse': 'GuidanceResponse',
    'healthcareservice': 'HealthcareService',
    'imagingstudy': 'ImagingStudy',
    'immunization': 'Immunization',
    'immunizationevaluation': 'ImmunizationEvaluation',
    'immunizationrecommendation': 'ImmunizationRecommendation',
    'implementationguide': 'ImplementationGuide',
    'insuranceplan': 'InsurancePlan',
    'invoice': 'Invoice',
    'iteminstance': 'ItemInstance',
    'library': 'Library',
    'linkage': 'Linkage',
    'list': 'List',
    'location': 'Location',
    'measure': 'Measure',
    'measurereport': 'MeasureReport',
    'media': 'Media',
    'medication': 'Medication',
    'medicationadministration': 'MedicationAdministration',
    'medicationdispense': 'MedicationDispense',
    'medicationknowledge': 'MedicationKnowledge',
    'medicationrequest': 'MedicationRequest',
    'medicationstatement': 'MedicationStatement',
    'medicinalproduct': 'MedicinalProduct',
    'medicinalproductauthorization': 'MedicinalProductAuthorization',
    'medicinalproductcontraindication': 'MedicinalProductContraindication',
    'medicinalproductindication': 'MedicinalProductIndication',
    'medicinalproductingredient': 'MedicinalProductIngredient',
    'medicinalproductinteraction': 'MedicinalProductInteraction',
    'medicinalproductmanufactured': 'MedicinalProductManufactured',
    'medicinalproductpackaged': 'MedicinalProductPackaged',
    'medicinalproductpharmaceutical': 'MedicinalProductPharmaceutical',
    'medicinalproductundesirableeffect': 'MedicinalProductUndesirableEffect',
    'messagedefinition': 'MessageDefinition',
    'messageheader': 'MessageHeader',
    'namingsystem': 'NamingSystem',
    'nutritionorder': 'NutritionOrder',
    'observation': 'Observation',
    'observationdefinition': 'ObservationDefinition',
    'operationdefinition': 'OperationDefinition',
    'operationoutcome': 'OperationOutcome',
    'organization': 'Organization',
    'organizationaffiliation': 'OrganizationAffiliation',
    'parameters': 'Parameters',
    'patient': 'Patient',
    'paymentnotice': 'PaymentNotice',
    'paymentreconciliation': 'PaymentReconciliation',
    'person': 'Person',
    'plandefinition': 'PlanDefinition',
    'practitioner': 'Practitioner',
    'practitionerrole': 'PractitionerRole',
    'procedure': 'Procedure',
    'processrequest': 'ProcessRequest',
    'processresponse': 'ProcessResponse',
    'provenance': 'Provenance',
    'questionnaire': 'Questionnaire',
    'questionnaireresponse': 'QuestionnaireResponse',
    'relatedperson': 'RelatedPerson',
    'requestgroup': 'RequestGroup',
    'researchdefinition': 'ResearchDefinition',
    'researchelementdefinition': 'ResearchElementDefinition',
    'researchstudy': 'ResearchStudy',
    'researchsubject': 'ResearchSubject',
    'resource': 'Resource',
    'riskassessment': 'RiskAssessment',
    'riskevidencesynthesis': 'RiskEvidenceSynthesis',
    'schedule': 'Schedule',
    'searchparameter': 'SearchParameter',
    'sequence': 'Sequence',
    'servicerequest': 'ServiceRequest',
    'slot': 'Slot',
    'specimen': 'Specimen',
    'specimendefinition': 'SpecimenDefinition',
    'structuredefinition': 'StructureDefinition',
    'structuremap': 'StructureMap',
    'subscription': 'Subscription',
    'substance': 'Substance',
    'substancenucleicacid': 'SubstanceNucleicAcid',
    'substancepolymer': 'SubstancePolymer',
    'substanceprotein': 'SubstanceProtein',
    'substancereferenceinformation': 'SubstanceReferenceInformation',
    'substancesourcematerial': 'SubstanceSourceMaterial',
    'substancespecification': 'SubstanceSpecification',
    'supplydelivery': 'SupplyDelivery',
    'supplyrequest': 'SupplyRequest',
    'task': 'Task',
    'terminologycapabilities': 'TerminologyCapabilities',
    'testreport': 'TestReport',
    'testscript': 'TestScript',
    'usersession': 'UserSession',
    'valueset': 'ValueSet',
    'verificationresult': 'VerificationResult',
    'visionprescription': 'VisionPrescription',
    'address': 'Address',
    'age': 'Age',
    'annotation': 'Annotation',
    'attachment': 'Attachment',
    'backboneelement': 'BackboneElement',
    'codeableconcept': 'CodeableConcept',
    'coding': 'Coding',
    'contactdetail': 'ContactDetail',
    'contactpoint': 'ContactPoint',
    'contributor': 'Contributor',
    'count': 'Count',
    'datarequirement': 'DataRequirement',
    'distance': 'Distance',
    'dosage': 'Dosage',
    'duration': 'Duration',
    'element': 'Element',
    'elementdefinition': 'ElementDefinition',
    'expression': 'Expression',
    'extension': 'Extension',
    'humanname': 'HumanName',
    'identifier': 'Identifier',
    'marketingstatus': 'MarketingStatus',
    'meta': 'Meta',
    'money': 'Money',
    'moneyquantity': 'MoneyQuantity',
    'narrative': 'Narrative',
    'parameterdefinition': 'ParameterDefinition',
    'period': 'Period',
    'population': 'Population',
    'prodcharacteristic': 'ProdCharacteristic',
    'productshelflife': 'ProductShelfLife',
    'quantity': 'Quantity',
    'range': 'Range',
    'ratio': 'Ratio',
    'reference': 'Reference',
    'relatedartifact': 'RelatedArtifact',
    'sampleddata': 'SampledData',
    'signature': 'Signature',
    'simplequantity': 'SimpleQuantity',
    'substanceamount': 'SubstanceAmount',
    'timing': 'Timing',
    'triggerdefinition': 'TriggerDefinition',
    'usagecontext': 'UsageContext',
    'base64binary': 'base64Binary',
    'boolean': 'boolean',
    'canonical': 'canonical',
    'code': 'code',
    'date': 'date',
    'datetime': 'dateTime',
    'decimal': 'decimal',
    'id': 'id',
    'instant': 'instant',
    'integer': 'integer',
    'markdown': 'markdown',
    'oid': 'oid',
    'positiveint': 'positiveInt',
    'string': 'string',
    'time': 'time',
    'unsignedint': 'unsignedInt',
    'uri': 'uri',
    'url': 'url',
    'uuid': 'uuid',
    'xhtml': 'xhtml'
    }

r_list = [
    'account',
    'activitydefinition',
    'adverseevent',
    'allergyintolerance',
    'appointment',
    'appointmentresponse',
    'auditevent',
    'basic',
    'binary',
    'biologicallyderivedproduct',
    'bodystructure',
    'bundle',
    'capabilitystatement',
    'careplan',
    'careteam',
    'catalogentry',
    'chargeitem',
    'chargeitemdefinition',
    'claim',
    'claimresponse',
    'clinicalimpression',
    'codesystem',
    'communication',
    'communicationrequest',
    'compartmentdefinition',
    'composition',
    'conceptmap',
    'condition',
    'consent',
    'contract',
    'coverage',
    'coverageeligibilityrequest',
    'coverageeligibilityresponse',
    'detectedissue',
    'device',
    'devicedefinition',
    'devicemetric',
    'devicerequest',
    'deviceusestatement',
    'diagnosticreport',
    'documentmanifest',
    'documentreference',
    'domainresource',
    'effectevidencesynthesis',
    'encounter',
    'endpoint',
    'enrollmentrequest',
    'enrollmentresponse',
    'episodeofcare',
    'eventdefinition',
    'evidence',
    'evidencevariable',
    'examplescenario',
    'explanationofbenefit',
    'familymemberhistory',
    'flag',
    'goal',
    'graphdefinition',
    'group',
    'guidanceresponse',
    'healthcareservice',
    'imagingstudy',
    'immunization',
    'immunizationevaluation',
    'immunizationrecommendation',
    'implementationguide',
    'insuranceplan',
    'invoice',
    'iteminstance',
    'library',
    'linkage',
    'list',
    'location',
    'measure',
    'measurereport',
    'media',
    'medication',
    'medicationadministration',
    'medicationdispense',
    'medicationknowledge',
    'medicationrequest',
    'medicationstatement',
    'medicinalproduct',
    'medicinalproductauthorization',
    'medicinalproductcontraindication',
    'medicinalproductindication',
    'medicinalproductingredient',
    'medicinalproductinteraction',
    'medicinalproductmanufactured',
    'medicinalproductpackaged',
    'medicinalproductpharmaceutical',
    'medicinalproductundesirableeffect',
    'messagedefinition',
    'messageheader',
    'namingsystem',
    'nutritionorder',
    'observation',
    'observationdefinition',
    'operationdefinition',
    'operationoutcome',
    'organization',
    'organizationaffiliation',
    'parameters',
    'patient',
    'paymentnotice',
    'paymentreconciliation',
    'person',
    'plandefinition',
    'practitioner',
    'practitionerrole',
    'procedure',
    'processrequest',
    'processresponse',
    'provenance',
    'questionnaire',
    'questionnaireresponse',
    'relatedperson',
    'requestgroup',
    'researchdefinition',
    'researchelementdefinition',
    'researchstudy',
    'researchsubject',
    'resource',
    'riskassessment',
    'riskevidencesynthesis',
    'schedule',
    'searchparameter',
    'sequence',
    'servicerequest',
    'slot',
    'specimen',
    'specimendefinition',
    'structuredefinition',
    'structuremap',
    'subscription',
    'substance',
    'substancenucleicacid',
    'substancepolymer',
    'substanceprotein',
    'substancereferenceinformation',
    'substancesourcematerial',
    'substancespecification',
    'supplydelivery',
    'supplyrequest',
    'task',
    'terminologycapabilities',
    'testreport',
    'testscript',
    'usersession',
    'valueset',
    'verificationresult',
    'visionprescription'
        ]
