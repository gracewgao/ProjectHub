from . import connection

def projects(project):
    st = "SELECT id FROM projects WHERE name=%s" % (project,)

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st)

    return cur.fetchone()

def users(username):
    st = "SELECT * FROM users WHERE username=%s" % (username,)

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st)

    return cur.fetchone()