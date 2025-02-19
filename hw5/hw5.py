from datetime import datetime


class MediaDada:
#переделать создание атрибутов на уровне инита
    def __new__(cls, value, name, filesize, autor, creation_date):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.creation_date = creation_date
        instance.file_size = filesize
        instance.autor = autor
        return instance

    def __init__(self, value):
        self.value = value

    def __str__(self):#для преобразованя в читаемую форму
        return f' {self.value} '

    def __repr__(self):#для преобразованя в читаемую форму
        return f'{self.value}'

    #определить м-ды

class Video(MediaDada):
    pass

class Audio(MediaData):
    pass

class Photo(MediaDada):
    pass


