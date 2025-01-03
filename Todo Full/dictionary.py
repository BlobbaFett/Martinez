import csv

def lodad_contacts(file_name):
    contacts = {}
    
    with open(file_name, mode = 'r', newline= '') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            first_name = row[0]
            last_name = row[1]
            phone_number = row[2]
            email_address = row[3]
            contacts[last_name] = [first_name, phone_number, email_address]
        return contacts

def display_contact_info(contact_info):
    if contact_info:
        print('Contact Information: ')
        print(f'Full Name: {contact_info[0]}')
        print(f'Phone Number: {contact_info[1]}')
        print(f'Email: {contact_info[2]}')
    else:
        print('No contact information found')
def main():
    file_name = r'C:\Users\Labinfo10\Documents\Quebec Martinez\archivos de chamba\contacts.csv'
    
    contacts = lodad_contacts(file_name)
    last_name = input('Please enter a last name to look up: ').strip()#.strip() is used to delete any white space:
    contact_info = contacts.get(last_name)
    
    display_contact_info(contact_info)
    
main()