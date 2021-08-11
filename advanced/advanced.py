
fruit=[]
while True:
	print("Press 1 for add fruit and rate")
	print("Press 2 for delete employee ")
	print("Press 3 for change name of fruit")
	print("Press 4 for search  fruit")
	print("Press 5 for display fruit")
	print("Press 6 for Quit")
	choice = int(input("Enter choice"))
	if choice == 1:
		name=input("Enter the fruit name")
		rate=input("Enter the rate")
		if name != None and rate != None:
			fruit.append([name,rate])
	elif choice == 2:
		name=input("enter the fruit name you want to delete")
		for i in fruit:
			if i[0]== name:
				fruit.remove(i)
	elif choice == 3:
		name=input("Enter the fruit name you want to change")
		rate=input("Enter the rate you want to change")
		new_name=input("Enter the new name")
		new_rate=input("Enter the new rate")
		for i in fruit:
			if i[0] == name and i[1] == rate :
				fruit.remove(i)
				fruit.append([new_name,new_rate])
				print(fruit)
	elif choice == 4:
		name=input("enter the fruit name you want to search")
		rate=input("enter the fruit rate you want to search")
		for i in fruit:
			if i[0] == name and i[1] == rate:
				print("We found!!")
			else:
				print("Not exist!!")
	elif choice == 5: 
                print(fruit)
	elif choice == 6:
                break
	else:
		print("Invalid choice")
