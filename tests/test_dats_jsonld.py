from unittest import TestCase
from dats import dats_jsonld
import jsonref


jsonld_doc = """
{
  "@context": "http://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
  "@type": "Dataset",
  "identifier": {
    "identifier": "5AEM",
    "identifierSource": "PDB"
  },
  "alternateIdentifiers": [
    {
      "identifier": "http://identifiers.org/pdb/5AEM",
      "identifierSource": "http://identifiers.org"
    }
  ],

  "title" : "Structure of t131 N-terminal TPR array",

  "creators": [
    {
      "@context": "http://w3id.org/dats/context/sdo/person_sdo_context.jsonld",
      "@type": "Person",
      "fullName": "C.W.Muller"
    }
  ],

  "description" : "TRANSCRIPTION FACTOR TAU 131 KDA SUBUNIT",

  "types" : [
    {
      "information": { "value": "protein 3D structure"}
    },
    {
      "information": { "value": "transcription"}
    }
  ],

  "distributions": [
    {
      "@context": "http://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
      "@type": "DatasetDistribution",
      "dates": [
        {
          "date": "2015/01/05",
          "type": {}
        },
        {
          "date": "2015/06/24",
          "type": { "value": "release date"}
        }
      ],

      "access":
      {
        "@context": "http://w3id.org/dats/context/sdo/access_sdo_context.jsonld",
        "@type": "Access",
        "landingPage": "http://identifiers.org/pdb/5AEM",
        "accessURL": "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=FASTA&compression=NO&structureId=5AEM"
      },
      "storedIn" :
      {
        "@context": "http://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@type": "DataRepository",
        "identifier": {
          "identifier": "https://www.fairsharing.org/biodbcore-000511",
          "identifierSource": "FAIRsharing"
        },
        "alternateIdentifiers": [
          {
            "identifier": "http://www.rcsb.org/pdb/",
            "identifierSource": "HTTP"
          }
        ],
        "name": "RCSB Protein Data Bank",
        "licenses" : [
          {
            "@context": "http://w3id.org/dats/context/sdo/license_sdo_context.jsonld",
            "@type": "License",
            "name": "free of all copyright restrictions and made fully and freely available for both non-commercial and commercial use"
          }
        ]
      },
      "conformsTo": [
        {
          "@context": "http://w3id.org/dats/context/sdo/data_standard_sdo_context.jsonld",
          "@type": "DataStandard",
          "identifier": {
            "identifier": "https://www.fairsharing.org/bsg-000255",
            "identifierSource": "FAIRsharing"
          },
          "name": "Protein Data Bank Format",
          "type": { "value": "format"}
        },
        {
          "@context": "http://w3id.org/dats/context/sdo/data_standard_sdo_context.jsonld",
          "@type": "DataStandard",
          "identifier": {
            "identifier": "https://www.fairsharing.org/bsg-000290",
            "identifierSource": "FAIRsharing"
          },
          "name": "macromolecular Crystallographic Information File",
          "type": { "value": "format"}
        }
      ]
    },
    {
      "@context": "http://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
      "@type": "DatasetDistribution",
      "dates": [
        {
          "date": "2015/01/05",
          "type": {}
        },
        {
          "date": "2015/06/24",
          "type": { "value": "release date"}
        }
      ],

      "access":
      {
        "@context": "http://w3id.org/dats/context/sdo/access_sdo_context.jsonld",
        "@type": "Access",
        "landingPage": "http://identifiers.org/pdb/5AEM",
        "accessURL": "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId=5AEM"
      },
      "storedIn" :
      {
        "@context": "http://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@type": "DataRepository",
        "identifier": {
          "identifier": "https://www.fairsharing.org/biodbcore-000511",
          "identifierSource": "FAIRsharing"
        },
        "alternateIdentifiers": [{
          "identifier": "http://www.rcsb.org/pdb/",
          "identifierSource": "HTTP"
        }
        ],
        "name": "RCSB Protein Data Bank",
        "licenses" : [
          {
            "@context": "http://w3id.org/dats/context/sdo/license_sdo_context.jsonld",
            "@type": "License",
            "name": "free of all copyright restrictions and made fully and freely available for both non-commercial and commercial use"
          }
        ]
      },
      "conformsTo": [
        {
          "@context": "http://w3id.org/dats/context/sdo/data_standard_sdo_context.jsonld",
          "@type": "DataStandard",
          "identifier": {
            "identifier": "https://www.fairsharing.org/bsg-000255",
            "identifierSource": "FAIRsharing"
          },
          "name": "Protein Data Bank Format",
          "type": { "value": "format"}
        },
        {
          "@context": "http://w3id.org/dats/context/sdo/data_standard_sdo_context.jsonld",
          "@type": "DataStandard",
          "identifier": {
            "identifier": "https://www.fairsharing.org/bsg-000290",
            "identifierSource": "FAIRsharing"
          },
          "name": "macromolecular Crystallographic Information File",
          "type": { "value": "format"}
        }
      ]
    },
    {
      "@context": "http://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
      "@type": "DatasetDistribution",
      "dates": [
        {
          "date": "2015/01/05",
          "type": {}
        },
        {
          "date": "2015/06/24",
          "type": { "value": "release date"}
        }
      ],
      "access":
      {
        "@context": "http://w3id.org/dats/context/sdo/access_sdo_context.jsonld",
        "@type": "Access",
        "landingPage": "http://identifiers.org/pdb/5AEM",
        "accessURL": "http://www.rcsb.org/pdb/files/5AEM.pdb.gz"
      },
      "storedIn" :
      {
        "@context": "http://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@type": "DataRepository",
        "identifier": {
          "identifier": "https://www.fairsharing.org/biodbcore-000511",
          "identifierSource": "FAIRsharing"
        },
        "alternateIdentifiers": [
          {
            "identifier": "http://www.rcsb.org/pdb/",
            "identifierSource": "HTTP"
          }
        ],
        "name": "RCSB Protein Data Bank",
        "licenses" : [
          {
            "@context": "http://w3id.org/dats/context/sdo/license_sdo_context.jsonld",
            "@type": "License",
            "name": "free of all copyright restrictions and made fully and freely available for both non-commercial and commercial use"
          }
        ]
      },
      "conformsTo": [
        {
         "@context": "http://w3id.org/dats/context/sdo/data_standard_sdo_context.jsonld",
          "@type": "DataStandard",
          "identifier": {
            "identifier": "https://www.fairsharing.org/bsg-000255",
            "identifierSource": "FAIRsharing"
          },
          "name": "Protein Data Bank Format",
          "type": { "value": "format"}
        },
        {
          "@context": "http://w3id.org/dats/context/sdo/data_standard_sdo_context.jsonld",
          "@type": "DataStandard",
          "identifier": {
            "identifier": "https://www.fairsharing.org/bsg-000290",
            "identifierSource": "FAIRsharing"
          },
          "name": "macromolecular Crystallographic Information File",
          "type": { "value": "format"}
        }
      ]
    }
  ],
  "primaryPublications" : [
    {
      "@context": "http://w3id.org/dats/context/sdo/publication_sdo_context.jsonld",
      "@type": "Publication",
      "identifier": {
        "identifier": "26060179",
        "identifierSource": "PMID"
      },
      "title": "Architecture of Tfiiic and its Role in RNA Polymerase III Pre-Initiation Complex Assembly.",
      "type" : {
        "value": "article"
      },
      "dates" : [
        {
          "date": "2015",
          "type": {
            "value": "publication date"
          }
        }
      ],
      "authors" : [
        {
          "@context": "http://w3id.org/dats/context/sdo/person_sdo_context.jsonld",
          "@type": "Person",
          "firstName": "G.",
          "lastName": "Male"
        },
        {
          "@context": "http://w3id.org/dats/context/sdo/person_sdo_context.jsonld",
          "@type": "Person",
          "firstName": "A.",
          "lastName": "Von Appen"
        },
        {
          "@context": "http://w3id.org/dats/context/sdo/person_sdo_context.jsonld",
          "@type": "Person",
          "firstName": "S.",
          "lastName": "Glatt"
        },
        {
          "@context": "http://w3id.org/dats/context/sdo/person_sdo_context.jsonld",
          "@type": "Person",
          "firstName": "N.M.I.",
          "lastName": "Taylor"
        },
        {
          "@context": "http://w3id.org/dats/context/sdo/person_sdo_context.jsonld",
          "@type": "Person",
          "firstName": "M.",
          "lastName": "Cristovao"
        },
        {
          "@context": "http://w3id.org/dats/context/sdo/person_sdo_context.jsonld",
          "@type": "Person",
          "firstName": "H.",
          "lastName": "Groetsch"
        },
        {
          "@context": "http://w3id.org/dats/context/sdo/person_sdo_context.jsonld",
          "@type": "Person",
          "firstName": "M.",
          "lastName": "Beck"
        },
        {
          "@context": "http://w3id.org/dats/context/sdo/person_sdo_context.jsonld",
          "@type": "Person",
          "firstName": "C.W.",
          "lastName": "Muller"
        }
      ]
    }

  ],
  "producedBy" : {
    "@context": "http://w3id.org/dats/context/sdo/study_sdo_context.jsonld",
    "@type": "Study",
    "name" : "crystallography study",
    "input": [
      {
        "name": "N-TERMINAL TPR ARRAY, RESIDUES 123-566",
        "characteristics" : [
          {
            "name" : "sequence"
          }
        ]
      }
    ],
    "schedulesDataAcquisition": [
      {
        "@context": "http://w3id.org/dats/context/sdo/data_acquisition_sdo_context.jsonld",
        "@type": "DataAcquisition",
        "name" : "X-RAY DIFFRACTION",
        "startDate": {
          "date": "04-FEB-10",
          "type": { "value": "start date"}
        },
        "endDate": {
          "date": "04-FEB-10",
          "type": { "value": "end date" }
        },
        "uses": [
          {
            "name": "SCALA"
          },
          {
            "name": "SYNCHROTRON"
          }
        ]
      }

    ]
  }
}
"""

