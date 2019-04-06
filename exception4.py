# Creating your own exception
try:
    f = open("currupt_file.txt")
    if f.name == "currupt_file.txt":
        raise Exception #here we create our own exception using "Exception"
        #which is used around line 9
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Error!") #Here we change it instead (e) type "Error!"
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")