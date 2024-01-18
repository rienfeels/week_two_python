class Person:
    def __init__(self, name, email, phone, friends=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends if friends is not None else []  # Initialize friends as an empty list if not provided
        self.greeting_count = 0
        self.unique_people_greeted = set()  # Initialize the set for unique people greeted

    def __str__(self):
        return '{} {} {}'.format(self.name, self.email, self.phone)

    def print_contact_info(self):
        print("%s's email: %s" % (self.name, self.email))
        print("%s's phone number: %s" % (self.name, self.phone))

    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))
        self.greeting_count += 1
        self.unique_people_greeted.add(other_person)  # Add the person to the set of unique people greeted

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)

    def num_unique_people_greeted(self):
        return len(self.unique_people_greeted)

# Example usage
Sonny = Person(name='Sonny', email='sonny@hotmail.com', phone='483-485-4948')
Jordan = Person(name='Jordan', email='jordan@aol.com', phone='495-586-3456')
Dee_Ann = Person(name='Dee Ann', email='dee_ann@gmail.com', phone='555-123-4567')

Sonny.greet(Jordan)
Jordan.greet(Sonny)
Sonny.greet(Jordan)
Sonny.greet(Dee_Ann)

# Access the greeting_count attribute
print(Sonny.greeting_count)  # Output: 3
print(Jordan.greeting_count)  # Output: 1
print(Dee_Ann.greeting_count)  # Output: 0

# Access the num_unique_people_greeted method
print(Sonny.num_unique_people_greeted())  # Output: 2 (Jordan and Dee Ann have been greeted)
print(Jordan.num_unique_people_greeted())  # Output: 1 (Sonny has been greeted)
print(Dee_Ann.num_unique_people_greeted())  # Output: 0

# Add friends using the add_friend method
Jordan.add_friend(Sonny)
Sonny.add_friend(Jordan)

# Get the number of friends using the num_friends method with the person's name
print(f"{Jordan.name} has {Jordan.num_friends()} friends.")  # Output: Jordan has 1 friend
print(f"{Sonny.name} has {Sonny.num_friends()} friends.")   # Output: Sonny has 1 friend

Sonny.print_contact_info()
print('Sonny\'s contact info - Email: %s, Phone: %s' % (Sonny.email, Sonny.phone))
print('Jordan\'s contact info - Email: %s, Phone: %s' % (Jordan.email, Jordan.phone))

# Print the representation of Person objects using __str__
print(str(Sonny))
print(str(Jordan))
print(str(Dee_Ann))
