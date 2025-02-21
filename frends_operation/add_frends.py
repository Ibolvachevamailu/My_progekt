def add_frends(frends_list, frends_name):
    if frends_name not in frends_list:
        frends_list.append(frends_name)
        return f'{frends_name} добавлен в друзья'
    return f'{frends_name} уже в списке друзей'