# dats-tools

[![Build Status](https://travis-ci.org/datatagsuite/dats-tools.svg?branch=master)](https://travis-ci.org/datatagsuite/dats-tools)

Python code to deal with the DATS model.

The python code included in the repository validates the DATS JSON schemas and the DATS JSON instances against the schemas.
To execute the code, it is recommended to use a virtual environment, following these steps:

1. If not already installed in your system, first install the virtual environment via `pip`:
   `pip install virtualenv`
1. Create a virtual environment:
   `virtualenv venv`
1. Then, activate the virtual environment:
  `source venv/bin/activate`
1. Install the requirements:
  `pip install -r requirements.txt`
1. Download the schemas, contexts and instance data:
   `bash -x get_schemas_contexts_data.sh`
1. Finally, you can inspect and run the tests to validate the DATS schemas and JSON instances against the schemas.
   `python setup.py test`

