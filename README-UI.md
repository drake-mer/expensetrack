## Command line interface and tests

The folder `ui-cli` contains a python module to interact with the API (`cli_extrack.py`).
 
This module can deal with user authentication and can be used to script any 
operations wished with the API. It is also used to run  a test suit based 
on the `pytest` framework.

To launch the tests, run `pytest` in your terminal at the root of the project. 
Use `pytest --help` to learn about additional possibilities.

## Graphical User Interface

The graphical user interface is a javascript/HTML application (single page) 
doing HTTP request to the webserver using based on bootstrap/jquery.

The design is simple and serves the purpose of demonstrating the 
possibilities of the API.

You can create/update/delete users and records from 
this user interface.

The app display basic stats on the expenses. You can also select 
a week against which you want to filter expenses.

### Possible improvements
* Do A--B filtering on dates
* Do filtering by level of expenses
* Display stats and graphs on expense
* Improve ergonomy of input forms
