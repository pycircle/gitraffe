import sqlite3
from structures import Repository
conn = sqlite3.connect('database.db')

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
    query = 'CREATE TABLE IF NOT EXISTS ' + REPO + ' (' + REPO_ID + ' INTEGER PRIMARY KEY AUTOINCREMENT, ' + REPO_NAME + ' TEXT, ' + REPO_PATH + ' TEXT);'
    execute_query(query)

def add_repository(name, path):
    query = 'INSERT INTO ' + REPO + '(' + REPO_NAME + ', ' + REPO_PATH +') VALUES("' + name + '", "' + path + '");'
    execute_query(query)

def get_repositories():
    cur = conn.cursor()
    query = 'SELECT * FROM ' + REPO +';'
    cur.execute(query)
    repositories = []
    for row in cur:
        repositories.append(Repository(row[0], row[1], row[2]))
    cur.close()
    return repositories

def get_repository_by_name(name):
    cur = conn.cursor()
    query = 'SELECT * FROM ' + REPO + ' WHERE ' + REPO_NAME + ' = "' + name + '";'
    cur.execute(query)
    row = cur.fetchone()
    repository = Repository(row[0], row[1], row[2])
    cur.close()
    return repository

def delete_repository(name):
    query = 'DELETE FROM ' + REPO + ' WHERE ' + REPO_NAME + ' = ' + name + ';'
    execute_query(query)
