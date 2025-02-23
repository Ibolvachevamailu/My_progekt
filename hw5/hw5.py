import datetime
import os


class MediaData:

    # def __new__(cls):
    #     instance = super().__new__(cls)
    #     return instance

    def __init__(self, name: str, filesize:int, autor:str, creation_date: datetime, path: str):
        self.name = name
        self.creation_date = creation_date
        self.file_size = filesize
        self.autor = autor
        self.path = path


    def __str__(self):#для преобразованя в читаемую форму
        return f' {self.value} '

    def __repr__(self):#для преобразованя в читаемую форму
        return f'{self.value}'

    def __add__(self, other: int):#для работы add как сумма чисел
        return MediaData(self.value + other.value)

class Video(MediaData):
    # здесь будут методы типа save, open, rename, delete в зависимости от типов файлов

    def read_(self):
        # Здесь будет код для чтения из облака
        print(f"Чтение файла {self.path}")
        return f'чтение файла {self.path}'

    pass

class Audio(MediaData):
    # здесь будут методы типа save, open, rename, delete в зависимости от типов файлов
    def delite(self):
        return os.remove(self.name)
    pass

class Photo(MediaData):
    # здесь будут методы типа save, open, rename, delete в зависимости от типов файлов

    def rename(self, new_name):
        return os.rename(self.name, new_name)
    pass

print(os.getcwd())

#объявляем переменные
media3 = Video('C:/Users/Инна/Desktop/WIN_20150711_124528.JPG', 4, 'df', (2025, 2, 4), 'C:/Users/Инна/Desktop/WIN_20150711_124528.JPG')
mf_path = 'C:/Users/Инна/Desktop/Dimasik_.mp3'
media1 = Photo('C:/Users/Инна/Desktop/WIN_20150711_124528.JPG',2,'inna', datetime.date(2024, 12, 2), mf_path)
photo_path = 'C:/Users/Инна/Desktop/Dima.mp3'
media2 = Audio('C:/Users/Инна/Desktop/Dima.mp3', 3,'nata', datetime.date(2025, 1, 3), photo_path)
video1 = Video('https://docs.google.com/spreadsheets/d/1vqtrZbLnc_mQqKTMTN4dJJ38pcwoLKscdAfWhsZBQ3s/edit?usp=sharing', 5, 'inna_b', (2024, 2, 12), 'https://docs.google.com/spreadsheets/d/1vqtrZbLnc_mQqKTMTN4dJJ38pcwoLKscdAfWhsZBQ3s/edit?usp=sharing')

#пробуем работают ли методы
print((media1.file_size + media2.file_size))
media1.rename('C:/Users/Инна/Desktop/my_photo.JPG')#переименование файла
media2.delite()
video1.read_()
