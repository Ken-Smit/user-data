#Kenneth Smith 4-13-24 5.3 
#This program is intended to get information from a user write it and read the message in a file

def main():
    # Prompt the user for file name
    file_name = input("Enter the file name: ")

    # Prompt the user for their name
    name = input("Enter your name: ")

    # Prompt the user for their street address
    street_address = input("Enter your street address: ")

    # Prompt the user for their phone number
    phone_number = input("Enter your phone number: ")

    # Write user data to the file
    with open('kenneth_data.txt', 'w') as file:
        file.write(f"{name},{street_address},{phone_number}")

    # Read and display the contents of the file
    with open('kenneth_data.txt', 'r') as file:
        data = file.read()
        print("Contents of the file:")
        print(data)

if __name__ == "__main__":
    main()
