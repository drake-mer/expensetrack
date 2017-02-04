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

The use a of virtual environments is not covered by this doc but is 
quite possible with minor tweaks.

## Demo script

To check if everything is ok, a script `demo_script.sh` has
been included for a quick start. It doesn't install dependencies,
you will have to do it by hand.