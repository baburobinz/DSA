# Define a function named to_string that converts a number 'n' to a string representation
# in a given 'base' using a character set "0123456789ABCDEF"
def to_string(n, base):

    conver_tString = "0123456789ABCDEF"

    if n<base:
        return conver_tString[n]
    
    return to_string(n//base,base)+conver_tString[n%base]

# Print the result of calling the to_string function with the input values 2835 and 16
print(to_string(10, 2))
