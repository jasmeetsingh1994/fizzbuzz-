def tocheckbook("a,b,c")
	return(a,b,c)

target=input("textbook1 textbook2 textbook3")
	if target = "textbook1":
		fr=open('textbook1.txt','r')
		check1=1
	elif target = "textbook2":
		fr=open('textbook2.txt','r')
	elif target = "textbook3":
		fr=open('textbook3.txt','r')
	else target = input("enter a valid book again")		
