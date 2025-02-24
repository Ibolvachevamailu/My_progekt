import datetime
import os.path
import requests


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

    def __add__(self, other):#для работы add как сумма чисел
        return MediaData(self.file_size + other)


class Video(MediaData):
    # здесь будут методы типа save, open, rename, delete в зависимости от типов файлов
    def download_from_url(self, url, save_path):
        pass

    def upload_to_s3(self, file_path, bucket_name, object_name=None):
        pass

    pass

class Audio(MediaData):
    # здесь будут методы типа save, open, rename, delete в зависимости от типов файлов
    def delite(self, path):
        if os.path.exists(path):
            print(f'файл {path} удалён')
            return os.remove(self.path)
        else:
            print(f'файла не существует')
    pass

class Photo(MediaData):
    # здесь будут методы типа save, open, rename, delete в зависимости от типов файлов

    def rename(self,path, new_name):
        if os.path.exists(path):
            print(f'файл {path} переименован')
            return os.rename(self.name, new_name)
        else:
            print(f'файла не существует')

    pass

#объявляем переменные
media3 = Video('C:/Users/Инна/Desktop/WIN_20150711_124528.JPG', 4, 'df', datetime.date(2020, 11,14), 'C:/Users/Инна/Desktop/WIN_20150711_124528.JPG')
mf_path = 'C:/Users/Инна/Desktop/IMG_20200630_195058.jpg'
media1 = Photo(mf_path,2,'inna', datetime.date(2024, 12, 2), mf_path)
photo_path = 'C:/Users/Инна/Desktop/IMG_20200630_195128.jpg'
media2 = Audio(photo_path, 3,'nata', datetime.date(2025, 1, 3), photo_path)



#пробуем работают ли методы
# print((media1.file_size + media2.file_size))
# media1.rename(media1.path,'C:/Users/Инна/Desktop/my_photo2.JPG')#переименование файла
# media2.delite(media2.path) #проверка удаления файла
# print(media3.creation_date)


class CloudStorageMixin(MediaData):
# """Mixin для работы с файлами в облаке и удаленных хранилищах."""

    def download_from_url(self, url, save_path):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
                    print(f'Файл скачан: {save_path}')
        else:
            print(f'Ошибка скачивания: {response.status_code}')

    def upload_to_s3(self, file_path, bucket_name, object_name=None):
        s3 = boto3.client('s3')
        if object_name is None:
            object_name = os.path.basename(file_path)
            try:
                s3.upload_file(file_path, bucket_name, object_name)
                print(f'Файл {file_path} загружен в S3 как {object_name}')
            except NoCredentialsError:
                print('Ошибка: Не указаны учетные данные для AWS S3')

# В облаке:
video_cloud = Video(
'https://example.com/video.mp4', # URL удаленного файла
10, 'cloud_user', datetime.date(2024, 2, 24),
'/tmp/video.mp4' # Временный путь для скачивания
)
video_cloud.download_from_url(video_cloud.name, video_cloud.path) # Скачивание
video_cloud.upload_to_s3(video_cloud.name,"my-bucket") # Загрузка в S3





