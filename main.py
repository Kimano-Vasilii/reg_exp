import re


def process_contacts(contacts):
    # Задача 1: разделить полное имя на фамилию, имя и отчество
    for i, contact in enumerate(contacts):
        if len(contact) >= 3:
            name_parts = contact[0].split(" ")
            if len(name_parts) == 1:  # только фамилия
                contacts[i] = [name_parts[0], "", ""] + contact[1:]
            elif len(name_parts) == 2:  # фамилия и имя
                contacts[i] = [name_parts[0], name_parts[1], ""] + contact[1:]
            elif len(name_parts) >= 3:  # фамилия, имя и отчество
                contacts[i] = [name_parts[0], name_parts[1], " ".join(name_parts[2:])] + contact[1:]

    # Задача 2: форматирование телефонов
    phone_regex = re.compile(r"\+?(\d{1})?(\d{3})(\d{3})(\d{2})(\d{2})([(доб)](\d+))?")
    for i, contact in enumerate(contacts):
        phone_match = phone_regex.match(contact[5])
        if phone_match:
            phone_parts = phone_match.groups()
            formatted_phone = "+7({}){}-{}-{}".format(
                phone_parts[1],
                phone_parts[2],
                phone_parts[3],
                phone_parts[4]
            )
            if phone_parts[6]:  # добавочный номер
                formatted_phone += " доб.{}".format(phone_parts[6])
            contacts[i][5] = formatted_phone

    # Задача 3: объединение дублирующихся записей
    unique_contacts = {}
    for contact in contacts:
        full_name = " ".join(contact[:3])
        if full_name not in unique_contacts:
            unique_contacts[full_name] = contact
        else:
            existing_contact = unique_contacts[full_name]
            if contact[3] and not existing_contact[3]:
                existing_contact[3] = contact[3]
            if contact[4] and not existing_contact[4]:
                existing_contact[4] = contact[4]

    return list(unique_contacts.values())
