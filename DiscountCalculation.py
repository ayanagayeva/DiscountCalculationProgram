#Ayan Agayeva

#1. Menu options
def menu_options():
 print("\n1- Print Transaction ID and username")
 print("\n2- Print username, total before and total after discount")
 print("\n3- Quit")
 
#2. Get user's choice
def users_choice():
    while True:
        try:
         user_choice = int(input("\nEnter your choice ==> "))
         if user_choice == 1 or user_choice == 2 or user_choice == 3:
            return user_choice
         else:
            print("\nEnter a valid option")
        except ValueError:
            print("/nInvalid input. Please enter a number.")

#3. File access
def file_access():
 file_name = "input.txt"
 while True:
    user_file = input("\nEnter file name ==> ")
    if user_file.lower() == file_name:
        break
    else:
        print("\nEnter correct file name")

 print("\nReading data....\n")
 try:
    with open("input.txt","r") as f:
        data = f.readlines()
    return data

 except IOError as e:
    print(e)
    
#4. Display transaction ID + username (first + last name) + use try-except
def trid_username(file_data):
 print("{:<5} {:<10} {:<10}".format("ID","FirstName","LastName\n"))

 for line in file_data:
    row = line.split(" ")
    print("{:<5} {:<10} {:<10}\n".format(row[0],row[1],row[2]))


#5. Display username + ttl amnt b4 discount + ttl amnt after discout + saved amnt
#after discount
#round to 2 digits (output)
def before_after(file_data):
 print("{:<8} {:<10} {:<10} {:<10} {:<10}{:<10}".format('ID','FirstName','LastName','Before','After','Saved\n'))

 for line in file_data:
    row = line.split(" ")
    after_discount = float(row[3])-(float(row[3])*0.4)
    saved = float(row[3])-after_discount
    print("{:<8} {:<10} {:<10} {:<10.2f} {:<10.2f} {:<10.2f}\n".format(row[0],row[1],row[2],float(row[3]),after_discount, saved))

#6. After first attempt, ask menu again + another attempt
def more_option():
 while True:
    continue_choice = input("\nDo you want to see more option Y/N: ")
    if continue_choice == 'Y' or continue_choice =='y':
        return continue_choice == 'y'
    elif continue_choice == 'N' or continue_choice == 'n':
        return False
 else:
    print("You must enter Y/y/N/n to continue. Please try again")
    
def main():
    more_choice = None
    while True:
        menu_options()
        menu_choice = users_choice()
        if menu_choice == 3:
            print("\nHave a great day")
            break
        file_data = file_access() #assigning the data from the file to file data,
#then use file data for parameter of other functions
        if menu_choice == 1:
            trid_username(file_data)
        elif menu_choice == 2:
            before_after(file_data)
            more_choice = more_option()
        if not more_option:
            print("\nHave a great day")
            break

if __name__ == "__main__":
 main()
