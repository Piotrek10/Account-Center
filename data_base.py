import sqlite3

# conn = sqlite3.connect('log.db')
# c = conn.cursor()

# c.execute("""CREATE TABLE logs(		
# 		id_name,
# 		link text,
# 		login text,
# 		password text)
# 	""")

# conn.commit()

class Account:
	def __init__(self):
		self.conn = sqlite3.connect('log.db')
		self.c = self.conn.cursor()

	def add_account(self, name, link, login, passwd):
		with self.conn:
			self.c.execute("INSERT INTO logs VALUES (:name, :link, :login, :password)",
				{'name':name, 'link':link, 'login': login, 'password':passwd})

	def get_password_by_name(self, name):
		self.c.execute("SELECT password FROM logs WHERE id_name = :name", {'name':name})
		return self.c.fetchall()[0][0]

	def get_record_by_name(self, name):
		self.c.execute("SELECT * FROM logs WHERE id_name = :name", {'name':name})
		return self.c.fetchall()

	def get_link_by_name(self, name):
		self.c.execute("SELECT * FROM logs WHERE id_name = :name", {'name':name})
		return self.c.fetchall()[0][1]

	def get_login_by_name(self, name):
		self.c.execute("SELECT * FROM logs WHERE id_name = :name", {'name':name})
		return self.c.fetchall()[0][2]

	def remove_record(self, login):
		with self.conn:
			self.c.execute("DELETE from logs where login = :login", {'login':login})

	def get_all_records(self):
		self.c.execute("SELECT * FROM logs")
		record_list = ""
		for row in self.c.fetchall():
			record_list += str(row) + 2*"\n"
		return record_list

	def update_password(self, old_password, new_password):
		self.c.execute("SELECT password FROM logs")
		passwords = [str(password[0]) for password in self.c.fetchall()]
		if old_password not in passwords:
			return False
		else:
			self.c.execute("UPDATE logs SET password = :new_password WHERE password = :old_password", {'new_password':new_password, 'old_password':old_password})
			self.conn.commit()
			return True

	def __del__(self):
		self.conn.close()





