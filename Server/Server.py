import psycopg2
from Server.config import config
from Server.Accessor import Accessor
from Server.Controller import Controller


class Server:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.controller = Controller()

    def connect_db(self):
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)
            self.cur = self.conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
        finally:
            if self.conn is None:
                print('Can\'t connect to database. Connection closed.')
                return False
        return True

    def close_db(self):
        try:
            # close the communication with the PostgreSQL
            self.conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')

    def execute_query(self, query, command):
        if command == '$size':
            return self.get_table_size_query()
        elif command in ('$update', '$delete', '$insert'):
            return self.alter_table_query(query[1:])
        else:
            # command is '$select':
            return self.select_table_query(query[1:])

    def get_table_size_query(self):
        response, status = '', False
        try:
            self.cur.execute(Accessor.accessor_get_size_writer)
            size = self.cur.fetchone()[0]
            response += 'Writer: {0} records \n'.format(size)
            self.cur.execute(Accessor.accessor_get_size_book)
            size = self.cur.fetchone()[0]
            response += 'Book: {0} records'.format(size)
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()  # rollback and continue the session
            return error, status

        status = True
        self.conn.commit()
        return response, status

    def alter_table_query(self, query):
        status = False
        try:
            self.cur.execute(query)
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            return error, status

        status = True
        self.conn.commit()
        return 'Operation succeeded', status

    def select_table_query(self, query):
        status = False
        try:
            self.cur.execute(query)
            records = [dict((self.cur.description[i][0], value)
                            for i, value in enumerate(row)) for row in self.cur.fetchall()]
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            return error, status

        status = True
        self.conn.commit()
        return records, status
