def make_album(artist_name, artist_album):
    full_title = f"{artist_name} {artist_album}"
    return full_title.title()
while True:
    print("\nPlease tell me your artist name and artist album:")
    print("(enter 'q' at any time to quit)")
    f_name = input("Artist Name: ")
    if f_name == 'q':
        break
    l_name = input("Artist Album: ")
    if l_name == 'q':
        break
    make_album = make_album(f_name, l_name)
    print(f"\nYour artist name and artist title is: {make_album}, !")

