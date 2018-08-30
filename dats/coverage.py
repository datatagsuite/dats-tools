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


if __name__ == "__main__":
    schema_filename = "dataset_schema.json"
    context_filename = "dataset_obo_context.jsonld"
    schemas_path = os.path.join(os.path.dirname(__file__), "../json-schemas")
    obo_contexts_path = os.path.join(os.path.dirname(__file__), "../contexts/obo")
    schema_file = open(os.path.join(schemas_path, schema_filename))
    context_file = open(os.path.join(obo_contexts_path,context_filename))
    schema = json.load(schema_file)
    context = json.load(context_file)
    print(Coverage.json_schema_context_coverage(schema, context))



    #Coverage.json_schema_context_mapping(schema, context)