topmed="""{
  "@type": "Dataset",
  "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
  "@id": "http://w3id.org/datacommons/topmeddataset",
  "identifier": {
    "@type": "Identifier",
    "identifierSource": "TOPMed",
    "identifier": "https://www.ncbi.nlm.nih.gov/gap/?term=topmed"
  },
  "title": "Trans-Omics for Precision Medicine (TOPMed)",
  "description": "TOPMed generates scientific resources related to heart, lung, blood, and sleep disorders (HLBS). It is sponsored by the NIH NHLBI and is part of a broader Precision Medicine Initiative.",
  "storedIn": {
    "@type": "DataRepository",
    "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
    "@id": "https://www.ncbi.nlm.nih.gov/gap",
    "name": "dbGaP"
  },
  "types": [
    {
      "@type": "DataType",
      "@id": "http://w3id.org/datacommons/datatype1",
      "@context": "https://w3id.org/dats/context/sdo/data_type_sdo_context.jsonld",
      "information": {
        "value": "DNA sequencing",
        "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
      },
      "method": {
        "value": "whole genome sequencing assay",
        "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
      },
      "platform": {
        "value": "Illumina",
        "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000759"
      }
    }
  ],
  "creators": [
    {
      "@type": "Organization",
      "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
      "@id": "https://www.nhlbi.nih.gov/",
      "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
      "abbreviation": "NHLBI"
    }
  ],
  "distributions": [
    {
      "@type": "DatasetDistribution",
      "@context": "https://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/datasetdistribution1",
      "access": {
        "@type": "Access",
        "@id": "http://w3id.org/datacommons/access1",
        "landingPage": "https://www.ncbi.nlm.nih.gov/gap/?term=topmed"
      }
    }
  ],
  "hasPart": [
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/dataset2",
      "identifier": {
        "@type": "Identifier",
        "@context": "https://w3id.org/dats/context/sdo/identifier_info_sdo_context.jsonld",
        "@id": "http://w3id.org/datacommons/phs000946.v3.p1.identifier",
        "identifier": "phs000946.v3.p1"
      },
      "version": "v3",
      "title": "Boston Early-Onset COPD Study in the TOPMed Program",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "http://w3id.org/datacommons/datarepository2",
        "name": "dbGaP"
      },
      "types": [
        {
          "@context": "https://w3id.org/dats/context/sdo/data_type_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/datatype2",
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension1",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "@id": "http://w3id.org/datacommons/datatype3",
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            80
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "http://w3id.org/datacommons/extraproperties1",
          "category": "study_type",
          "values": [
            "Pedigree Whole Genome Sequencing"
          ]
        }
      ],
      "isAbout": [
        {
          "@type": "Material",
          "@context": "https://w3id.org/dats/context/sdo/material_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/material1",
          "name": "DNA from SA0000000",
          "description": "DNA extracted from blood specimen collected from subject SU0000000",
          "taxonomy": [
            {
              "@type": "TaxonomicInformation",
              "@context": "https://w3id.org/dats/context/sdo/taxonomic_information_sdo_context.jsonld",
              "@id": "https://www.ncbi.nlm.nih.gov/taxonomy/9606",
              "name": "Homo sapiens",
              "identifier": {
                "@context": "https://w3id.org/dats/context/sdo/identifier_info_sdo_context.jsonld",
                "identifier": "ncbitax:9606",
                "identifierSource": "ncbitax"
              }
            }
          ],
          "roles": [
            {
              "value": "DNA extract",
              "valueIRI": ""
            }
          ],
          "derivesFrom": [
            {
              "@type": "Material",
              "@context": "https://w3id.org/dats/context/sdo/material_sdo_context.jsonld",
              "@id": "http://w3id.org/datacommons/material2",
              "name": "SA0000000",
              "identifier": {
                "identifier": "SA0000000"
              },
              "alternateIdentifiers": [
                {
                  "@type": "AlternateIdentifier",
                  "@id": "",
                  "identifier": "0000000",
                  "identifierSource": "dbGaP"
                }
              ],
              "description": "blood specimen collected from subject SU0000000",
              "taxonomy": [
                {
                  "@type": "TaxonomicInformation",
                  "@context": "https://w3id.org/dats/context/sdo/taxonomic_information_sdo_context.jsonld",
                  "@id": "https://www.ncbi.nlm.nih.gov/taxonomy/9606",
                  "name": "Homo sapiens",
                  "identifier": {
                    "identifier": "ncbitax:9606",
                    "identifierSource": "ncbitax"
                  }
                }
              ],
              "roles": [
                {
                  "value": "specimen",
                  "valueIRI": ""
                }
              ],
              "derivesFrom": [
                {
                  "@type": "Material",
                  "@context": "https://w3id.org/dats/context/sdo/material_sdo_context.jsonld",
                  "@id": "",
                  "name": "SU0000000",
                  "identifier": {
                    "identifier": "SU0000000"
                  },
                  "alternateIdentifiers": [
                    {
                      "@type": "AlternateIdentifier",
                      "@context": "https://w3id.org/dats/context/sdo/alternate_identifier_info_sdo_context.jsonld",
                      "@id": "",
                      "identifier": "0000000",
                      "identifierSource": "dbGaP"
                    }
                  ],
                  "description": "Boston Early-Onset COPD Study in the TOPMed Program subject SU0000000",
                  "characteristics": [
                    {
                      "@type": "Dimension",
                      "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
                      "@id": "",
                      "name": {
                        "value": "Gender"
                      },
                      "description": "Gender of the subject",
                      "values": [
                        "female"
                      ]
                    },
                    {
                      "@type": "Dimension",
                      "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
                      "@id": "",
                      "name": {
                        "value": "Age"
                      },
                      "description": "Age of the subject",
                      "values": [
                        "46.76"
                      ]
                    }
                  ],
                  "taxonomy": [
                    {
                      "@type": "TaxonomicInformation",
                      "@context": "https://w3id.org/dats/context/sdo/taxonomic_information_sdo_context.jsonld",
                      "@id": "https://www.ncbi.nlm.nih.gov/taxonomy/9606",
                      "name": "Homo sapiens",
                      "identifier": {
                        "identifier": "ncbitax:9606",
                        "identifierSource": "ncbitax"
                      }
                    }
                  ],
                  "roles": [
                    {
                      "value": "patient",
                      "valueIRI": ""
                    },
                    {
                      "value": "donor",
                      "valueIRI": ""
                    }
                  ],
                  "extraProperties": [
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "BMI",
                      "values": [
                        "23.71"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "CIGSPERDAY",
                      "values": [
                        "5"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "CIGSPERDAY_AVERAGE",
                      "values": [
                        "25"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "CURRENT_SMOKER",
                      "values": [
                        "No"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "DNA_AGE",
                      "values": [
                        "48.75"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "FORMER_SMOKER",
                      "values": [
                        "No"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "GENDER",
                      "values": [
                        "Female"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "HEIGHT",
                      "values": [
                        "161.3"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "PACKYEARS",
                      "values": [
                        "32.25"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "PREGNANCY",
                      "values": [
                        "No"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "RACE",
                      "values": [
                        "Caucasian"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "SUBJECT_ID",
                      "values": [
                        "SU0000000"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "VISIT_AGE",
                      "values": [
                        "46.76"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "WEIGHT",
                      "values": [
                        "63.64"
                      ]
                    },
                    {
                      "@type": "CategoryValuesPair",
                      "@id": "",
                      "category": "dbGaP_Subject_ID",
                      "values": [
                        "0000000"
                      ]
                    }
                  ]
                },
                {
                  "@type": "AnatomicalPart",
                  "@context": "https://w3id.org/dats/context/sdo/anatomical_part_sdo_context.jsonld",
                  "@id": "",
                  "name": "blood",
                  "identifier": {
                    "identifier": "UBERON:0000178",
                    "identifierSource": "UBERON"
                  },
                  "alternateIdentifiers": [
                    {
                      "identifier": "http://purl.obolibrary.org/obo/UBERON_0000178",
                      "identifierSource": "UBERON"
                    }
                  ]
                }
              ],
              "extraProperties": [
                {
                  "@type": "CategoryValuesPair",
                  "@id": "",
                  "category": "ANALYTE_TYPE",
                  "values": [
                    "DNA"
                  ]
                },
                {
                  "@type": "CategoryValuesPair",
                  "@id": "",
                  "category": "BODY_SITE",
                  "values": [
                    "Blood"
                  ]
                },
                {
                  "@type": "CategoryValuesPair",
                  "@id": "",
                  "category": "Funding_Source",
                  "values": [
                    "TOPMed"
                  ]
                },
                {
                  "@type": "CategoryValuesPair",
                  "@id": "",
                  "category": "IS_TUMOR",
                  "values": [
                    "Is not a tumor"
                  ]
                },
                {
                  "@type": "CategoryValuesPair",
                  "@id": "",
                  "category": "SAMPLE_ID",
                  "values": [
                    "SA0000000"
                  ]
                },
                {
                  "@type": "CategoryValuesPair",
                  "@id": "",
                  "category": "SEQUENCING_CENTER",
                  "values": [
                    "UW"
                  ]
                },
                {
                  "@type": "CategoryValuesPair",
                  "@id": "",
                  "category": "Study_Name",
                  "values": [
                    "EOCOPD"
                  ]
                },
                {
                  "@type": "CategoryValuesPair",
                  "@id": "",
                  "category": "TOPMed_Phase",
                  "values": [
                    "1"
                  ]
                },
                {
                  "@type": "CategoryValuesPair",
                  "@id": "",
                  "category": "TOPMed_Project",
                  "values": [
                    "COPD"
                  ]
                },
                {
                  "@type": "CategoryValuesPair",
                  "@id": "",
                  "category": "dbGaP_Sample_ID",
                  "values": [
                    "0000000"
                  ]
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs001024.v3.p1",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs001024.v3.p1.identifier",
        "identifier": "phs001024.v3.p1"
      },
      "version": "v3",
      "title": "Partners HealthCare Biobank",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension2",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            128
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case Set"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs000964.v3.p1",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs000964.v3.p1.identifier",
        "identifier": "phs000964.v3.p1"
      },
      "version": "v3",
      "title": "The Jackson Heart Study",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension3",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            3596
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Longitudinal Cohort"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs000956.v3.p1",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs000956.v3.p1.identifier",
        "identifier": "phs000956.v3.p1"
      },
      "version": "v3",
      "title": "Genetics of Cardiometabolic Health in the Amish",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension4",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            1123
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Family"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs000954.v2.p1",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs000954.v2.p1.identifier",
        "identifier": "phs000954.v2.p1"
      },
      "version": "v2",
      "title": "The Cleveland Family Study (WGS)",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension5",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            994
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Longitudinal"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs000921.v2.p1",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs000921.v2.p1.identifier",
        "identifier": "phs000921.v2.p1"
      },
      "version": "v2",
      "title": "Study of African Americans, Asthma, Genes and Environment (SAGE) Study",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension6",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            500
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case Set"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs001040.v2.p1",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs001040.v2.p1.identifier",
        "identifier": "phs001040.v2.p1"
      },
      "version": "v2",
      "title": "Novel Risk Factors for the Development of Atrial Fibrillation in Women",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension7",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            118
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case Set"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs000993.v2.p2",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs000993.v2.p2.identifier",
        "identifier": "phs000993.v2.p2"
      },
      "version": "v2",
      "title": "Heart and Vascular Health Study (HVH)",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension8",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            709
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case Set"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs000997.v2.p2",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs000997.v2.p2.identifier",
        "identifier": "phs000997.v2.p2"
      },
      "version": "v2",
      "title": "The Vanderbilt AF Ablation Registry",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension9",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            171
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case Set"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs001032.v3.p2",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs001032.v3.p2.identifier",
        "identifier": "phs001032.v3.p2"
      },
      "version": "v3",
      "title": "The Vanderbilt Atrial Fibrillation Registry",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension10",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            1134
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case Set"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs001062.v2.p2",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs001062.v2.p2.identifier",
        "identifier": "phs001062.v2.p2"
      },
      "version": "v2",
      "title": "MGH Atrial Fibrillation Study",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension11",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            999
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case Set"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs000920.v2.p2",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs000920.v2.p2.identifier",
        "identifier": "phs000920.v2.p2"
      },
      "version": "v2",
      "title": "Genes-environments and Admixture in Latino Asthmatics (GALA II) Study",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension12",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            999
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case Set"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
       "@id": "http://w3id.org/datacommons/phs000974.v2.p2",
      "identifier": {
        "@type": "Identifier",
        "@context": "https://w3id.org/dats/context/sdo/identifier_info_sdo_context.jsonld",
        "@id": "http://w3id.org/datacommons/phs000974.v2.p2.identifier",
        "identifier": "phs000974.v2.p2"
      },
      "version": "v2",
      "title": "Whole Genome Sequencing and Related Phenotypes in the Framingham Heart Study",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension13",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            4154
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Cohort"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs000951.v2.p2",
      "identifier": {
        "@type": "Identifier",
        "@context": "https://w3id.org/dats/context/sdo/identifier_info_sdo_context.jsonld",
        "@id": "http://w3id.org/datacommons/phs000951.v2.p2.identifier",
        "identifier": "phs000951.v2.p2"
      },
      "version": "v2",
      "title": "Genetic Epidemiology of COPD (COPDGene) in the TOPMed Program",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension14",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            10229
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case-Control"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs000988.v2.p1",
      "identifier": {
        "@type": "Identifier",
        "@context": "https://w3id.org/dats/context/sdo/identifier_info_sdo_context.jsonld",
        "@id": "http://w3id.org/datacommons/phs000988.v2.p1.identifier",
        "identifier": "phs000988.v2.p1"
      },
      "version": "v2",
      "title": "The Genetic Epidemiology of Asthma in Costa Rica",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension15",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            1533
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Parent-Offspring Trios"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs000972.v2.p1",
      "identifier": {
        "@type": "Identifier",
        "@id": "http://w3id.org/datacommons/phs000972.v2.p1.identifier",
        "identifier": "phs000972.v2.p1"
      },
      "version": "v2",
      "title": "Genome-wide Association Study of Adiposity in Samoans",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension16",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            1332
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Cross-Sectional, Population"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs001211.v1.p1",
      "identifier": {
        "@type": "Identifier",
        "@context": "https://w3id.org/dats/context/sdo/identifier_info_sdo_context.jsonld",
        "@id": "http://w3id.org/datacommons/phs000972.v2.p1.identifier",
        "identifier": "phs001211.v1.p1"
      },
      "version": "v1",
      "title": "Trans-Omics for Precision Medicine Whole Genome Sequencing Project: ARICVersion 1: passed embargo",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension17",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            4230
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case-Control"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs001189.v1.p1",
      "identifier": {
        "@type": "Identifier",
        "@context": "https://w3id.org/dats/context/sdo/identifier_info_sdo_context.jsonld",
        "@id": "http://w3id.org/datacommons/phs001189.v1.p1.identifier",
        "identifier": "phs001189.v1.p1"
      },
      "version": "v1",
      "title": "Cleveland Clinic Atrial Fibrillation StudyVersion 1: passed embargo",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq X Ten",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002129"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension18",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            362
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Case Set"
          ]
        }
      ]
    },
    {
      "@type": "Dataset",
      "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
      "@id": "http://w3id.org/datacommons/phs001143.v1.p1",
      "identifier": {
        "@type": "Identifier",
        "@context": "https://w3id.org/dats/context/sdo/identifier_info_sdo_context.jsonld",
        "@id": "http://w3id.org/datacommons/phs001143.v1.p1.identifier",
        "identifier": "phs001143.v1.p1"
      },
      "version": "v1",
      "title": "The Genetics and Epidemiology of Asthma in BarbadosVersion 1: passed embargo",
      "storedIn": {
        "@type": "DataRepository",
        "@context": "https://w3id.org/dats/context/sdo/data_repository_sdo_context.jsonld",
        "@id": "",
        "name": "dbGaP"
      },
      "types": [
        {
          "information": {
            "value": "DNA sequencing",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0000626"
          },
          "method": {
            "value": "whole genome sequencing assay",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002117"
          },
          "platform": {
            "value": "Illumina HiSeq 2000",
            "valueIRI": "http://purl.obolibrary.org/obo/OBI_0002001"
          }
        }
      ],
      "creators": [
        {
          "@type": "Organization",
          "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
          "@id": "https://www.nhlbi.nih.gov/",
          "name": "The National Institute of Health's National Heart, Lung and Blood Institute",
          "abbreviation": "NHLBI"
        }
      ],
      "dimensions": [
        {
          "@type": "Dimension",
          "@context": "https://w3id.org/dats/context/sdo/dimension_sdo_context.jsonld",
          "@id": "http://w3id.org/datacommons/dimension19",
          "name": {
            "value": "Actual Subject Count"
          },
          "description": "The actual number of subjects entered into a clinical trial.",
          "types": [
            {
              "value": "Actual Subject Number",
              "valueIRI": "http://purl.obolibrary.org/obo/NCIT_C98703"
            }
          ],
          "values": [
            1527
          ]
        }
      ],
      "extraProperties": [
        {
          "@type": "CategoryValuesPair",
          "@id": "",
          "category": "study_type",
          "values": [
            "Family"
          ]
        }
      ]
    }
  ]
}"""

