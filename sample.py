employees=[]
while True:
	print("Press 1 for add employee")
	print("Press 2 for delete employee ")
	print("Press 3 for change name of  employee")
	print("Press 4 for search  employee")
	print("Press 5 for display employee")
	print("Press 6 for Quit")
	choice = int(input("Enter choice"))
	if choice == 1:
		name=input("Enter the name")
		if name != None:
			employees.append(name)
	elif choice == 2:
		name=input("enter the name you want to delete")
		if name in employees and name!=None:
			res=employees.remove(name)
#			print(res)
#			print(str(res) +" is deleted!")
		else:
			print("Incorrect!!!")
	elif choice == 3:
		name=input("Enter the name you want to change")
		employees.remove(name)
		new_name=input("Enter the new name")
		employees.append(new_name)
		print(employees)
	elif choice == 4:
		name=input("enter the name you want to search")
		if name in employees:
			print("We found!!")
		else:
			print("Not exist!!")
	elif choice == 5: 
                print(employees)
	elif choice == 6:
		break
	else:
		print("Invalid choice")
