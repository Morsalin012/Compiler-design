# Takes user input and checks if the string matches the pattern '^a.*b$'.

import re

def main():
    # 1. Take the input from the user
    print("Take the input from the user: ", end=" ")
    # Use input() to read the string
    input_string = input() 
    
    # 2. Define the regex pattern
    # Pattern: Must start with 'a', contain any characters in the middle, and end with 'b'.
    pattern = r"^a.*b$"
    
    # 3. Execute regex on the input string
    # re.match() tries to match the pattern at the beginning of the string.
    # We use re.match() here, but re.search() or re.fullmatch() would also work
    # since the pattern is anchored with '^' and '$'.
    
    # re.fullmatch() is often preferred for exact string matching as it requires 
    # the entire string to match the pattern, similar to your C code's anchors.
    
    match = re.fullmatch(pattern, input_string)
    
    # 4. Check the result and print output
    if match:
        print("Accepted")
    else:
        print("Rejected")

if __name__ == "__main__":
    main()