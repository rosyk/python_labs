import re


def find_address(line):
    address_pattern = r'(адреса|адр\.*)\s+(вул\.*|вулиця)\s+[a-zA-Zа-яА-Яєії\' ]+,\s+\d+\s+((кв\.*)\s+\d+)*'
    address = re.search(address_pattern, line)
    return address.group(0) if address else 'no address'


def find_name(line):
    name_pattern = r'[А-ЯЄІЇ][а-яєії]+\s+[А-ЯЄІЇа-яєії.]+\s+[А-ЯЄІЇа-яєії.]+'
    name = re.search(name_pattern, line)
    return name.group(0) if name is not None else 'no name'


def find_debt(line):
    debt_pattern = r'\d+$'
    debt = re.search(debt_pattern, line)
    return debt.group(0) if debt is not None else 'no debt'


def find_phone(line):
    phone_pattern = r'(телефон|тел\.*)+\s+(\+*38)*0\d{2} *\d{3} *\d{2} *\d{2}'
    phone = re.search(phone_pattern, line)
    return phone.group(0) if phone is not None else 'no phone'


def find_date(line):
    date_pattern = r'(\d{1,2}[.\-/]\d{1,2}[.\-/]\d{4})|(\d{4}[.\-/]\d{1,2}[.\-/]\d{1,2})'
    date = re.search(date_pattern, line)
    return date.group(0) if date is not None else 'no date'


def find_student_phone(line):
    student_phone_pattern = r'(\+*38)*0\d{2}\d{3}\d{2}\d{2}'
    student_phone = re.search(student_phone_pattern, line)
    if student_phone is not None:
        return '+380' + student_phone.group(0)[-9:]
    else:
        return 'no phone'


def find_number(line):
    number_pattern = r'\d{5}'
    number = re.search(number_pattern, line)
    return number.group(0) if number is not None else 'no number'


def create_letter():
    with open('people.txt', 'r', encoding='utf-8') as file, open('letters.txt', 'w', encoding='utf-8') as letters:
        for line in file:
            letter = f'{find_phone(line)}, {find_address(line)}\n' \
                     f'Dear {find_name(line)}\n' \
                     f'The amount of your debt for services is {find_debt(line)}.\n' \
                     f'Please pay the debt within a month. ' \
                     f'Otherwise, the provision of services will be discontinued.\n\n'
            letters.write(letter)


def create_dict():
    students_dict = {}
    with open('students.txt', 'r', encoding='utf-8') as file:
        for line in file:
            student_information = f'{find_name(line)}, {find_date(line)}, {find_student_phone(line)}'
            students_dict.update({find_number(line): student_information})
    return students_dict


if __name__ == '__main__':
    create_letter()
    print(create_dict())
