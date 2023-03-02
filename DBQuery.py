from mysql import connector
from connector import errorcode

config = {
	'host': 'localhost',
	'user': 'me',
	'password': 'mypassword',
	'database': 'mydatabase'
}

class DBAccessObject:
	def __init__(self):
		self.cursor = None
		self.cnx = None

	def db_read(self, query, params=None):
		try:
			self.cnx = connector.connect(**config)
			self.cursor = self.cnx.cursor(dictionary=True)
			if params:
				self.cursor.execute(query, params)
			else:
				self.cursor.execute(query)

			entries = self.cursor.fetchall()
			self.cursor.close()
			self.cnx.close()

			content = []

			for entry in entries:
				content.append(entry)

			return content

		except connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("User authorization error")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database doesn't exist")
			else:
				print(err)
		else:
			self.cnx.close()
		finally:
			if self.cnx.is_connected():
				self.cursor.close()
				self.cnx.close()
				print("Connection closed")