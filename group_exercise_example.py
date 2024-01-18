def create_person(name, email, phone):
    person = {
        "name": name,
        "email": email,
        "phone": phone,
    }
    return person

def greet(person1, person2):
    print('Hello {}, I am {}!'.format(person2["name"], person1["name"]))

def print_contact_info(person):
    print(f"{person['name']}'s email: {person['email']}, {person['name']}'s phone number: {person['phone']}")


# Create people as dictionaries
sonny = create_person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = create_person("Jordan", "jordan@aol.com", "495-586-3456")

# Perform actions on people
greet(sonny, jordan)
greet(jordan, sonny)

print_contact_info(sonny)