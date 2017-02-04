# Run the ExTrack API and clients

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

```
pip install -r requirements.txt
```

This will install 

* Django
* django-rest-framework
* django-cors-headers application 
* pytest
 
and all the dependencies.

If you you want install the requirements in your user directory, 
use the `--user` flag and don't forget to add 
the `~/.local/lib/python3.6/site-packages/`
to your `PYTHONPATH` environment variable. 

## Demo script

To check if everything is ok, run `demo_script.sh` at the root 
of your repository.
It will clone the repo, create the database schema and launch the webserver.
It will also ask you for the creation of an superuser.
 
At this point, you will be able to use the application by
opening `ui-js/index.html` in your browser and to start creating
users and records.