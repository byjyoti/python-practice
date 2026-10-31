student ={
    "name":"Jyoti",
    "age":20,
    "course":"CSIT"
}
print(student["name"])
print(student["course"])
student["age"] = 21
student["city"] = "Mahendranagar"
print(student)
for key, value in student.items ():
    print(key,":",value)
users = {
    "admin":"1234",
    "jyoti":"pass99"
}
username = input("Enter username:")
password = input("Enter password:")
if username in users and users[username] == password:
    print("Login successful")
else:
    print("Login failed")

