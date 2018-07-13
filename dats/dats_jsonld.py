from pyld import jsonld
import json
from os.path import join

from rdflib import Graph, plugin
from rdflib.serializer import Serializer

def jsonld2graph(jsonld_doc):
    g = Graph().parse(data=jsonld_doc, format='json-ld')
    return g

def jsonld2rdf(jsonld_doc):
    g = jsonld2graph(jsonld_doc)
    return g.serialize(format='n3', indent=4)


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
