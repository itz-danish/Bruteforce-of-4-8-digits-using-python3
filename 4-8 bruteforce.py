in_put = input("Enter your password to bruteforce: ")
a1 = "a"
a2 = "a"
a3 = "a"
a4 = "a"
a5 = "a"
a6 = "a"
a7 = "a"
a8 = "a"
dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w', 'x', 'y', 'z',]
plc1 = -1
plc2 = -1
plc3 = -1
plc4 = -1
plc5 = -1
plc6 = -1
plc7 = -1
plc8 = -1

l = len(in_put)
while True:
	if l == 4:
		plc4 += 1
		a4 = a4.replace(a4,(dictionary[plc4]))
		print(a1+a2+a3+a4)
		
		if a1+a2+a3+a4 == in_put:
			print("Your password is ",a1+a2+a3+a4)
			break;
			
		if plc4 == 25:
			plc4 = -1
			plc3 += 1
			a3 = a3.replace(a3,(dictionary[plc3]))
			print(a1+a2+a3+a4)
		
		if a1+a2+a3+a4 == in_put:
			print("Your password is ",a1+a2+a3+a4)
			break;
			
		if plc3 == 25:
			plc3 = -1
			plc2 += 1
			a2 = a2.replace(a2,(dictionary[plc2]))
			print(a1+a2+a3+a4)
		
		if a1+a2+a3+a4 == in_put:
			print("Your password is ",a1+a2+a3+a4)
			break;
		
		if plc2 == 25:
			plc2 = -1
			plc1+= 1
			a1 = a1.replace(a1,(dictionary[plc1]))
			print(a1+a2+a3+a4)
		
		if a1+a2+a3+a4 == in_put:
			print("Your password is ",a1+a2+a3+a4)
			break;
	if l == 5:
		plc5 += 1
		a5 = a5.replace(a5,dictionary[plc5])
		print(a1+a2+a3+a4+a5)
		if a1+a2+a3+a4+a5 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5)
			break;
		if plc5 == 25:
			plc5 = -1
			plc4 += 1
			a4 = a4.replace(a4,(dictionary[plc4]))
			print(a1+a2+a3+a4+a5)
		
		if a1+a2+a3+a4+a5 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5)
			break;
			
		if plc4 == 25:
			plc4 = -1
			plc3 += 1
			a3 = a3.replace(a3,(dictionary[plc3]))
			print(a1+a2+a3+a4+a5)
		
		if a1+a2+a3+a4+a5 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5)
			break;
			
		if plc3 == 25:
			plc3 = -1
			plc2 += 1
			a2 = a2.replace(a2,(dictionary[plc2]))
			print(a1+a2+a3+a4+a5)
		
		if a1+a2+a3+a4+a5 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5)
			break;
		
		if plc2 == 25:
			plc2 = -1
			plc1+= 1
			a1 = a1.replace(a1,(dictionary[plc1]))
			print(a1+a2+a3+a4+a5)
		
		if a1+a2+a3+a4 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5)
			break;
	if l == 6:
		plc6 += 1
		a6 = a6.replace(a6,(dictionary[plc6]))
		print(a1+a2+a3+a4+a5+a6)
		
		if a1+a2+a3+a4+a5+a6 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6)
			break;
		if plc6 == 25:
			plc6 = -1
			plc5 += 1
			a5 = a5.replace(a5,(dictionary[plc5]))
			print(a1+a2+a3+a4+a5+a6)
		if plc5 == 25:
			plc5 = -1
			plc4 += 1
			a4 = a4.replace(a4,(dictionary[plc4]))
			print(a1+a2+a3+a4+a5+a6)
		
		if a1+a2+a3+a4+a5+a6 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6)
			break;
			
		if plc4 == 25:
			plc4 = -1
			plc3 += 1
			a3 = a3.replace(a3,(dictionary[plc3]))
			print(a1+a2+a3+a4+a5+a6)
		
		if a1+a2+a3+a4+a5+a6 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6)
			break;
			
		if plc3 == 25:
			plc3 = -1
			plc2 += 1
			a2 = a2.replace(a2,(dictionary[plc2]))
			print(a1+a2+a3+a4+a5+a6)
		
		if a1+a2+a3+a4+a5+a6 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6)
			break;
		
		if plc2 == 25:
			plc2 = -1
			plc1+= 1
			a1 = a1.replace(a1,(dictionary[plc1]))
			print(a1+a2+a3+a4+a5+a6)
		
		if a1+a2+a3+a4+a5+a6 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6)
			break;
	if l == 7:
		plc7 += 1
		a7 = a7.replace(a7,(dictionary[plc7]))
		print(a1+a2+a3+a4+a5+a6+a7)
		
		if plc7 == 25:
			plc7 = -1
			plc6 += 1
			a6 = a6.replace(a6,(dictionary[plc6]))
			print(a1+a2+a3+a4+a5+a6+a7)
		
		if a1+a2+a3+a4+a5+a6+a7 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6+a7)
			break;
		if plc6 == 25:
			plc6 = -1
			plc5 += 1
			a5 = a5.replace(a5,(dictionary[plc5]))
			print(a1+a2+a3+a4+a5+a6+a7)
			
		if plc5 == 25:
			plc5 = -1
			plc4 += 1
			a4 = a4.replace(a4,(dictionary[plc4]))
			print(a1+a2+a3+a4+a5+a6+a7)
		
		if a1+a2+a3+a4+a5+a6+a7 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6+a7)
			break;
			
		if plc4 == 25:
			plc4 = -1
			plc3 += 1
			a3 = a3.replace(a3,(dictionary[plc3]))
			print(a1+a2+a3+a4+a5+a6+a7)
		
		if a1+a2+a3+a4+a5+a6+a7 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6+a7)
			break;
			
		if plc3 == 25:
			plc3 = -1
			plc2 += 1
			a2 = a2.replace(a2,(dictionary[plc2]))
			print(a1+a2+a3+a4+a5+a6+a7)
		
		if a1+a2+a3+a4+a5+a6+a7 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6+a7)
			break;
		
		if plc2 == 25:
			plc2 = -1
			plc1+= 1
			a1 = a1.replace(a1,(dictionary[plc1]))
			print(a1+a2+a3+a4+a5+a6+a7)
		
		if a1+a2+a3+a4+a5+a6+a7 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6+a7)
			break;
			
	if l == 8:
		plc8 += 1
		a8 = a8.replace(a8,(dictionary[plc8]))
		print(a1+a2+a3+a4+a5+a6+a7+a8)
		
		if plc8 == 25:
			plc8 = -1
			plc7 += 1
			a7 = a7.replace(a7,(dictionary[plc7]))
			print(a1+a2+a3+a4+a5+a6+a7+a8)
			
		if plc7 == 25:
			plc7 = -1
			plc6 +=1
			a6 = a6.replace(a6,(dictionary[plc6]))
			print(a1+a2+a3+a4+a5+a6+a7+a8)	
		if plc6 == 25:
			plc6 = -1
			plc5 += 1
			a5 = a5.replace(a5,(dictionary[plc5]))
			print(a1+a2+a3+a4+a5+a6+a7+a8)
		if plc5 == 25:
			plc5 = -1
			plc4 += 1
			a4 = a4.replace(a4,(dictionary[plc4]))
			print(a1+a2+a3+a4+a5+a6+a7+a8)
		if plc4 == 25:
			plc4 = -1
			plc3 += 1
			a3 = a3.replace(a3,(dictionary[plc3]))
			print(a1+a2+a3+a4+a5+a6+a7+a8)
		if plc3 == 25:
			plc3 = -1
			plc2 +=1
			a2 = a2.replace(a2,(dictionary[plc2]))
			print(a1+a2+a3+a4+a5+a6+a7+a8)
		if plc2 == 25:
			plc2 = -1
			plc1 += 1
			a1 = a1.replace(a1,(dictionary[plc1]))
			print(a1+a2+a3+a4+a5+a6+a7+a8)
		
		
		
		if a1+a2+a3+a4+a5+a6+a7+a8 == in_put:
			print("Your password is ",a1+a2+a3+a4+a5+a6+a7+a8)
			break;
