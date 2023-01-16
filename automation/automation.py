import re


def contacts(file:str, email_pattern:str, phone_pattern:str):
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    phone_pattern = r'(?:\+?1[-. ]?)?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})|([0-9]{7})$'

    email_re = re.compile(email_pattern)
    phone_re = re.compile(phone_pattern)

    with open("assets/potential-contacts.txt", "r") as f:
        data = f.read()

    emails = set(email_re.findall(data))
    phones = set(phone_re.findall(data))
    phone_numbers = ['{}-{}-{}'.format(num[0], num[1], num[2]) for num in phones]

    with open('phone_numbers.txt', 'w') as ef:
        for email in emails:
            ef.write(email + '\n')

    with open('emails.txt', 'w') as pf:
        for phone in phone_numbers:
            pf.write(phone + '\n')


contacts('./assets/potential_contacts.txt', 'outputs/emails.txt', 'outputs/phone_numbers.txt')
