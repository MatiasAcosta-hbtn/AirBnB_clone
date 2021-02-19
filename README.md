![](https://camo.githubusercontent.com/9ebbf60e208b031d4dcf7db6ffc19fe0339d0ff3/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67)

<h1 align ="center"> AIRBNB CLONE </h1><br>

# AirBnb Clone Console
A Command Interpreter to Manage AirBnb objects.

## Project Notes

### Environment
Files interpreted/run on Ubuntu 14.04 LTS with Python 3

### Style
All code is written in accordance with Pep8 https://www.python.org/dev/peps/pep-0008/

## How to use the Console

## To start:
* Interactive mode, `$ ./console.py`, and you will prompted with `(hbnb)`
*Non-interactive mode, `$ echo "help" | ./console.py`

## To close:
* Type either `EOF`(Ctrl + D) or `quit`

## Command usage of Console:

* `help`
  * Usage: `help`
  * Documentation/help provided
  
  Example
  
  ```
  $ ./console.py
  hbnb) help 

  Documented commands (type help <topic>):
  ========================================
  EOF  all  create  destroy  help  quit  show  update
  ```

* `create`
  * Usage: `create <Class Name>`
  * Creates a new instance of a class, saves it (to the JSON file) and prints the `id`

  Example:

  ```
  $ ./console.py
  (hbnb) create User
  e1fe6e2c-8d16-4997-8b46-d355fc4158a7
  (hbnb) 
  ```

* `show`
  * Usage: `show <Class Name> <ID Instance>`
  * Prints the string representation of an instance based on the class name and `id`

  Example:

  ```
  $ ./console.py
  (hbnb) create User
  e1fe6e2c-8d16-4997-8b46-d355fc4158a7
  (hbnb) show User e1fe6e2c-8d16-4997-8b46-d355fc4158a7
  [User] (e1fe6e2c-8d16-4997-8b46-d355fc4158a7) {'id': 'e1fe6e2c-8d16-4997-8b46-d355fc4158a7', 'created_at': datetime.datetime(2021, 2, 18, 23, 1, 31, 450042), 'updated_at': datetime.datetime(2021, 2, 18, 23, 1, 31, 451723)}
  ```

  
* `destroy`
  * Usage: `destroy <Class Name> <ID Instance>`
  * Deletes an instance based on the class name and `id` (save the change into the JSON file). 

  Example:

  ```
  $ ./console.py
  (hbnb) create Review
  1d5adc89-36dc-4325-8e84-fa8443a987a9
  (hbnb) destroy Review 1d5adc89-36dc-4325-8e84-fa8443a987a9
  (hbnb) 
  ```

* `all`
  * Usage: `all` or `<Class Name> all`
  * Prints all string representation of all instances based or not on the class name.

  Example:

  ```
  $ ./console.py
  (hbnb) all
  ["[User] (13cedb31-39b2-4ef9-8965-28957886df86) {'id': '13cedb31-39b2-4ef9-8965-28957886df86', 
  'created_at': datetime.datetime(2021, 2, 18, 21, 23, 35, 933490), 
  'updated_at': datetime.datetime(2021, 2, 18, 21, 23, 35, 933519)}", "[User] (e1fe6e2c-8d16-4997-8b46-d355fc4158a7) {'id': 'e1fe6e2c-8d16-4997-8b46-d355fc4158a7', 
  'created_at': datetime.datetime(2021, 2, 18, 23, 1, 31, 450042), 
  'updated_at': datetime.datetime(2021, 2, 18, 23, 1, 31, 451723)}", "[Review] (c4a0c5e5-e761-4674-8201-878cf83a7a5d) {'id': 'c4a0c5e5-e761-4674-8201-878cf83a7a5d', 'created_at': datetime.datetime(2021, 2, 18, 23, 3, 36, 274393),
   'updated_at': datetime.datetime(2021, 2, 18, 23, 3, 36, 274633)}"]
  (hbnb) all Review
  ["[Review] (c4a0c5e5-e761-4674-8201-878cf83a7a5d) {'id': 'c4a0c5e5-e761-4674-8201-878cf83a7a5d', 'created_at': datetime.datetime(2021, 2, 18, 23, 3, 36, 274393), 'updated_at': datetime.datetime(2021, 2, 18, 23, 3, 36, 274633)}"]
  ```

* `update`
  * Usage: `update <Class Name> <Id Instance> <Attribute Name> <Value>`
  * Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)

  ```
  $ ./console.py
  (hbnb) all
  []
  (hbnb) create User
  b54c1240-4b9b-4459-86d6-0a77288cf5ef
  (hbnb) all
  ["[User] (b54c1240-4b9b-4459-86d6-0a77288cf5ef) 
  {'id': 'b54c1240-4b9b-4459-86d6-0a77288cf5ef', 'created_at': datetime.datetime(2021, 2, 18, 23, 9, 35, 250970), 
  'updated_at': datetime.datetime(2021, 2, 18, 23, 9, 35, 250999)}"]
  (hbnb) update User b54c1240-4b9b-4459-86d6-0a77288cf5ef name "MatiasTuPapi"
  (hbnb) show User b54c1240-4b9b-4459-86d6-0a77288cf5ef
  [User] (b54c1240-4b9b-4459-86d6-0a77288cf5ef)
   {'id': 'b54c1240-4b9b-4459-86d6-0a77288cf5ef', 'created_at': datetime.datetime(2021, 2, 18, 23, 9, 35, 250970),
    'updated_at': datetime.datetime(2021, 2, 18, 23, 9, 35, 250999), 'name': 'MatiasTuPapi'}
  ```

