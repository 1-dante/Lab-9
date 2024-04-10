#Dante Lorenzo-Rodriguez

def encoder(string):
    num_list = []
    ans = ''
    for i in range(len(string)):
        num_list.append(int(string[i]))
    num_list = [num + 3 for num in num_list]
    for num in num_list:
        ans += f'{num}'
    return ans

def decoder(input):
    my_list = []
    for number in input:
        my_list.append(int(number) - 3)
    my_string = ''
    for item in my_list:
        my_string += str(item)
    return my_string


if __name__ == '__main__':
    while True:
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit\n''')
        menu_input = int(input('Please enter an option: '))
        if menu_input == 3:
            quit()
        elif menu_input == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
            print()
            continue
        elif menu_input == 2:
            original_password = decoder(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {original_password}.')
            print()
            continue
