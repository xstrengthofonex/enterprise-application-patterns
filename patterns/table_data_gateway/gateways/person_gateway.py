from patterns.table_data_gateway.db import db

class PersonGateway(object):
    @staticmethod
    def find_all():
        sql = "SELECT * FROM person"
        with db.connect() as conn:
            return conn.execute(sql).fetchall()

    @staticmethod
    def find_with_lastname(lastname):
        sql = "SELECT * FROM person WHERE lastname=:lastname"
        with db.connect() as conn:
            return conn.execute(sql, {'lastname':lastname}).fetchall()

    @staticmethod
    def find_where(condition, **params):
        sql = "SELECT * FROM person WHERE {}".format(condition)
        with db.connect() as conn:
            return conn.execute(sql, params).fetchall()

    @staticmethod
    def find_row(id):
        sql = "SELECT 1 FROM person WHERE id=:id"
        with db.connect() as conn:
            return conn.execute(sql, {'id':id}).fetchone()

    @staticmethod
    def update(id, firstname, lastname, numberOfDependents):
        sql = "UPDATE person "\
              "SET firstname=:firstname, lastname=:lastname, " \
              "numberOfDependents=:numberOfDependents "\
              "WHERE id=:id"
        with db.connect() as conn:
            conn.execute(sql, {'firstname':firstname, 'lastname':lastname,
                               'numberOfDependents':numberOfDependents, 'id':id})

    @staticmethod
    def insert(id, firstname, lastname, numberOfDependents):
        sql = "INSERT INTO person "\
              "VALUES (:id, :firstname, :lastname, :numberOfDependents)"
        with db.connect() as conn:
            conn.execute(sql, {'id':id, 'firstname':firstname, 'lastname':lastname,
                               'numberOfDependents':numberOfDependents})

    @staticmethod
    def delete(id):
        sql = "DELETE FROM person WHERE id=:id"
        with db.connect() as conn:
            conn.execute(sql, {'id': id})