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


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """quit command exits the program"""
        return True

    def do_EOF(self, args):
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
