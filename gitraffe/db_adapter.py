import sqlite3
from structures import Repository
conn = sqlite3.connect('database.db')

def execute_query(query):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()

def init():
    query = 'CREATE TABLE IF NOT EXISTS repositories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, path TEXT);'
    execute_query(query)

def add_repository(name, path):
    query = 'INSERT INTO repositories(name, path) VALUES("' + name + '", "' + path + '");'
    execute_query(query)

def get_repositories():
    cur = conn.cursor()
    query = 'SELECT * FROM repositories;'
    cur.execute(query)
    repositories = []
    for row in cur:
        repositories.append(Repository(row[0], row[1], row[2]))
    cur.close()
    return repositories

def get_repository_by_name(name):
    cur = conn.cursor()
    query = 'SELECT * FROM repositories WHERE name = "' + name + '";'
    cur.execute(query)
    row = cur.fetchone()
    repository = Repository(row[0], row[1], row[2])
    cur.close()
    return repository

# TODO delete_repository!