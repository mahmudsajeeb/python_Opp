#function is a first class object 

def double_deckar():
    print("Starting the double decker")

    def inner_fun():
        print('inside the inner')
    return inner_fun

print(double_deckar())
