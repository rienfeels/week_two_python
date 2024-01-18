class Person():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, Person):
        print('Hello {}, I am {}!'.format(Person.name, self.name))

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}")
        print(f"{self.name}'s phone number: {self.phone}")

Sonny = Person(name='Sonny', email='sonny@hotmail.com', phone='483-485-4948')
Jordan = Person(name='Jordan', email='jordan@aol.com', phone='495-586-3456')

Sonny.greet(Jordan)
Jordan.greet(Sonny)

Sonny.print_contact_info()
Jordan.print_contact_info()
