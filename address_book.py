from book_log import get_logger
import json
import csv

lg = get_logger("(CrudOperations_json_csv)", file_name="address_book_log.log")


class Contact:
    def __init__(self, sl_no, first_name, last_name, address, phone_number, email):
        self.sl_no = sl_no
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    @property
    def full_name(self):
        """
        :return: full name
        """
        try:
            return self.first_name + " " + self.last_name
        except Exception as e:
            lg.error(e)

    def to_string(self):
        try:
            return f'Sl.No: {self.sl_no}, Full Name: {self.full_name}, Address: {self.address}, ' \
                   f'Phone Number: {self.phone_number}, Email: {self.email} '
        except Exception as e:
            lg.error(e)

    def to_json(self):
        return {"sl_no": self.sl_no, "full_name": self.full_name, "address": self.address,
                "phone_number": self.phone_number, "email": self.email}

    def to_csv(self):
        return {"sl_no": self.sl_no, "full_name": self.full_name, "address": self.address,
                "phone_number": self.phone_number, "email": self.email}


class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contact_dict = {}

    def add_contact(self, contact_person_obj):
        """
        :param contact_person_obj: is the object of contact class
        :return: None
        """
        try:
            self.contact_dict.update({contact_person_obj.first_name: contact_person_obj})
        except Exception as e:
            lg.error(e)

    # def update_contact(self, sl_no, first_name, last_name, address, phone_number, email):
    #     """
    #     updating contacts
    #     :param sl_no: user integer input
    #     :param first_name: user string input
    #     :param last_name: user string input
    #     :param address: user string input
    #     :param phone_number:user integer input
    #     :param email: user string input
    #     :return: None
    #     """
    #     try:
    #         contact_person_name = input("Enter person name you want to update: ")
    #         contact_exist = self.contact_dict.get(contact_person_name)
    #         if not contact_exist:
    #             lg.info("name not present")
    #             return
    #         contact_exist.sl_no = sl_no
    #         contact_exist.first_name = first_name
    #         contact_exist.last_name = last_name
    #         contact_exist.address = address
    #         contact_exist.phone_number = phone_number
    #         contact_exist.email = email
    #         lg.debug("updated successfully")
    #     except Exception as e:
    #         lg.error(e)

    def get_contact(self, name):
        """
        :param name:  user string input
        :return: name of contact
        """
        try:
            return self.contact_dict.get(name)
        except Exception as e:
            lg.error(e)

    def display_contact(self):
        """
        displaying contact in key and value format
        :return: None
        """
        try:
            for key, value in self.contact_dict.items():
                print(key, value.to_string())
        except Exception as e:
            lg.error(e)

    def delete_contact(self, key):
        """
        this function display the details of contacts
        :param key: user string input
        :return: None
        """
        try:
            contact = self.get_contact(key)
            if not contact:
                lg.info("invalid contact")
                return
            self.contact_dict.pop(key)
            lg.debug("contact deleted successfully")
        except Exception as e:
            lg.error(e)

    def add_json_contact(self):
        """
        adding contacts to json dict
        :return: json dictionary
        """
        try:
            json_record_dict = {}
            for key, value in self.contact_dict.items():
                json_record_dict.update({key: value.to_json()})
            return json_record_dict
        except Exception as e:
            lg.error(e)

    def add_csv_contact(self):
        """
        adding contacts to csv dict
        :return: csv dictionary
        """
        try:
            csv_record_dict = {}
            for key, value in self.contact_dict.items():
                csv_record_dict.update({key: value.to_csv()})
            return csv_record_dict
        except Exception as e:
            lg.error(e)


