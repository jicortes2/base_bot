import db
from random import choice


# Public commands

def start(sender_id, command):
    return "IdeaBot a su servicio"

# Auxiliary methods

def not_found(sender_id, command, *args):
    """ Respuesta predeterminada para cuando un comando no existe """
    return 'El comando {} no existe'.format(command)
