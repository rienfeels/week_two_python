hotel = {
    '1': {
        '185': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}
def display_occupants():
    print("\nCurrent Occupants:")
    for floor, rooms in hotel.items():
        for room, occupants in rooms.items():
            print(f"Floor {floor}, Room {room}: {', '.join(occupants)}")

def check_in():
    floor = input("Enter the floor number: ")
    room = input("Enter the room number: ")

    if room in hotel.get(floor, {}):
        print("Error: Room is already occupied.")
        return

    occupants_count = int(input("Enter the number of occupants: "))
    occupants = [input(f"Enter name of occupant {i + 1}: ") for i in range(occupants_count)]

    hotel.setdefault(floor, {})[room] = occupants
    display_occupants()

def check_out():
    floor = input("Enter the floor number: ")
    room = input("Enter the room number: ")

    occupants = hotel.get(floor, {}).get(room, None)

    if occupants is None:
        print("Error: Room is not occupied.")
        return

    del hotel[floor][room]
    display_occupants()

# Main program loop
while True:
    print("\nMenu:")
    print("1. Check In")
    print("2. Check Out")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        check_in()
    elif choice == '2':
        check_out()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")