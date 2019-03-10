import unittest
from Server.Server import Server


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.server = Server()

    def test_connect_db(self):
        self.server.connect_db()
        self.server.cur.execute('SELECT 1;')
        response = self.server.cur.fetchone()[0]
        self.assertEqual(response, 1, 'Something wrong with database connection')

    def tearDown(self):
        self.server.close_db()


if __name__ == '__main__':
    unittest.main()