## Handle Errors in the Console

### When an error occurs, the console will handle it and give a corresponding message

### Create Errors

 * If the class name is missing, print ** class name missing ** 
 * If the class name doesn’t exist, print ** class doesn't exist **

  ```
  $ ./console.py
  (hbnb) create
  ** class name missing **
  (hbnb) create MyModel
  ** class doesn't exist **
  ```
 
### Show Errors

 * If the class name is missing, print ** class name missing **
 * If the class name doesn’t exist, print ** class doesn't exist **
 * If the id is missing, print ** instance id missing **
 * If the instance of the class name doesn’t exist for the id, print ** no instance found **

 ```
  $ ./console.py
  (hbnb) show
  ** class name missing **
  (hbnb) show MyModel
  ** class doesn't exist **
  (hbnb) show BaseModel
  ** instance id missing **
  (hbnb) show BaseModel 12345678
  ** no instance found **
 ```

### Destroy Errors

 * If the class name is missing, print ** class name missing **
 * If the class name doesn’t exist, print ** class doesn't exist **
 * If the id is missing, print ** instance id missing **
 * If the instance of the class name doesn’t exist for the id, print ** no instance found **

 ```
 $ ./console.py
 (hbnb) destroy
 ** class name missing **
 (hbnb) destroy NoModel
 ** class doesn't exist **
 (hbnb) destroy User
 ** instance id missing **
 (hbnb) destroy User 1245
 ** no instance found **
```

### all Errors

 * If the class name doesn’t exist, print ** class doesn't exist **

 ```
 $ ./console.py
 (hbnb) all AnyModel
 ** class doesn't exist **
 ``` 

### update Errors

* Usage `update <class name> <id> <attribute name> "<attribute value>`

* If the class name is missing, print ** class name missing ** 
* If the class name doesn’t exist, print ** class doesn't exist **
* If the id is missing, print ** instance id missing **
* If the instance of the class name doesn’t exist for the id, print ** no instance found **
* If the attribute name is missing, print ** attribute name missing **
* If the value for the attribute name doesn’t exist, print ** value missing **

```
$ ./console.py
(hbnb) all
["[User] (b54c1240-4b9b-4459-86d6-0a77288cf5ef)
 {'id': 'b54c1240-4b9b-4459-86d6-0a77288cf5ef', 'created_at': datetime.datetime(2021, 2, 18, 23, 9, 35, 250970), 
 'updated_at': datetime.datetime(2021, 2, 18, 23, 9, 35, 250999), 'name': 'MatiasTuPapi'}"]
(hbnb) update
** class name missing **
(hbnb) update Buho
** class doesn't exist **
(hbnb) update User
** instance id missing **
(hbnb) update User 1245
** no instance found **
(hbnb) update User b54c1240-4b9b-4459-86d6-0a77288cf5ef
** attribute name missing **
(hbnb) update User b54c1240-4b9b-4459-86d6-0a77288cf5ef name2
** value missing **
```

### Files

