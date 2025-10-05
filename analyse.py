filename = 'ulysses.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        
except FileNotFoundError:
    print("My wasp'll be spanked if the file doesnt exist")

else: 
    # count the number of words in the file
    # words = contents.split()
    # num_words = len(words)
    # print(f"There are {num_words} words in the file {filename}!")

    # COUNT HOW MANY TIMES THE WORD 'THE' APPEARS
    the_count = contents.lower().count('the')


    print(f"The word 'The' appears {the_count} times in {filename}!")
