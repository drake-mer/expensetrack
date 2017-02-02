# ExTrack : simple HTTP REST API for expense tracking

## ExTrack API

### Introduction
This is a simple API  based on Django and Django Rest Framework to keep a book of expenses up to date,
There is at the moment only two user roles : 

* simple users 
* admin user.

The admin users may create/update/delete any user
The simple users may create users but only do update/deletion on the very account with which they are logged.

In the same fashion, simple users may create/update/delete records only if they are owners of this record, while
admin users can basically create/update/delete any record.

The API is accessed through HTTP with the following verbs:

* GET: used to retrieve users/records
* POST: used to create records/users
* PUT: used to update users
* DELETE: used to delete users

### Exemples

* `GET http://localhost:8000/users` :  retrieve the list of all users (if logged as admin) or the info on the current user.
* `POST http://localhost:8000/users/` : create a new user with the data provided in the HTTP body request.
* `DELETE http://localhost:8000/users/8` : delete the user with user_id=8 (only if you are admin or this user)

### Authentication
With curl, you would do:
where the Token string is fetched from the server upon correct authentication

`curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'`

## Command line interface

The folder ui-cli contains a python module to interact with the API (cli_extrack.py). This module
can deal with user authentication and can be used to script any operations wished with the API.

This module is also used to run a whole bunch of test with the pytest framework.

To launch the tests, run the `pytest` command at the root of the project. Use `pytest --help`
for additional options.


## Graphical User Interface

The graphical user interface is a javascript/HTML application doing HTTP request to the webserver.
Its design is really basic and serves the purpose of demonstrating the possibilities of the API.

You can create/update/delete users and records from this user interface.
You can also display basic stats on the expenses, do filtering by week.

Further improvements may include :
* filter by A-B dates
* filter by level of expenses
* display stats on expense
* improve ergonomy of input forms










