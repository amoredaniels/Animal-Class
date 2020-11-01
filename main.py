#Amore' Daniels

#create animal class
class Zoo:
  
  #__init___ construct method 
  #initializes the attributes of the instance
  #called for every instance of the cllass
  def __init__(self,name,color,animalType,age,sound):
    self.name = name
    self.animalType = animalType
    self.age = age
    self.sound = sound
    self.color = color
    
  #set the value of each argument
  def setName(self,name):
    self.name = name
  def setAnimalType(self,animalType):
    self.animalType = animalType
  def setAge(self,age):
    self.age = age
  def setSound(self,sound):
    self.sound = sound
  def setColor(self,color):
    self.color = color

  #get/return the value of each argument
  def getName(self):
    return self.name
  def getAnimalType(self):
    return self.animalType
  def getAge(self):
    return self.age
  def getSound(self):
    return self.sound
  def getColor(self):
    return self.color

  #use __str__ method to print object details
  def __str__(self):
    return ('Hi, my name is {}! I am a {} {}. I am {} years old and make a(n) {} sound.'.format(self.name, self.color, self.animalType, self.age, self.sound))
    
#define main function
def main():
    #Create instances/objects of the Zoo class
    zoo_animal1 = Zoo('Miss Piggy','pink','pig',44,'oink')
    zoo_animal2 = Zoo('Alex','golden brown','lion',15,'roar')
    zoo_animal3 = Zoo('Horton', 'grey','elephant',32,'trumpeting')
    #print them
    print(zoo_animal1)
    print(zoo_animal2)
    print(zoo_animal3)

#call main function
main()
