import unittest
from DBQuery import DBAccessObject
from mock import MagicMock, patch

class DBQueryTest(unittest.TestCase):

	def test_db_read(self):
		sql = DBAccessObject()
		sql.cursor = MagicMock()
		sql.cnx = MagicMock()
		
		self.assertEqual()


if __name__ == '__main__':
    unittest.main()