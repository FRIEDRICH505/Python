def make_album(artist_name, artist_album):
    full_title = f"{artist_name} {artist_album}"
    return full_title.title()
while True:
    print("\nPlease tell me your artist name and album:")
    f_name = input("Artist Name: ")
    l_name = input("Artist Title: ")
    make_album = make_album(f_name, l_name)
    print(f"\nYour artist name and album is: {make_album}, !")
