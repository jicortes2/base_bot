import db
from random import choice

TOKEN = str(db.os.environ['TOKEN'])
# Public commands

def start(sender_id, command):
    return "BaseBot at your service"

# Admin commands
def masterdb(sender_id, command, statement):
    """ Run a SQL command """
    if str(sender_id) in db.ADMINS:
        if db.custom_statement(statement):
            return '"{}" was correctly executed'.format(statement)
        else:
            return 'There was a problem executing "{}"'.format(statement)
    else:
        return 'Your are not authorized to run this command'
# Auxiliary methods

def not_found(sender_id, command, *args):
    """ Default answer for wrong commands """
    return 'The command {} doesn"t exists'.format(command)
