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

if __name__ == '__main__':
    while True:
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit\n''')
        menu_input = int(input('Please enter an option:'))
        password = input("Please enter your password to encode:")
        print("Your password has been encoded and stored!")
        if menu_input == 1:
            password = encoder(password)
        elif menu_input == 2:
            pass
            #fixme
            #print(f'The encoded password is {password}, and the original password is {please do this!}.')
        elif menu_input == 3:
            quit()