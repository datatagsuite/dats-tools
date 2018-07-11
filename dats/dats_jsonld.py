from pyld import jsonld
import json
from os.path import join

from rdflib import Graph, plugin
from rdflib.serializer import Serializer

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
        "@type": "Access",
        "landingPage": "http://identifiers.org/pdb/5AEM",
        "accessURL": "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=FASTA&compression=NO&structureId=5AEM"
      },
      "storedIn" :
      {
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
        "@type": "Access",
        "landingPage": "http://identifiers.org/pdb/5AEM",
        "accessURL": "http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId=5AEM"
      },
      "storedIn" :
      {
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
      "@context": {
        "sdo": "https://schema.org/",
        "DatasetDistribution": "sdo:DataDownload",
        "title": {
          "@id": "sdo:name",
          "@type": "sdo:Text"
        },
        "description": {
          "@id": "sdo:description",
          "@type": "sdo:Text"
        },
        "storedIn": {
          "@id": "sdo:includedInDataCatalog",
          "@type": "sdo:DataCatalog"
        },
        "version": "sdo:version",
        "licenses": "sdo:license"
      },
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
        "@type": "Access",
        "landingPage": "http://identifiers.org/pdb/5AEM",
        "accessURL": "http://www.rcsb.org/pdb/files/5AEM.pdb.gz"
      },
      "storedIn" :
      {
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



g = Graph().parse(data=jsonld_doc, format='json-ld')
print(g.serialize(format='n3', indent=4))


#doc = json.load(open(join("../json-instances/", "PDB-5AEM.jsonld")))

# print("loaded jsonld", doc)
#
# context = json.load(open(join("../json-schemas/contexts/", "dataset_sdo_context.jsonld")))
#
# print("loaded context")
#
# compacted = jsonld.compact(doc, context)
#
# print("-------------COMPACTED")
#
# print(json.dumps(compacted, indent=2))
#
# expanded = jsonld.expand(compacted)
#
# print("-------------EXPANDED")
#
# print(json.dumps(expanded, indent=2))
#
# flattened = jsonld.flatten(compacted)
