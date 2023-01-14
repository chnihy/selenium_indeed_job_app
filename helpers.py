# helper functions
def nn():
	print("\n\n")

def show_dict(obj):
	nn()
	print(" :: Dict :: ")
	for k,v in obj.__dict__.items():
		print(f"{k}: {v}")
	nn()

def show_dir(obj):
	nn()
	print(" :: Dir ::")
	for x in dir(obj):
		if "__" in x:
			pass
		else:
			print(x)
	nn()