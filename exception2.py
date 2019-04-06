try:
    f = open("test_file.txt")
    var = bad_var #if remove this line code will run succesfully
# more expecific error at the Top
except FileNotFoundError as e:
    print(e)
# general exceptions after the expecifics
except Exception as e:
    print(e)

# will get: "name 'bad_var' is not defined"
