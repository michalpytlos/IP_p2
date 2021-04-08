# Meme generator

Project 2 of the Intermediate Python Nanodegree <br>
Michal Pytlos, April 2021

## Overview
This is a tool for generating memes - images with overlaid quotes. Memes can be generated either randomly from the images and quotes kept in the app's _data directory or from the user input. The application can be run either from a command line or via a web browser (Flask app). 

## Prerequisites
* Python 3.6.8 or higher
* pdftotext CLI utility
## Installation
1. Navigate into the project's directory
2. Create a dedicated virtual env: `python -m venv <venv_name>`
3. Activate the created virtual env: `source <venv_name>/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
## Usage
Activate the virtual env before using the CLI and/or the Flask app. 
### CLI
The script `meme.py` creates a meme and prints the path to the generated image. 

It has three optional parameters:
* `path` - path to the base image
* `body` - body of the quote
* `author` - author of the quote (required if body is provided) <br>

Example usage:
* Generate a random meme: `python meme.py`
* Generate a meme from the user input: `python meme.py --path <path/to/file> --body <body> --author <author>`
* Display help: `python meme.py --help`

### Flask app
1. Tell Flask where to find the app:
    * Navigate into the project's directory
    * Execute `export FLASK_APP=app` (on Windows: `set FLASK_APP=app`) 
2. Start the Flask server: `flask run`
3. Flask will print the IP address and the port number at which the app can be accessed (these can also be specified directly via the -h and -p flags)
4. Generate memes at random of from the user input using the GUI in the web browser
## Sub-packages
### QuoteEngine
Sub-package for extracting quotes from a variety of file types. The package consists of the following single-class modules:
* `ingestor_interface` - Interface for classes capable of extracting quotes from files.
* `pdf_ingestor` - Realizes the ingestor interface for pdf input files. Utilizes the `pdftotext` CLI utility via `subprocess` to extract the quotes.
* `docx_ingestor` - Realizes the ingestor interface for docx input files. Utilizes the `docx` package to extract the quotes.
* `txt_ingestor` - Realizes the ingestor interface for txt input files.
* `csv_ingestor` - Realizes the ingestor interface for csv input files. Utilizes the `pandas` package to extract the quotes.
* `ingestor` - Encapsulates all the ingestors to provide one interface to extract quotes from any of the supported file type.
* `quote_model` - quote model used by the ingestors.

The `tests` directory contains unit tests for this sub-package. To execute the tests run `pytest` from the app's directory.
### MemeGenerator
Sub-package for generating memes. The package consists of a single-class module `meme_generator`. The module utilizes the Python Imaging Library `Pillow` to generate memes and is dependant on the `QuoteEngine` package for extraction of quotes from input files.