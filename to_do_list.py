import os
while(1):
    print("""
1. To create and add in  To do list
2. Track the  To do list
3. Update on To list
4. Delete a list
""")
    ch=int(input("Please Enter your choice: "))
    if ch==1:
        f_name=input("Enter the list name to create: ")
        f_name=f_name+".txt"
        f=open(f_name,"a")
        f_data=input("Enter the data to add in the list:\n----> ")
        f.write("\n"+f_data)
        f.close()
    elif ch==2:
         f_name=input("Enter the name of  To do list: ")
         f_name=f_name+".txt"
         print("To do list data is\n----->")
         f_data=open(f_name,"r")
         item=f_data.read()
         print(item)
         f_data.close()
    elif ch==3:
        f_name=input("Enter the To do list name: ")
        f_name=f_name+".txt"
        f_data=open(f_name,"w")
        wrt=input("Please Write something here for Updation: ")
        f_data.write(" "+wrt)
        f_data=open(f_name,"r")
        print(f_data.read())
        f_data.close()
    elif ch==4:
        f_name=input("Enter a file name to Delete: ")
        f_name=f_name+".txt"
        os.remove(f_name)
        print("----->")
        print(f_name," is Deleted successfully")
    else:
         print("Invalid Input ")

