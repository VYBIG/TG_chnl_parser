def phone_number_right(phone: str):
    phone = ''.join(filter(str.isdigit, phone))
    phone = '+7' + phone[1:]
    return phone


def write_in_file(write_phrase):
    with open('parcing.txt', 'a', encoding='utf-8') as file:
        file.write(f'{write_phrase}\n')


