def read_existing_usernames(filename):
    """Read existing usernames from a file and store them in a dictionary.

    Args:
        filename (str): The name of the file containing existing usernames.

    Returns:
        dict: A dictionary containing existing usernames as keys.
    """
    # Create an empty dictionary to store existing usernames
    existing_usernames = {}
    
    # Read existing usernames from the file
    with open(filename, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into username and password (separated by a space)
            username, _ = line.split()
            
            # Store the username in the dictionary and set the value to True
            existing_usernames[username] = True
    
    # Print a success message with the existing usernames
    print(f'Existing usernames: {', '.join(existing_usernames)}')
    
    # Return the dictionary of existing usernames
    return existing_usernames


def register_user():
    """
    Register a new user by entering a username and password.
    The username must be unique and the password must be confirmed.
    The new username and password are stored in a file. ('user.txt')
    
    Args:
        None
        
    Returns:
        None
    """
    # Bring in existing usernames from the file with the function
    existing_usernames = read_existing_usernames('user.txt')
    
    # Iterate until a new user is successfully registered
    while True:
        # Prompt the user to enter a new username
        username = input("To register a new user, please enter a username: ")
        
        # Check if the username is already taken
        if username.lower() in existing_usernames:
            # Print an error message and prompt the user to try again
            print(f"Sorry, the username '{username}' has already been taken")
            print("Please try again.\n")
        # If the username is not taken
        else:
            # Prompt the user to enter a password and confirm it
            password = input("Please enter a password: ")
            
            # Confirm the password by reentering it
            confirm_password = input("Please reenter your password: ")
            
            # Check if the passwords match
            if password == confirm_password:
                # Open the file in append mode and write the new information
                # Append because we don't want to overwrite the existing data
                with open('user.txt', 'a') as file:
                    # Write the new username and password to the file
                    file.write(f'{username} {password}\n')
                
                # Print a success register message
                print("User registered successfully!")
                
                # Break out of the loop to end the program
                break
            
            # If the passwords do not match
            else:
                # Print an error message and prompt the user to try again
                print("Passwords do not match. Please try again.\n")

# Run main program to register a new user
register_user()
