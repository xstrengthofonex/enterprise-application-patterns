from patterns.table_data_gateway.db import db

create_person_table = """\
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    numberOfDependents INTEGER)
"""

drop_person_table = """\
DROP TABLE IF EXISTS person
"""

def upgrade():
    with db.connect() as conn:
        conn.execute(create_person_table)

def downgrade():
    with db.connect() as conn:
        conn.execute(drop_person_table)

