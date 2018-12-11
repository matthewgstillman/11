#Lab 11
#1. Write a class named, Pet, which should have the following attributes:
# __name
# __animal_type
# __age

#Note that all these attributes are private.
#The Pet class should have an __init__method that creates these attributes. It should also have the
#following methods:

# set_name: This method assigns a value to the __name field
# set_animal_type: This method assigns a value to the __animal_type field
# set_age: This method assgins a value to the __age field
# get_name: This method returns the value of the __name field
# get_animal_type: This method returns the value of the __animal_type field
# get_age: This method returns the value of the __age field

class Pet(object):
    count = 0
    def __init__(self, __name, __animal_type, __age):
        self.__name = __name
        self.__animal_type = __animal_type
        self.__age = __age
        Pet.count += 1


    def set_name(self, __name):
        self.__name = __name
        print("The pet's name is: {}".format(self.__name))
        return self

    def set_animal_type(self, __animal_type):
        self.__animal_type = __animal_type
        print("The animal's type is {}".format(self.__animal_type))
        return self

    def set_age(self, __age):
        self.__age = __age
        print("The animal's age is {}".format(self.__age))
        return self

    def total_pets(self):
        print("Total pets: {}".format(self.__total_pets))

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

#2. Using the class created above, now create the following 3 pets that you own
# a 15-year old cat named Tigger (use the variable pet1)
# a 3-year old dog named Lucky (use the variable pet2)
# a 30-year old parrot named Coco (use the variable pet3)
#Also create a class attribute called number to keep track of the number of pets created

pet1 = Pet("Grizzelda", "cat", 6)
pet2 = Pet("Bugatti", "cat", 1)
pet3 = Pet("Hedwig", "cat", 10)
print("Pet Count: {}".format(Pet.count))


#3. Once you have created the 3 instances, please use the get_* methods to return description of the 3
#pets you own
#For example,
#I have a pet named Tigger. He is a 15-year-old cat. 

print("I have a pet named {}. She is a {}-year-old {}.".format(pet1.get_name(), pet1.get_age(), pet1.get_animal_type(), pet1.get_age()))

print("My roommate has a pet named {}. He is a {}-year-old {}.".format(pet2.get_name(), pet2.get_age(), pet2.get_animal_type(), pet2.get_age()))

print("My parents have a pet named {}. She is a {}-year-old {}.".format(pet3.get_name(), pet3.get_age(), pet3.get_animal_type(), pet3.get_age()))



