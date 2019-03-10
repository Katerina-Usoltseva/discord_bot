import unittest
from Server.Server import Server


class BotCommandsTest(unittest.TestCase):
    def setUp(self):
        self.server = Server()
        self.server.connect_db()

    def test_select_command(self):
        query = 'SELECT * FROM __python__.writer;'
        response, status = self.server.select_table_query(query)
        self.assertTrue(status)

    def test_insert_command(self):
        query = '''INSERT INTO __python__.writer (name) VALUES ('Автор');'''
        response, status = self.server.alter_table_query(query)
        self.assertTrue(status)

    def test_update_command(self):
        query = '''UPDATE __python__.writer SET name = 'Робертс' \
                   WHERE writer_id = (SELECT max(writer_id) FROM __python__.writer);'''
        response, status = self.server.alter_table_query(query)
        print(response)
        self.assertTrue(status)

    def test_delete_command(self):
        query = 'DELETE FROM __python__.writer  WHERE writer_id = (SELECT max(writer_id) FROM __python__.writer);'
        response, status = self.server.alter_table_query(query)
        self.assertTrue(status)

    def test_size_command(self):
        response, status = self.server.get_table_size_query()
        self.assertTrue(status)

    def tearDown(self):
            self.server.close_db()


if __name__ == '__main__':
    unittest.main()