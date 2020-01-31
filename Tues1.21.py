class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print("Your car is a {}, {}, {} ".format(self.year, self.make, self.model))

car = Vehicle('Honda', 'Brown', 2015)

car.print_info()

class Person: 
    def __init__(self, name, email, phone, friends):
        self.name = name                                                    #Instance variable
        self.email = email
        self.phone = phone
        self.friends = []
    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
    def print_contact_info(self):
        print('My email: {}, My phone number {}'.format(self.email, self.phone))
    def add_friend(self, other_person):
        self.friends.append(other_person)
    def num_frineds(self):
        len(Jordan.friends)
        print(Jordan.friends)

Sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', []) #Creating an object(Person Type) #Passing arguments to the paramaters (instc var)
Jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', [])

Sonny.print_contact_info()
Jordan.print_contact_info()

Jordan.add_friend(Sonny)

print(len(Jordan.friends))

Jordan.num_frineds()