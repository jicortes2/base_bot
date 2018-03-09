from psycopg2 import connect, IntegrityError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import urllib.parse as urlparse

"""
tables:
"""

ADMINS = [str(os.environ['JUAN_ID']), str(os.environ['CRIS_ID'])]
TOKEN = str(os.environ['TOKEN'])
