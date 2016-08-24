import os
import time

class TempFile(object):
	def __init__(self, name):
		self.name = name

	def __enter__(self):
		working_path = os.getcwd()
		self.temp_file_name = os.path.join(working_path, self.name)
		self.temp_file = open(self.temp_file_name, 'w')
		return self.temp_file

	def __exit__(self, *args):
		print "in __exit__"
		self.temp_file.close()
		os.remove(self.temp_file_name)
		return False

def open_temp_file(name):
	return TempFile(name)

def test():
	with TempFile('temp.txt') as f:
		f.write('Hello world')
		f.flush()
		raise Exception('sorry')
		time.sleep(10)

if __name__ == '__main__':
	test()