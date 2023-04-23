# variables
two_lines = 'GUI r' + '\nDELAY 1000'
#print(two_lines)

# create a list of upper case letters to use
alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = alphabet.upper()

# use upper case letters into ducky script
for i in range(len(alphabet)):
    print('REM The next 4 lines opens the ' + upper_alphabet[i] + ' drive')
    print(two_lines)
    print('STRING file:///'  + str(upper_alphabet[i]) + ':/')
    print('DELAY 1000')
    print('ENTER')
    print('')
