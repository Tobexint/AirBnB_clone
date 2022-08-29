This project is the first step towards building a full web application(an AirBnB clone). This first step consists of a custom command-line interface for data management and the base classes for the storage of this data.
Step 1: Write a command interpreter (The Console)
Functionalities of this command interpreter:
-Create a new object (ex: a new User or a new Place)
-Retrieve an object from a file, a database etc...
-Do operations on objects (count, compute stats, etc...)
-Update attributes of an object
-Destroy an object
Console and Command Usage
The console is a Unix shell-like command line user interface provided by the python CmdModule It prints a prompt and waits for the user for input, for our project we used (hbnb)

-Create a new object (ex: a new User or a new Place)
-Retrieve an object from a file, a database etc...
-Do operations on objects (count, compute stats, etc...)
-Update attributes of an object
-Destroy an object
Execution
Your shell should work like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
