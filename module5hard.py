from time import sleep


class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

class Video:
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users: list[User] = []
        self.videos: list[Video] = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and hash(password) == user.password:
                self.current_user = user
                print('Вы вошли в систему')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
        user = User(nickname, password, age)
        self.users.append(user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos: Video):
        temp = []
        for exist_video in self.videos:
            temp.append(exist_video.title)
        for video in videos:
            if video.title not in temp:
                self.videos.append(video)

    def get_videos(self, search_world):
        temp_videos = []
        for video in self.videos:
            if search_world.lower() in video.title.lower():
                temp_videos.append(video.title)
        return temp_videos

    def watch_video(self, title):
        for video in self.videos:
            if video.title == title:
                if self.current_user is not None:
                    if self.current_user.age >= 18:
                        for seconds in range(video.time_now + 1, video.duration + 1):
                            print(seconds, end = '')
                            sleep(1)
                        print('Конец видео', end = '')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео")


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
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
