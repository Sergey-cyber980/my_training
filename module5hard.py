class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration  # в секундах
        self.time_now = 0  # текущая секунда остановки
        self.adult_mode = adult_mode  # ограничение по возрасту



class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        self.nickname = nickname
        if password == password:
            self.password = password
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему.")
                return
        print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")

    def log_out(self):
        self.current_user = None
        print("Пользователь вышел из системы.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует.")

    def get_videos(self, search_term):
        search_term_lower = search_term.lower()
        return [video.title for video in self.videos if search_term_lower in video.title.lower()]

    def watch_video(self, title):
        for video in self.videos:
            if video.title == title:
                print(f"Начало просмотра видео '{title}'.")
                while video.time_now < video.duration:
                    print(f"Просмотр на {video.time_now} сек.")
                    video.time_now += 1  # имитация просмотра
                print(f"Просмотр видео '{title}' завершен.")
                video.time_now = 0  # сброс времени
                return
        print(f"Видео '{title}' не найдено.")


if __name__ == "main":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    # v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

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
