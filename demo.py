while True:
   try:
       x=int(input("number:"))
   except ValueError:
       print("please input number")
   else:
       print(x)
       break