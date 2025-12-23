# write_file.py
# Writing text to a file

with open("sample.txt", "w") as file:
    file.write("Hello, this is a file.\n")
    file.write("Written using Python.\n")

print("File written successfully.")
