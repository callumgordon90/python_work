def sandwiches(*list):
    """Summarising the sandwhich that we are about to make:"""
    print("..Making a delicious sandwich with the following toppings:\n")
    for item in list: 
        print(f"adding {item}")
    print("\nWe now have a delicious Sandwich. Thank you and good night!\n")

sandwiches('ham', 'cheese', 'pickle')

sandwiches('chorizo')

sandwiches('tuna', 'mayonase')