# Installation and use of the ExTrack API
## Requirements

Throughout this doc, we assume that the user is using a Linux system 
with the following requirements:
 
* a linux shell (bash/sh/ ...)
* a python shell and the pip program (https://pip.pypa.io)
* a recent browser allowing javascript execution (chromium/firefox in a late version)

The application of this doc to a different system (windows, *BSD, Minix, ...) 
should be possible with minimal changes.  

## Installation
 
In the command line interface, at the root of the project, execute: 

```pip install requirements.txt```

This will install 
* Django
* the django-rest-framework
* the django-cors-headers application, 
* pytest 
 
 and all the required dependencies.

If you you want install the requirements in your user directory, 
use the `--user` flag and don't forget to add the `~/.local/lib/python3.6/site-packages/`
to your `PYTHONPATH` environment variable. 

The use of virtual environments is not covered by this doc but should
still be possible.

## Deployment

TODO