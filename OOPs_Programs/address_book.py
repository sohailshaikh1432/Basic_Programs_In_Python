from Log_Configuration import log_config_file

# set up logger to handle exceptions
logger = log_config_file.get_logger()


def welcome_screen(user_):
    """
    This method is used to display the operations that can be perform by that user.
    :param user_: It's accept user as a parameter.
    :return: None
    """
    option = 'y'
    while option == 'y':
        print('\n________Welcome To Address Book________\n')
        option = int(input('1. Insert Details \n2. Update Details \n3. Delete Details \n4. Quit \n\n'
                           'You chosen option : '))
        if option == 1:
            user_.insert_data()
        elif option == 2:
            user_.update_data()
        elif option == 3:
            user_.delete_data()
        elif option == 4:
            exit()
        else:
            print('Wrong Input! Try Again...\n\n')
            welcome_screen(user_)
        option = input('\nDo you want to continue (y/n) : ')


class AddressBook:
    def __init__(self):
        """
        This method (constructor) is used to initialised the variables.
        """
        self._first_name = None
        self._last_name = None
        self._address = None
        self._city = None
        self._state = None
        self._pin_code = None
        self._phone_number = None

    def insert_data(self):
        """
        This method is used to insert the details into the Address Book.
        :return: None
        """
        print('\nEnter the following details :-')
        self._first_name = input('First Name : ')
        self._last_name = input('Last Name : ')
        self._address = input('Address : ')
        self._city = input('City : ')
        self._state = input('State : ')
        self._pin_code = input('Pin Code : ')
        self._phone_number = input('Phone Number : ')
        self.save_data()
        print('\nAll Details Inserted Successfully!')

    def update_data(self):
        """
        This function is used to update the previous information of Address Book.
        :return: None
        """
        option = int(input('\nChoose which data you want to update : '
                           '\n1. First Name '
                           '\n2. Last Name '
                           '\n3. Address '
                           '\n4. City '
                           '\n5. State '
                           '\n6. Pin Code '
                           '\n7. Phone Number '
                           '\n\nYou Chosen option : '))
        if option == 1:
            print('First Name : ', self._first_name)
            self._first_name = input('Updated First Name : ')
            self.save_data()
        elif option == 2:
            print('First Name : ', self._last_name)
            self._last_name = input('Updated Last Name : ')
            self.save_data()
        elif option == 3:
            print('Address : ', self._address)
            self._address = input('Updated Address : ')
            self.save_data()
        elif option == 4:
            print('City : ', self._city)
            self._city = input('Updated City : ')
            self.save_data()
        elif option == 5:
            print('State : ', self._state)
            self._state = input('Updated State : ')
            self.save_data()
        elif option == 6:
            print('Pin Code : ', self._pin_code)
            self._pin_code = input('Updated Pin Code : ')
            self.save_data()
        elif option == 7:
            print('Phone Number : ', self._phone_number)
            self._phone_number = input('Updated Phone Number : ')
            self.save_data()
        else:
            print('Invalid Input! Please try again...')
            self.update_data()

    def delete_data(self):
        """
        This function is used to delete any specific data.
        :return: None
        """
        option = int(input('\nChoose which data you want to Delete : '
                           '\n1. First Name '
                           '\n2. Last Name '
                           '\n3. Address '
                           '\n4. City '
                           '\n5. State '
                           '\n6. Pin Code '
                           '\n7. Phone Number '
                           '\n\nYou Chosen option : '))
        if option == 1:
            print('First Name : ', self._first_name, ' (Deleted)')
            self._first_name = ''
            self.save_data()
        elif option == 2:
            print('Last Name : ', self._last_name, ' (Deleted)')
            self._last_name = ''
            self.save_data()
        elif option == 3:
            print('Address : ', self._address, ' (Deleted)')
            self._address = ''
            self.save_data()
        elif option == 4:
            print('City : ', self._city, ' (Deleted)')
            self._city = ''
            self.save_data()
        elif option == 5:
            print('State : ', self._state, ' (Deleted)')
            self._state = ''
            self.save_data()
        elif option == 6:
            print('Pin Code : ', self._pin_code, ' (Deleted)')
            self._pin_code = ''
            self.save_data()
        elif option == 7:
            print('Phone Number : ', self._phone_number, ' (Deleted)')
            self._phone_number = ''
            self.save_data()
        else:
            print('Invalid Input! Please try again...')
            self.update_data()

    def save_data(self):
        """
        This function save all the information into the Address Book.
        :return: None
        """
        file = open('address_book.txt', 'w')
        list_of_data = [
            ['First Name : ', self._first_name],
            ['\nLast Name : ', self._last_name],
            ['\nAddress : ', self._address],
            ['\nCity : ', self._city],
            ['\nState : ', self._state],
            ['\nPin Code : ', self._pin_code],
            ['\nPhone Number : ', self._phone_number, '\n']
        ]
        for data in list_of_data:
            for information in data:
                file.write(information)
        file.close()


if __name__ == '__main__':
    user = AddressBook()
    try:
        welcome_screen(user)
    except Exception as e:
        print('\nOops! Exception occurred..! Please try again...\n')
        logger.exception(e)
        welcome_screen(user)
