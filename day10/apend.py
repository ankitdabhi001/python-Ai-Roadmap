# Add New Content In Old File End Without Erasing Old Content. 

Content=input("Enter New Content=")

with open("abc.txt","a")as newfile:
    newfile.write("\n"+ Content)

print("New  Content is added")
