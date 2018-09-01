import json
import os

class Coverage:
    """
    A class that compute the overlap between two structures
    """

    jsonld_ignored_keys = ["@id", "@context", "@type"]


    @staticmethod
    def json_schema_context_coverage(schema, context):
        "Method to compute the coverage of a context file for a particular json-schema"

        overlap = []
        diff = []

        for field in schema["properties"]:
            if field not in Coverage.jsonld_ignored_keys:
                if field in context["@context"]:
                    overlap.append(field)
                else:
                    diff.append(field)
        return overlap, diff

    @staticmethod
    def json_schema_context_mapping(schema, *contexts):
        "Method to retrieve the mapping between a schema and multiple context files"
        mappings = {}

        for field in schema["properties"]:
            terms = []
            if field not in Coverage.jsonld_ignored_keys:
                for context in contexts:
                    #print(context)
                    if field in context["@context"]:
                        if "@id" in context["@context"][field]:
                            terms.append(context["@context"][field]["@id"])
                        else:
                            terms.append(context["@context"][field])
                    else:
                        terms.append("")
                if field in mappings:
                    previous_terms = mappings[field]
                    terms.append(previous_terms)
                mappings.update( { field : terms })
        print(mappings)

if __name__ == "__main__":
    schema_filename = "dataset_schema.json"
    obo_context_filename = "dataset_obo_context.jsonld"
    sdo_context_filename = "dataset_sdo_context.jsonld"
    schemas_path = os.path.join(os.path.dirname(__file__), "../json-schemas")
    obo_contexts_path = os.path.join(os.path.dirname(__file__), "../contexts/obo")
    sdo_contexts_path = os.path.join(os.path.dirname(__file__), "../contexts/sdo")
    schema_file = open(os.path.join(schemas_path, schema_filename))
    obo_context_file = open(os.path.join(obo_contexts_path,obo_context_filename))
    sdo_context_file = open(os.path.join(sdo_contexts_path, sdo_context_filename))
    schema = json.load(schema_file)
    obo_context = json.load(obo_context_file)
    sdo_context = json.load(sdo_context_file)
    print(Coverage.json_schema_context_coverage(schema,obo_context))


    Coverage.json_schema_context_mapping(schema, sdo_context, obo_context)