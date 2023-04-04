import phone_book

pb = phone_book.PhoneBook('phone_db.txt')
print(pb)
#pb.new_contact('Веня', '8954625274', 'Учитель')
#print(pb)
#pb.save()
print(pb.search('А'))
while True:
    print(pb.menu())
    choice = int(input('Выберете пункт меню: '))
    match choice:
        case 1:
            print(pb)
        case 2:
           name = input('Введите имя: ')
           phone = input('Введите номер телефона: ')
           comment = input('Введите комментарий: ')
           pb.new_contact(name, phone, comment)
        case 3:
            print(pb)
            index = int(input('Введите индекс контакта: '))
            name = input('Введите имя, или пропустите: ')
            phone = input('Введите номер телефона, или пропустите: ')
            comment = input('Введите комментарий, или пропустите: ')
            pb.change(index-1, name, phone, comment)
        case 4:
            pb.save()
        case 5:
            word = input('Найти контакт: ')
            print(pb.search(word))
        case 6:
            index = int(input('Введите индекс контакта, который нужно удалить: '))
            pb.delete(index-1)
        case 7:
            break