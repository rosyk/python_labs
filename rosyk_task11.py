import re


def find_address(line):
    address_pattern = r'(адреса|адр\.*)\s+(вул\.*|вулиця)\s+[a-zA-Zа-яА-Яєії\' ]+,\s+\d+\s+((кв\.*)\s+\d+)*'
    address = re.match(address_pattern, line)
    return address.group(0) if address else 'no address'


def find_name(line):
    name_pattern = r'[a-zA-Zа-яА-Яєії\']+\s+[a-zA-Zа-яА-Яєії\'\.]+\s+[a-zA-Zа-яА-Яєії\'\.]+'
    name = re.match(name_pattern, line)
    return name.group(0) if name is not None else 'no name'


def find_debt(line):
    debt_pattern = r'\d+$'
    debt = re.match(debt_pattern, line)
    return debt.group(0) if debt is not None else 'no debt'


def find_phone(line):
    phone_pattern = r'(телефон|тел\.*)+\s+(\+*38)*0\d{2} *\d{3} *\d{2} *\d{2}'
    phone = re.match(phone_pattern, line)
    return phone if phone is not None else 'no phone'


def create_letter():
    with open('people.txt', 'r', encoding='utf-8') as file, open('letters.txt', 'w', encoding='utf-8') as letters:
        for line in file:
            letter = f'{find_phone(line)}, {find_address(line)}\n' \
                     f'Dear {find_name(line)}\n' \
                     f'The amount of your debt for services is {find_debt(line)}.\n' \
                     f'Please pay the debt within a month. ' \
                     f'Otherwise, the provision of services will be discontinued.\n\n'
        letters.write(letter)


if __name__ == '__main__':
    create_letter()
