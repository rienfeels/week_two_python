numbers = [1, 2, 3, 4, 5, 99, 2600, 300]
reversed_list = list(reversed(numbers))
print("Original List", numbers)
print("Reversed List", reversed_list)

original_string = "Python"
empty_list = []
for letter in original_string:
    empty_list.append(letter)
empty_list.reverse()
new_string = ""
for letter in empty_list:
    new_string += letter
print(new_string)

favorite_albums = ["To Pimp a Butterfly", "The Sun's Tirade", "Flower Boy"]
album_to_check = "Swimming"
if album_to_check in favorite_albums:
    favorite_albums.remove(album_to_check)
    print(f"{album_to_check} has been removed from the list.")
else:
    favorite_albums.append(album_to_check)
    print(f"{album_to_check} has been added to the list.")
print("Updated List:", favorite_albums)