### [Console](./console.py)
Module for Main Console
* `class HBNBCommand(cmd.Cmd)` includes:
  * `emptyline(self)` : method to handle empty line
  * `do_quit(self, line)` : quit command method to exit console
  * `do_create(self, arg)` : method to make new instance, saves it, and print id
  * `do_show(self, arg)` : method to print string representation of an instance based on class name/id
  * `do_destroy(self, arg)` : method to deletes instance based on class name/id
  * `do_all(self, arg)` : prints string representation of all instances or all instances of a class
  * `do_update(self, arg)` : method to update instance based on class name/id by adding/updating attribute
  * `do_EOF(self, arg)` : method to handle the signal EOF
  * `count(self, arg)` : Method print the numbers of the instances of a class
  * `default`: method that handles any command not contemplated in functions do_foo

### [Base Model](./models/base_model.py)
Module for Base Model
* `class BaseModel` includes:
  * `def __init__(self, *args, **kwargs)` : method to initialize instance
  * `def save(self)` : method to update attributes `updated_at` with current datetime.
  * `def to_json(self)` : method to return dictionary of all key/values of instance and teh class name
  * `def __str__(self)` : method to print dictionary of attributes of the instance.

### [Amenity](./models/amenity.py)
Module for Amenity Model
* `class Amenity` includes:
  * Inherit all methods and attributes from BaseModel because it is a subclass of it
  
  ##### Public class attributes
  * name: string - empty string


### [City](./models/city.py)
Module for City Model
* `class City` includes:
  * Inherit all methods and attributes from BaseModel because it is a subclass of it

  ##### Public class attributes
  * state_id: string - empty string: it will be the State.id
  * name: string - empty string

### [Place](./models/place.py)
Module for Place Model
* `class Place` includes:
  * Inherit all methods and attributes from BaseModel because it is a subclass of it

  ##### Public class attributes
  * city_id: string - empty string: it will be the City.id
  * user_id: string - empty string: it will be the User.id
  * name: string - empty string
  * description: string - empty string
  * number_rooms: integer - 0
  * number_bathrooms: integer - 0
  * max_guest: integer - 0
  * price_by_night: integer - 0
  * latitude: float - 0.0
  * longitude: float - 0.0
  * amenity_ids: list of string - empty list: it will be the list of Amenity.id later

### [Review](./models/review.py)
Module for Review Model
* `class Review` includes:
  * Inherit all methods and attributes from BaseModel because it is a subclass of it

  ##### Public class attributes
  * place_id: string - empty string: it will be the Place.id
  * user_id: string - empty string: it will be the User.id
  * text: string - empty string

### [State](./models/state.py)
Module for State Model
* `class State` includes:
  * Inherit all methods and attributes from BaseModel because it is a subclass of it

  ##### Public class attributes
  * name: string - empty string

### [User](./models/user.py)
Module for User Model
*`class User` includes:
  * Inherit all methods and attributes from BaseModel because it is a subclass of it

  ##### Public class attributes
  * email: string - empty string
  * password: string - empty string
  * first_name: string - empty string
  * last_name: string - empty string

### [Init](./models/__init__.py)
* initializes package

### [File Storage](./models/engine/file_storage.py)
Module for serializing and deserializing instances and JSON
* `class FileStorage` includes:
  * `def all(self)` : methods to return __objects
  * `def new(self, obj)` : method to set obj in __objects with key/value pair 
  * `def save(self)` : method to serialize __objects to JSON file
  * `def reload(self)` : method to deserialize the JSON to __objects

## Test Files : Unit Tests for respectively named files

#### [Test Amenity](./tests/test_models/test_amenity.py) -> Test for the class Amenity

#### [Test Base Model](./tests/test_models/test_base_model.py) -> Test for the class BaseModel

#### [Test City](./tests/test_models/test_city.py) -> Test for the class City

#### [Test Place](./tests/test_models/test_place.py) -> Test for the class 

#### [Test Review](./tests/test_models/test_review.py) -> Test for the class 

#### [Test State](./tests/test_models/test_state.py) -> Test for the class 

#### [Test User](./tests/test_models/test_user.py) -> Test for the class 

#### [Test FileStorage](./tests/test_models/test_engine/test_file_storage.py) -> Test for the class 


## Authors
* Matias Acosta, <a href='https://github.com/MatiasAcosta-hbtn'>Github</a>
* Martin Saavedra, <a href='https://github.com/martinmsaavedra'>Github</a>