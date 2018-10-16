# convert an integer to a hex digit (a character)
def hex_char(value):
    if value <= 9 and value >= 0:
        return chr(value + ord('0'))
    else:
        return chr(value - 10 + ord('A'))

# convert a decimal to a hex as a string python
def to_hex(decimal):
    pass

def main():
    pass
    #assert to_hex(12345) == '3039' 
    #assert to_hex(0) == '0' 

main()
