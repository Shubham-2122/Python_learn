def validate_name_and_contact(func):
    def wrapper(name,contact_number):
        if not name or not isinstance(name, str):
            return "Name must be a non-empty string."
        if len(contact_number) != 10 or not contact_number.isdigit():
            return "Contact number must be a 10-digit number"
        return func(name,contact_number)
    return wrapper

@validate_name_and_contact

def register_user(name, contact_number):
    return f"User {name} with contact number {contact_number} hase been successfully registered."

name = input("Enter Name : ")
contact =input("Enter your 1- digit mobile number :")

'''
print(register_user("Shubham","1234567891")) #valid input
print(register_user("","1234567890")) #invalid name
print(register_user("bob","2324")) #invalid contact number
print(register_user("charli","123bgf3563")) #invalid contcat number (contains letters)

'''

print(register_user(name,contact)) # Valid Input
