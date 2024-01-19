#The list

help = "Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me; Thy rod and thy staff they comfort me."

# Open a file for writing (creates the file if it doesn't exist)
file_path = "C:\\Users\\Komek\\Python_stuff\\EXAMPLE.txt"
with open(file_path, "w") as file:
    # Write content to the file
    file.write(help)
