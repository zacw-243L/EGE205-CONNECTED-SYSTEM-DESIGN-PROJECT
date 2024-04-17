import os

File = open("MyNotes.txt", "w")
File.write("If you can see me means I have written to MyNotes successfully!")
File.close()

File = open("MyNotes.txt", "r")
print(File.read())
File.close()

File = open("MyNotes.txt", "a")
File.write("I am adding more lines!")
File.close()

File = open("MyNotes.txt", "r")
print(File.read())
File.close()

os.remove("MyNotes.txt")

try:
  File = open("demofile.txt", "r")
  File.write("How are you?")
except:
  print("Something went wrong when writing to the file")
  
class Student:
  def __init__(self, Name, Age):
    self.Name = Name
    self.Age = Age

  def SelfIntro(self):
    print("Hello my name is " + self.Name)


Student1 = Student("John", 18)
print(Student1.Name)
print(Student1.Age)
Student1.SelfIntro()

