filename_1 = 'cats.txt'
filename_2 = 'chickens.txt'

def see_content(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(contents)
            print("And my wasp'll be spanked for Roger Fairfax!!!")
    except FileNotFoundError:
        pass
        # print("My wasp\'ll be spanked if we can\'t find the bloomin file!!!!")



see_content(filename_2)