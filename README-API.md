## ExTrack API

### Introduction
This is a simple API  based on Django and Django Rest 
Framework to keep a book of expenses up to date,
There is at the moment only two user roles : 

* simple users 
* admin user.

The admin users may create/update/delete any user
The simple users may create users but only 
update/delete their own account.

In the same fashion, simple users may create/update/delete records 
only if they are owners of this record, while
admin users can basically create/update/delete any record.

The API is accessed through HTTP with the following verbs:

* `GET`: used to retrieve users/records
* `POST`: used to create records/users
* `PUT`: used to update records/users
* `DELETE`: used to delete records/users

#### Exemples

* `GET http://localhost:8000/users` :  retrieve 
the list of all users (if logged as admin) or the info on the current user.
* `POST http://localhost:8000/users/` : create 
a new user with the data provided in the HTTP body request.
* `DELETE http://localhost:8000/users/8` : delete 
the user with `user_id=8` (admin only or owner of the account)

### Authentication

The authentication is made through a `POST` request whose header
contains the credentials in JSON format :

```{username: 'username', password: '*******'}```

With curl, you would authenticate doing:

```
[david@localhost ~]$ curl --header "Content-Type: application/json" -X POST \
 --data '{"username": "david", "password": "test"}' \
 http://localhost:8000/api-token-auth/ 
```

Then the /api-token-auth/ route will answer JSON data 
containing your authentication token (if the provided credentials
are correct):

```
{ "token": "b4a8a313eb062dbff8c7b9cfee28e9bcfddb9dc8",
  "user_id": 1, "username": "david", "is_staff": true }
```

Subsequent calls to the API must provide the obtained token
in the header's request:

```
curl -X GET http://127.0.0.1:8000/users/ -H \
'Authorization: Token b4a8a313eb062dbff8c7b9cfee28e9bcfddb9dc8'
```
