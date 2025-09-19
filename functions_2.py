def make_album():
    while True:
        print("Type the name of an artist:")
        print("Enter 'q' at any time to quit\n")

        
        artist = input("Type artist:\n")
        if artist == 'q':
            break

        album = input("Type Album name\n")
        if album == 'q':
            break

        print(f"YOU HAVE SELECTED {artist} {album}. GOOD CHOICE!\n")

make_album()
