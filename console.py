#!/usr/bin/python3
"""
This is the console.It is the entry point into this program
The console allows a user to interact with the database
    from the command line.
    it allows viewing, creating, deleting, etc models
"""

from models.base_model import BaseModel
from models import storage
import cmd
import re
from models.base_model import BaseModel
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review
classes = {
    # 'Amenity': Amenity,
    'BaseModel': BaseModel,
    # 'City': City,
    # 'Place': Place,
    # 'Review': Review,
    # 'State': State,
    # 'User': User
}


def parse_string(string):
    # regular expression to match words within quotes and words without quotes
    pattern = r'"([^"]*)"|(\S+)'
    # Find all matches in the string
    matches = re.findall(pattern, string)
    # Concatenate the non-empty groups from the matches
    result = [match[0] or match[1] for match in matches]
    return result


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Command: create

        Description:
        Create a new model and store it in the storage system.

        Usage:
        create <model_name>
        """
        if not arg:
            print('** class name missing **')
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            model = classes[arg]()
            model.save()
            print(model.id)

    def do_show(self, arg):
        """
        Command: show

        Description:
        Prints the string representation of an instance based on the class name
        and id

        Usage:
        show <model_name> <id>
        """
        if not arg:
            print('** class name missing **')
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        models = storage.all()
        if f'{args[0]}.{args[1]}' not in models:
            print('** no instance found **')
        else:
            print(models[f'{args[0]}.{args[1]}'])

    def do_destroy(self, arg):
        """
        Command: destroy

        Description:
        Deletes an instance based on the class name and id
        (saves the change into the JSON file)

        Usage:
        destroy <model_name> <id>
        """
        if not arg:
            print('** class name missing **')
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        models = storage.all()
        if f'{args[0]}.{args[1]}' not in models:
            print('** no instance found **')
        else:
            del models[f'{args[0]}.{args[1]}']
            storage.save()

    def do_all(self, arg):
        """
        Command: all

        Description:
        Prints all string representations of all instances of  <model_name>
        if no model name is provided, prints all instances

        Usage:
        all [<model_name>]
        """
        if not arg:
            models = storage.all()
            st = [value.__str__() for value in models.values()]
            print(st)
        elif arg in classes:
            models = storage.all()
            st = [value.__str__() for value in models.values()
                  if value.__class__.__name__ == arg]
            print(st)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Command: update

        Description:
        Updates an instance based on the model name and id
        by adding or updating attribute

        Usage:
        update <model_name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print('** class name missing **')
            return
        args = parse_string(arg)
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        models = storage.all()
        if f'{args[0]}.{args[1]}' not in models:
            print('** no instance found **')
            return
        instance = models[f'{args[0]}.{args[1]}']
        if len(args) < 3:
            print('** attribute name missing **')
            return
        if len(args) < 4:
            print('** value missing **')
            return
        # if not hasattr(instance, args[2]):  # check if attr exists in model?
        #     # print(f'{args[0]} has no {args[2]}')

        # type checks here, currently only places model
        place_types = {
            'number_rooms': int,
            'number_bathrooms': int,
            'max_guest': int,
            'price_by_night': int,
            'latitude': float,
            'longitude': float
        }
        if args[0] == 'Place' and args[2] in place_types:
            expected_type = place_types[args[2]]
            try:
                val = expected_type(args[3])
                setattr(instance, args[2], val)
                instance.save()

            except ValueError:
                print(f'{args[0]}.{args[2]} should be {expected_type}')
            # number_rooms = 0
            # number_bathrooms = 0
            # max_guest = 0
            # price_by_night = 0
            # latitude = 0.0
            # longitude = 0.0
        else:
            setattr(instance, args[2], args[3])
            instance.save()

    def do_quit(self, arg):
        """quit command exits the program"""
        return True

    def do_EOF(self, args):
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
