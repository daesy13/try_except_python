try:
    f = open("test_file.txt")
    var = bad_var
# more expecific error at the Top
except FileNotFoundError:
    print("Sorry, this file does not exist")
# general exceptions after the expecifics
except Exception:
    print("Sorry, something went wrong")
# else:
#     pass
# finally:
#     pass