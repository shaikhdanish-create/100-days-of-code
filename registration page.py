#create function
def format_name(f_name, l_name):
    
    format_f_name = f_name.title()
    format_l_name = l_name.title()  
    result = f"Result: {format_f_name} {format_l_name}"  
        
    return result

print(format_name(input("What is your first name? "),
                  input("What is your last name? ")))
