# try:
#     # Try to open a file that might not exist
#     my_file = open("non_existent_file.txt", "r")
#     content = my_file.read()
#     print(content)

# except FileNotFoundError: # This is a specific type of surprise (error)
#     print("Oops! I couldn't find that file. Are you sure the name is correct?")
#     # We could also create the file here if needed:
#     # with open("non_existent_file.txt", "w") as f:
#     #     f.write("This file was created because it didn't exist.")

# except Exception as e: # This is a general "catch-all" for any other surprise
#     print(f"An unexpected error occurred: {e}") # f-string for easy message creation

# finally:
#     # This will always run, whether there was an error or not.
#     # It's a good place to make sure resources are closed, but 'with open' is even better for files!
#     print("Attempted file operation complete.")

try:
    my_file= open("seven.txt", "r")
    my_text = my_file.read()    
    print(my_text)

except FileNotFoundError:
    print("The file 'seeven.txt' does not exist. Please check the file name and try again.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    try:
        my_file.close()
    except NameError:
        print("File was never opened, so no need to close it.")
