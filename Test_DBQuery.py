import unittest
from DBQuery import DBAccessObject
from mock import MagicMock, patch

class DBQueryTest(unittest.TestCase):

	def test_db_read(self):
		sql = DBAccessObject()
		sql.cursor = MagicMock()
		sql.cnx = MagicMock()
		
		sql.cursor.execute.return_value = None
		
		sentences = sql.cursor()
		
		self.assertEqual(sentences)

if __name__ == '__main__':
    unittest.main()