#!/usr/bin/python3
""" Defines the entry point of the command interpreter. """
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb)"
    l_classes = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True

    def emptyline(self):
        """Do nothing when empty line."""
        pass

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def do_create(self, t_model):
        """Create a new class instance and print its id."""

        if not t_model:
            print("** class name missing **")

        elif t_model not in HBNBCommand.l_classes:
            print("** class doesn't exist **")

        else:
            dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'City': City, 'Amenity': Amenity, 'State': State,
                    'Review': Review}
            my_model = dict[t_model]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id
        """

        args = arg.split(' ')
        objdict = storage.all()
        if not arg:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """  Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
        objdict = storage.all()
        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        if len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation
            of all instances based or not on the class name
        """
        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file)
        """
        args = arg.split(' ')
        objdict = storage.all()

        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.l__classes:
            print("** class doesn't exist **")
        if len(args) == 1:
            print("** instance id missing **")
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
        if len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
