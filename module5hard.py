"""
modul5hard
"""
import time

class UrTube:
    """
    Urban Youtube Video Hosting Service
    """
    users = []   # список объектов User
    videos = []  # список объектов Video
    current_user = None  # текущий пользователь, User

    def add(self, *vlist):
        """
        :param vlist:  список видео
        :return: None
        """
        for video in vlist:
            if video not in UrTube.videos:
                UrTube.videos.append(video)

    def get_videos(self, search):
        retlist = []
        for video in UrTube.videos:
            title = str(video)
            if search.upper() in title.upper():
                retlist.append(title)
        return retlist

    def watch_video(self, title):
        if UrTube.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in UrTube.videos:
            if str(video) == title:
                # Проверить доступность видео
                if UrTube.current_user.age < 18 and video.adult_mode:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    break
                for i in range(video.duration):
                    video.time_now = i + 1
                    print(video.time_now, end=' ')
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                break  # выйти из цикла поиска

    def log_in(self, nickname, password):
        """
        :param nickname:
        :param password:
        :return:
        Метод log_in пытается найти пользователя в users
        с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        """
        for user in UrTube.users:
            if user.nickname == nickname and user.password == hash(password):
                UrTube.current_user = user
                break

    def register(self, nickname, password, age):
        """
        :param nickname:
        :param password:
        :param age:
        :return:
        Метод register добавляет пользователя в список,
        если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
        "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
        """
        for user in UrTube.users:
            if user == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        user = User(nickname, hash(password), age)
        UrTube.users.append(user)
        UrTube.current_user = user

    def log_out(self):
        """
        Сброс текущего пользователя на None.
        """
        UrTube.current_user = None

class Video:
    """
    Работа с видео
    """
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        """
        Атрибуты: title (заголовок, строка),
        duration (продолжительность, секунды),
        time_now (секунда остановки (изначально 0)),
        adult_mode (ограничение по возрасту, bool (False по умолчанию)
        """
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title

class User:
    """
    Поддержка пользователей сервиса: регистрация, вход, удаление
    """
    def __init__(self, nickname, password, age):
        """
        nickname (имя пользователя, строка),
        password (в хэшированном виде, число),
        age (возраст, число)
        """
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if other == None:
            if self.nickname == None:
                return True
            else:
                return False

        if isinstance(other, User):
            if self.nickname == other.nickname:
                return True
            else:
                return False
        elif isinstance(other, str):
            if self.nickname == other:
                return True
            else:
                return False
        else:
            print('Unknown class type ', type(other))
            return None

"""
Код для проверки:
"""
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
print(ur.current_user)

ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

#eof-module5hard