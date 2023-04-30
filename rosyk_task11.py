import re

def address_search(line):
    # address_pattern = r'(адреса|адр\.|вул\.)\s+[\w\s]+'
    address_pattern = r"(вулиця|вул\.)\s+[A-ZА-ЯЄЇІ][a-zа-яєїі ']*,\s+\d+(,\s+(кв|кв\.)\s+\d+)*"
    address_match = re.search(address_pattern, line, re.IGNORECASE)
    return address_match.group(0) if address_match else 'no address'


def name_search(line):
    name_pattern = r"[A-ZА-ЯЄЇІ][a-zа-яєїі']+\s+[A-ZА-ЯЄЇІ][a-zа-яєїі'\.]+\s+[A-ZА-ЯЄЇІ][a-zа-яєїі'\.]+"
    name_match = re.search(name_pattern, line)
    return name_match.group(0) if name_match else 'no name'


def debt_search(line):
    debt_pattern = r'\d+$'
    debt_match = re.search(debt_pattern, line)
    return debt_match.group(0) if debt_match else 'no debt'


def phone_search(line):
    phone_pattern = r'\+*(38)*\s*\(*\d{3}\)*\s*\d{3}\s*\d{2}\s*\d{2}'
    phone_match = re.search(phone_pattern, line)
    return phone_match.group(0) if phone_match else 'no phone'


def create_letter():
    with open('people.txt', 'r', encoding='utf-8') as info, open('letters.txt', 'w', encoding='utf-8') as letters:
        for line in info:
            letter = f'{address_search(line)}\n{phone_search(line)}\nDear {name_search(line)}\nThe amount of your debt for services is {debt_search(line)}.\nPlease pay the debt within a month. Otherwise, the provision of services will be discontinued\n\n'
            letters.write(letter)


if __name__ == '__main__':
    create_letter()