if __name__ == '__main__':
    address_book_dict = {}


    def add_addressbook():
        """
        helper function to add an addressbook
        :return:  address book dictionary
        """
        try:
            address_book_name = input("Enter the address book name:\n")
            lg.info(address_book_name)
            address_book_obj = AddressBook(address_book_name)
            address_book_dict.update({address_book_obj.name: address_book_obj})
            return address_book_dict
        except Exception as e:
            lg.error(e)


    def display_addressbook():
        """
        helper function to display addressbook
        :return:
        """
        try:
            for index, company_name in enumerate(address_book_dict.keys()):
                print(index, company_name)
        except Exception as e:
            lg.error(e)


    def add_contact_address_book():
        """
        helper function for adding contacts in to address book
        :return: None
        """
        try:
            address_book_name = input("Enter the address book name:\n")
            address_book_object = address_book_dict.get(address_book_name)
            if address_book_object is None:
                address_book_object = AddressBook(address_book_name)
                address_book_dict.update({address_book_object.name: address_book_object})
                return
            sl_no = input("Enter the sl_no:\n")
            first_name = input("Enter the first name:\n")
            last_name = input("Enter the last name:\n")
            address = input("Enter the address:\n")
            phone_number = input("Enter the phone number:\n")
            email = input("Enter the email:\n")
            contact_object = Contact(sl_no, first_name, last_name, address, phone_number, email)
            address_book_object.add_contact(contact_object)
        except Exception as e:
            lg.error(e)


    def update_contact_address_book():
        """
        helper function for updating contacts in address book
        :return: None
        """
        try:
            address_book_name = input("Enter the address book name:\n")
            address_book_object = address_book_dict.get(address_book_name)
            if address_book_object is None:
                lg.info("Address book is not exist")
                return
            first_name = input("Enter the contact person name:\n")
            contact_obj = address_book_object.get_contact(first_name)
            if contact_obj is None:
                lg.info("Contact is not available")
                return
            sl_no = input("Enter the sl_no:\n")
            last_name = input("Enter the last name:\n")
            address = input("Enter the address:\n")
            phone_number = input("Enter the phone number:\n")
            email = input("Enter the email:\n")
            # address_book_object.update_contact(sl_no, first_name, last_name, address, phone_number, email)
            contact = Contact(sl_no=sl_no, first_name=first_name, last_name=last_name, address=address,
                              phone_number=phone_number, email=email)
            address_book_object.add_contact(contact)
        except Exception as e:
            lg.error(e)


    def get_contact_address_book():
        """
        helper function to get a contact from address book
        :return: None
        """
        try:
            address_book_name = input("Enter the address book name:\n")
            address_book_object = address_book_dict.get(address_book_name)
            if address_book_object is None:
                lg.info("Address book is not exist")
                return
            first_name = input("Enter the first name:\n")
            contact = address_book_object.get_contact(first_name)
            if contact is None:
                lg.info("contact doesn't exist")
                return
            print(contact.to_string())
        except Exception as e:
            lg.error(e)


    def delete_contact_address_book():
        """
         Helper function to delete the contacts
        :return: None
        """
        try:
            address_book_name = input("Enter the address book name:\n")
            address_book_object = address_book_dict.get(address_book_name)
            if address_book_object is None:
                lg.info("Address book doesn't exist")
                return
            first_name = input("Enter the first name:\n")
            lg.info
            address_book_object.delete_contact(first_name)
        except Exception as e:
            lg.error(e)


    def display_contact_address_book():
        """
        Helper function to display contacts
        :return: None
        """
        try:
            address_book_name = input("Enter the address book name:\n")
            address_book_object = address_book_dict.get(address_book_name)
            if address_book_object is None:
                print("Address book doesn't exist")
                return
            address_book_object.display_contact()
        except Exception as e:
            lg.error(e)


    def json_write_func():
        """
        Helper function to write json in to file
        :return: None
        """
        try:
            json_add_dict = {}
            for name, obj in address_book_dict.items():
                json_add_dict.update({name: obj.add_json_contact()})
            with open("json_ab.json", "w") as file:
                json.dump(json_add_dict, file, indent=2)
                # file.close()
        except Exception as e:
            lg.error(e)


    def json_read_func():
        """
        Helper function to read the json file
        :return: None
        """
        try:
            with open("json_ab.json", "r") as json_file:
                data = json.loads(json_file.read())
                lg.info(data)
        except Exception as e:
            lg.error(e)


    def csv_write_fun():
        """
        Helper function to write the csv file
        :return: None
        """
        try:
            with open("csv_ab.csv", "w") as csv_file:
                field_names = ["sl_no", "full_name", "address", "phone_number", "email"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
                csv_writer.writeheader()
                for name, object in address_book_dict.items():
                    contact_dict = object.add_csv_contact()
                    for key, data in contact_dict.items():
                        lg.info(data)
                        csv_writer.writerow(data)
                # csv_file.close()
        except Exception as e:
            lg.error(e)


    def csv_read_func():
        """
        Helper function to read from csv file
        :return:
        """
        try:
            with open("csv_ab.csv", "r") as csv_file:
                data = csv.reader(csv_file)
                for line in data:
                    lg.info(line)
                # csv_file.close()
        except Exception as e:
            lg.error(e)


    def default():
        print("Invalid! Enter the correct choice")


    choice_dict = {1: add_addressbook, 2: display_addressbook, 3: add_contact_address_book, 4: get_contact_address_book,
                   5: delete_contact_address_book, 6: display_contact_address_book, 7: update_contact_address_book,
                   8: json_write_func, 9: json_read_func, 10: csv_write_fun, 11: csv_read_func}

    while True:
        print("Enter the choice: \n1.Add addressbook\n2.Display addressbook\n3.Add contacts\n4.Get contacts\n5.Delete "
              "contacts\n6.Display contacts\n7.Update\n8.Json write\n9.Json read\n10.Csv write\n11.Csv read\n0.Exit")
        choice = int(input())
        if choice in choice_dict.keys():
            choice_dict.get(choice)()
        else:
            default()

"""
Enter the choice: 
1.Add addressbook
2.Display addressbook
3.Add contacts
4.Get contacts
5.Delete contacts
6.Display contacts
7.Update
8.Json write
9.Json read
10.Csv write
11.Csv read
0.Exit
1
Enter the address book name:
home
(CrudOperations) - 2022-09-05 03:09:11,326 - INFO - home
Enter the choice: 
1.Add addressbook
2.Display addressbook
3.Add contacts
4.Get contacts
5.Delete contacts
6.Display contacts
7.Update
8.Json write
9.Json read
10.Csv write
11.Csv read
0.Exit
2
0 home
Enter the choice: 
1.Add addressbook
2.Display addressbook
3.Add contacts
4.Get contacts
5.Delete contacts
6.Display contacts
7.Update
8.Json write
9.Json read
10.Csv write
11.Csv read
0.Exit
3
Enter the address book name:
home
Enter the sl_no:
01
Enter the first name:
shivaraj
Enter the last name:
k
Enter the address:
bangalore
Enter the phone number:
9876543456
Enter the email:
4shivaraj.gowda@gmail.com
Enter the choice: 
1.Add addressbook
2.Display addressbook
3.Add contacts
4.Get contacts
5.Delete contacts
6.Display contacts
7.Update
8.Json write
9.Json read
10.Csv write
11.Csv read
0.Exit
1
Enter the address book name:
personal
Enter the choice: 
1.Add addressbook
2.Display addressbook
3.Add contacts
4.Get contacts
5.Delete contacts
6.Display contacts
7.Update
8.Json write
9.Json read
10.Csv write
11.Csv read
0.Exit
(CrudOperations) - 2022-09-05 03:09:53,942 - INFO - personal
2
0 home
1 personal
Enter the choice: 
1.Add addressbook
2.Display addressbook
3.Add contacts
4.Get contacts
5.Delete contacts
6.Display contacts
7.Update
8.Json write
9.Json read
10.Csv write
11.Csv read
0.Exit
3
Enter the address book name:
personal
Enter the sl_no:
01
Enter the first name:
cheluvesha
Enter the last name:
b
Enter the address:
bangalore
Enter the phone number:
987653456
Enter the email:
cheluvesha.b@gmail.com
Enter the choice: 
1.Add addressbook
2.Display addressbook
3.Add contacts
4.Get contacts
5.Delete contacts
6.Display contacts
7.Update
8.Json write
9.Json read
10.Csv write
11.Csv read
0.Exit
10
{'sl_no': '01', 'full_name': 'shivaraj k', 'address': 'bangalore', 'phone_number': '9876543456', 'email': '4shivaraj.gowda@gmail.com'}
{'sl_no': '01', 'full_name': 'cheluvesha b', 'address': 'bangalore', 'phone_number': '987653456', 'email': 'cheluvesha.b@gmail.com'}
"""
