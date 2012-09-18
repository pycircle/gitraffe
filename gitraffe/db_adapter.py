from sqlite3 import connect
from structures import Repository
from os.path import expanduser

conn = connect(expanduser('~/.gitraffe/database.db'))

REPO = 'repositories'
REPO_ID = 'id'
REPO_NAME = 'name'
REPO_PATH = 'path'

def execute_query(query):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()

def init():
    query = 'CREATE TABLE IF NOT EXISTS %s (%s INTEGER PRIMARY KEY AUTOINCREMENT, %s TEXT, %s TEXT);' % (REPO, REPO_ID, REPO_NAME, REPO_PATH)
    execute_query(query)

def exists_repository(path):
    cur = conn.cursor()
    query = 'SELECT * FROM %s WHERE %s = "%s";' % (REPO, REPO_PATH, path)
    cur.execute(query)
    return cur.fetchone() != None

def add_repository(name, path):
    query = 'INSERT INTO %s(%s, %s) VALUES("%s", "%s");' % (REPO, REPO_NAME, REPO_PATH, name, path)
    execute_query(query)

def get_repositories():
    cur = conn.cursor()
    query = 'SELECT * FROM %s;' % (REPO)
    cur.execute(query)
    repositories = []
    for row in cur:
        repositories.append(Repository(row[0], row[1], row[2]))
    cur.close()
    return repositories

# This function will be probably unnecessary
def get_repository_by_path(path):
    cur = conn.cursor()
    query = 'SELECT * FROM %s WHERE %s = "%s";' % (REPO, REPO_PATH, path)
    cur.execute(query)
    row = cur.fetchone()
    repository = Repository(row[0], row[1], row[2])
    cur.close()
    return repository

def delete_repository(path):
    query = 'DELETE FROM %s WHERE %s = "%s";' % (REPO, REPO_PATH, path)
    execute_query(query)