bdbag="""
{
    "@type": "Dataset",
    "@id": "http://identifiers.org/minid:b9j69h",
    "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
    "identifier": {
        "@type": "Identifier",
        "@context": "https://w3id.org/dats/context/sdo/identifier_info_sdo_context.jsonld",
        "identifier": "http://identifiers.org/minid:b9j69h",
        "identifierSource": "minid"
    },
    "title": "AGR Data set with identifier-based references to data in cloud storage",
    "description": "AGR Data set with identifier-based references to data in cloud storage",
    "dates": [{
        "date": "2018-03-19 17:43:57.073822",
        "type": {
            "value": "creation",
            "valueIRI": ""
        }
    }],
    "creators": [{
        "@type": "Person",
        "@context": "https://w3id.org/dats/context/sdo/person_sdo_context.jsonld",
        "identifier": {
            "identifier": "http://orcid.org/0000-0003-2280-917X",
            "identifierSource": "orcid"
        },
        "affiliations": [{
            "@type": "Organization",
            "@context": "https://w3id.org/dats/context/sdo/organization_sdo_context.jsonld",
            "name": "University of Southern California / Information Science"
        }],
        "firstName": "Michel",
        "fullName": "Mike d'Arcy",
        "lastName": "d'Arcy"
    }],
    "types": [{"information": {"value": "model organism data"}}],
    "hasPart": [
        {
            "@type": "Dataset",
            "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
            "@id": "https://identifiers.org/minid:b9n39d",
            "identifier": {
                "identifier": "minid:b9n39d",
                "identifierSource": "minid"
            },
            "title": "A list of disease ontology terms obtained from the Disease Ontology website.",
            "types": [{"information": {"value": "ontology terms"}}],
            "creators": [ {} ],
            "distributions": [{
                "@type": "DatasetDistribution",
                "@context": "https://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
                "identifier": {
                    "identifier": "minid:b9n39d",
                    "identifierSource": ""
                },
                "access": {
                    "@type": "Access",
                    "@context": "https://w3id.org/dats/context/sdo/access_sdo_context.jsonld",
                    "accessURL": "https://s3.amazonaws.com/mod-datadumps/DO/do_1.0.obo",
                    "landingPage": "https://identifiers.org/minid:b9n39d"
                },
                "conformsTo": [{
                    "name": "obo format",
                    "type": {
                        "value": "text/plain",
                        "valueIRI": ""
                    }
                }],
                "size": 4784295,
                "unit": {
                    "value": "byte",
                    "valueIRI": "http://purl.obolibrary.org/obo/UO_0000233"
                },
                "version": "Release 2.6.2018"
            }]
        },
        {
            "@type": "Dataset",
            "@id": "http://identifiers.org/minid:b9hd64",
            "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
            "identifier": {
                "identifier": "minid:b9hd64",
                "identifierSource": "minid"
            },
            "title": "A list of gene ontology terms obtained from the Gene Ontology Consortium.",
            "types": [{"information": {"value": "ontology terms"}}],
            "creators": [ {} ],
            "distributions": [{
                "@type": "DatasetDistribution",
                "@context": "https://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
                "identifier": {
                    "identifier": "minid:b9hd64",
                    "identifierSource": ""
                },
                "access": {
                    "@type": "Access",
                    "@context": "https://w3id.org/dats/context/sdo/access_sdo_context.jsonld",
                    "accessURL": "https://s3.amazonaws.com/mod-datadumps/GO/go_1.0.obo",
                    "landingPage": "http://identifiers.org/minid:b9hd64"
                },
                "conformsTo": [{
                    "name": "obo format",
                    "type": {
                        "value": "text/plain",
                        "valueIRI": ""
                    }
                }],
                "size": 36520029,
                "unit": {
                    "value": "byte",
                    "valueIRI": "http://purl.obolibrary.org/obo/UO_0000233"
                },
                "version": "Release 2.6.2018"
            }]
        },
        {
            "@type": "Dataset",
            "@id": "http://identifiers.org/minid:b9px1z",
            "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
            "identifier": {
                "identifier": "minid:b9px1z",
                "identifierSource": "minid"
            },
            "title": "A list of sequence ontology terms obtained from the Sequence Ontology website.",
            "types": [{"information": {"value": "ontology terms"}}],
            "creators": [ {} ],
            "dates": [{
                "date": "2.6.2018",
                "type": {
                    "value": "creation",
                    "valueIRI": ""
                }
            }],
            "distributions": [{
                "@type": "DatasetDistribution",
                "@context": "https://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
                "identifier": {
                    "identifier": "minid:b9px1z",
                    "identifierSource": ""
                },
                "access": {
                    "@type": "Access",
                    "@context": "https://w3id.org/dats/context/sdo/access_sdo_context.jsonld",
                    "accessURL": "https://s3.amazonaws.com/mod-datadumps/SO/so_1.0.obo",
                    "landingPage": "http://identifiers.org/minid:b9px1z"
                },
                "conformsTo": [{
                    "name": "obo format",
                    "type": {
                        "value": "text/plain",
                        "valueIRI": ""
                    }
                }],
                "size": 902733,
                "unit": {
                    "value": "byte",
                    "valueIRI": "http://purl.obolibrary.org/obo/UO_0000233"
                },
                "version": "Release 11.24.2015"
            }]
        },
        {
            "@type": "Dataset",
            "@id": "http://identifiers.org/minid:b9dm68",
            "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
            "identifier": {
                "identifier": "minid:b9dm68",
                "identifierSource": "minid"
            },
            "title": "Flybase MOD data",
            "types": [{"information": {"value": "MOD data"}}],
            "creators": [ {} ],
            "distributions": [{
                "@type": "DatasetDistribution",
                "@context": "https://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
                "identifier": {
                    "identifier": "minid:b9dm68",
                    "identifierSource": ""
                },
                "access": {
                    "@type": "Access",
                    "@context": "https://w3id.org/dats/context/sdo/access_sdo_context.jsonld",
                    "accessURL": "https://s3.amazonaws.com/mod-datadumps/FB_1.0.4_4.tar.gz",
                    "landingPage": "http://identifiers.org/minid:b9dm68"
                },
                "conformsTo": [{
                    "name": "tar.gz",
                    "type": {
                        "value": "application/x-compressed",
                        "valueIRI": ""
                    }
                }],
                "size": 7361930,
                "unit": {
                    "value": "byte",
                    "valueIRI": "http://purl.obolibrary.org/obo/UO_0000233"
                },
                "version": "1.0.4_4"
            }]
        },
        {
            "@type": "Dataset",
            "@id": "http://identifiers.org/minid:b9cm3t",
            "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
            "identifier": {
                "identifier": "minid:b9cm3t",
                "identifierSource": "minid"
            },
            "title": "A list of gene ontology associations for Drosophila obtained from the Gene Ontology Consortium.",
            "types": [{"information": {"value": "gene association data"}}],
            "creators": [ {} ],
            "distributions": [{
                "@type": "DatasetDistribution",
                "@context": "https://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
                "identifier": {
                    "identifier": "minid:b9cm3t",
                    "identifierSource": ""
                },
                "access": {
                    "@type": "Access",
                    "@context": "https://w3id.org/dats/context/sdo/access_sdo_context.jsonld",
                    "accessURL": "https://s3.amazonaws.com/mod-datadumps/GO/ANNOT/gene_association.fb.gz",
                    "landingPage": "http://identifiers.org/minid:b9cm3t"
                },
                "conformsTo": [{
                    "name": "tar.gz",
                    "type": {
                        "value": "application/x-compressed",
                        "valueIRI": ""
                    }
                }],
                "size": 2731033,
                "unit": {
                    "value": "byte",
                    "valueIRI": "http://purl.obolibrary.org/obo/UO_0000233"
                },
                "version": "Last updated 2.6.2018"
            }]
        },
        {
            "@type": "Dataset",
            "@id":  "http://identifiers.org/minid:b9m393",
            "@context": "https://w3id.org/dats/context/sdo/dataset_sdo_context.jsonld",
            "identifier": {
                "identifier": "http://identifiers.org/minid:b9m393",
                "identifierSource": "minid"
            },
            "title": "JSON files containing orthology derived from DIOPT v6.2 http://www.flyrnai.org/cgi-bin/DRSC_orthologs.pl",
            "types": [{"information": {"value": "orthology data"}}],
            "creators": [ {} ],
            "distributions": [{
                "@type": "DatasetDistribution",
                "@context": "https://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
                "identifier": {
                    "identifier": "http://identifiers.org/minid:b9m393",
                    "identifierSource": "minid"
                },
                "access": {
                    "@type": "Access",
                    "@context": "https://w3id.org/dats/context/sdo/access_sdo_context.jsonld",
                    "accessURL": "https://s3.amazonaws.com/mod-datadumps/ORTHO/orthology_FlyBase_1.0.0_2.json.tar.gz",
                    "landingPage": "http://identifiers.org/minid:b9m393"
                },
                "conformsTo": [
                    {
                        "name": "tar.gz",
                        "type": {
                            "value": "application/x-compressed",
                            "valueIRI": ""
                        }
                    },
                    {
                        "name": "json",
                        "type": {
                            "value": "application/json",
                            "valueIRI": ""
                        }
                    }
                ],
                "size": 2614596,
                "unit": {
                    "value": "byte",
                    "valueIRI": "http://purl.obolibrary.org/obo/UO_0000233"
                },
                "version": "DIOPT v6.2"
            }]
        }
    ],
    "distributions": [{
        "@type": "DatasetDistribution",
        "@context": "https://w3id.org/dats/context/sdo/dataset_distribution_sdo_context.jsonld",
        "identifier": {
            "identifier": "http://identifiers.org/minid:b9j69h",
            "identifierSource": "minid"
        },
        "access": {
            "@type": "Access",
            "@context": "https://w3id.org/dats/context/sdo/access_sdo_context.jsonld",
            "landingPage": "http://identifiers.org/minid/b9j69h",
            "accessURL": "https://nih-commons.s3.amazonaws.com/misc/agr-example.tgz"
        },
        "conformsTo": [{
            "name": "tar.gz",
            "type": {
                "value": "application/x-compressed",
                "valueIRI": ""
            }
        }],
        "size": -1,
        "unit": {
            "value": "byte",
            "valueIRI": "http://purl.obolibrary.org/obo/UO_0000233"
        },
        "version": ""
    }],
    "extraProperties": [
        {
            "category": "checksum",
            "categoryIRI": "http://purl.obolibrary.org/obo/NCIT_C43522",
            "values": [{
                "value": "6484968f81afac84857d02b573b0d589fb2f9582a2b920572830dc5781e0a53c",
                "valueIRI": ""
            }]
        },
        {
            "category": "checksum algorithm",
            "categoryIRI": "http://purl.obolibrary.org/obo/NCIT_C16275",
            "values": [{
                "value": "MD5",
                "valueIRI": ""
            }]
        }
    ]
}
"""


class FormatConversion(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_convert(self):
        print dats_jsonld.jsonld2rdf(jsonld_doc)

    def test_convert2(self):
        print dats_jsonld.jsonld2rdf(bdbag)

    def test_convert3(self):
        print dats_jsonld.jsonld2rdf(topmed)


    def test_query_creators(self):
        g =dats_jsonld.jsonld2graph(topmed)
        qres = g.query(
            """            
            SELECT DISTINCT ?dataset ?creator
               WHERE {
                  ?dataset a sdo:Dataset .
                  ?dataset sdo:creator ?creator                  
               }""")

        for row in qres:
            print("%s created by %s" % row)

    def test_query_files(self):
        g = dats_jsonld.jsonld2graph(bdbag)
        qres = g.query(
            """
            SELECT DISTINCT ?dataset ?file
            WHERE {
            
                                        
                ?dataset a sdo:Dataset.                
                ?dataset sdo:distribution ?distribution.
                ?distribution a sdo:DataDownload.
                ?distribution sdo:accessMode ?access.
                ?access sdo:contentUrl ?file.                                               
                
            }
            """)
        for row in qres:
            print("%s contains file %s" % row)