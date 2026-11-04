with open("notes.txt","w") as file:
    file.write("Hello Jyoti\n")
    file.write("Day 7 Python\n")
print("File saved")
with open("notes.txt","r") as file:
    print(file.read())
with open("notes.txt","a") as file:
    file.write("Learned the with statement\n")
with open("notes.txt","r") as file:
    print(file.read())
note = input("Write a note:")
with open("notes.txt","a") as file:
    file.write(note + "\n")
print("Note saved!")



