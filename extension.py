def get_file_extension(filename):
    # Split the filename by dot to separate the base name and extension
    parts = filename.split(".")

    # Get the last part of the split filename, which is the extension
    extension = parts[-1]

    return extension

# Prompt the user for input
filename = input("Input the Filename: ")

# Get the file extension
file_extension = get_file_extension(filename)

if file_extension=="py":
    extension='Python'
elif file_extension=="java":
    extension='Java'
elif file_extension=="c":
    extension='C'  
elif file_extension=="cpp":
    extension='C++'  
elif file_extension=="html":
    extension='HTML'    
elif file_extension=="css":
    extension='CSS'  
else:
    extension="INVALID"         
    
# Print the result
print("The extension of the file is:", extension)
