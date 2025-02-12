def remove_frends(frends_list, frends_name):
    if frends_name in frends_list:
        frends_list.remove(frends_name)
        return f'{frends_name} удален из друзья'
    return f'{frends_name} нет в списке друзья'

