from . import connection


def project(json):
    name = json.name
    description = json.description
    source_link = json.source_link
    demo_link = json.demo_link
    tags = ','.join(json.tags)
    authors = ','.join(json.authors)
    id = json.id

    st = "UPDATE projects SET name=%s, description=%s, source_link=%s, demo_link=%s, images=%s, tags=%s, authors=%s WHERE id=%s" % (name, description, source_link, demo_link, images, tags, authors, id,)

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st)
    conn.commit()


def user(json):
    username = json.username
    fullname = json.name
    timezone = json.timezone
    bio = json.bio
    skills = ','.join(json.skills)
    interests = ','.join(json.interests)

    st = "UPDATE users SET fullname=%s, timezone=%s, bio=%s, skills=%s, interests=%s WHERE username=%s" % (fullname, timezone, bio, skills, interests, username, )

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st)
    conn.commit()
