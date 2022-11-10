import time

def timeme(func):
	def wrapper():
		a = time.time()
		func()
		b = time.time()
		print(f"Total Time {b-a}")
	return wrapper

