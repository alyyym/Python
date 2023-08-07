def add_it_up():
	integer_int=(input("Give an integer:"))
	try:
		#integer_int=int(integer_int)
		print(sum(range(int(integer_int)+1)))
	except ValueError:
		print("0")
		
add_it_up()