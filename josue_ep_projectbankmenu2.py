#Menu body:
def menu():

    print('=============================')
    print('[1] Option 1')
    print('[2] Option 2')
    print('[3] Option 3')
    print('[0] Exit the program')
    print('=============================')

#Inputs:
menu()
option = int(input('Enter your option -->: '))


while option != 0:

    if option == 1:
        print('You choosed 1')

    elif option == 2:
        print('You choosed 2')
    
    elif option == 3:
        print('You choosed 3')
    
    else:
        print('You entered a invalid option.')
        menu()

    menu()
    option = int(input('Enter your option -->: '))

print('Thanks for using this program!')
    



    


    








