from psycopg2 import connect, IntegrityError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import urllib.parse as urlparse

"""
tables:
"""

ADMINS = [str(os.environ['JUAN_ID']), str(os.environ['CRIS_ID'])]
TOKEN = str(os.environ['TOKEN'])

def _access(option=True):
    """ Returns connection to ideabot database  """
    return connect(
                    dbname=os.environ["DB_NAME"],
                    user=os.environ["DB_USER"],
                    password=os.environ["DB_PASS"],
                    host=os.environ["DB_HOST"],
                    port=os.environ["DB_PORT"]
                )


def custom_statement(statement):
    """ Returns true if the thing is added to the table """
    try:
        conn = _access()
        cur = conn.cursor()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute("{}".format(statement)
        conn.close()
        return True
    except IntegrityError:
        return False
