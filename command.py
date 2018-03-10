import db
from random import choice

TOKEN = str(db.os.environ['TOKEN'])
# Public commands

def start(sender_id, command):
    return "SplitBot a su servicio"

# Admin commands
def masterdb(sender_id, command, statement):
    """ Corre un comando en SQL """
    if str(sender_id) in db.ADMINS:
        if db.custom_statement(statement)
            return '"{}" se ejecuto correctamente'.format(statement)
        else:
            return 'Hubo un problema al ejecutar "{}"'.format(statement)
    else:
        return 'No estas autorizado para ejecutar este comando'
# Auxiliary methods

def not_found(sender_id, command, *args):
    """ Respuesta predeterminada para cuando un comando no existe """
    return 'El comando {} no existe'.format(command)
