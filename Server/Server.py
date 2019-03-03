import psycopg2
from Server.config import config


class Server:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect_db(self):
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)

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
            self.cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')

    def do_query_db(self, query):
        status = 'ok'
        print(query)
        self.cur = self.conn.cursor()
        self.cur.execute(query[1:])
        response = self.cur.fetchone()[2]
        print(response)
        self.conn.commit()

        return status, response
