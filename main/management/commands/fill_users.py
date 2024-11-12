from django.core.management.base import BaseCommand, CommandError
from main.models import User
from random import choice, randint

NAMES = [
    "Александр", "Алексей", "Андрей", "Антон", "Артём", "Артур", "Богдан", "Борис", "Вадим", "Валентин",
    "Валерий", "Василий", "Виктор", "Виталий", "Владимир", "Владислав", "Всеволод", "Геннадий", "Георгий", "Герман",
    "Григорий", "Даниил", "Демид", "Денис", "Дмитрий", "Евгений", "Егор", "Иван", "Игнат", "Игорь",
    "Илья", "Кирилл", "Константин", "Лев", "Леонид", "Макар", "Максим", "Марк", "Михаил", "Никита",
    "Николай", "Олег", "Павел", "Петр", "Роман", "Ростислав", "Руслан", "Семён", "Сергей", "Станислав",
    "Степан", "Тимофей", "Фёдор", "Юрий", "Ярослав", "Агата", "Аделина", "Александра", "Алена", "Алина",
    "Алиса", "Анастасия", "Анжелика", "Анна", "Валентина", "Валерия", "Варвара", "Василиса", "Вера", "Вероника",
    "Виктория", "Галина", "Дарья", "Диана", "Ева", "Евгения", "Екатерина", "Елена", "Елизавета", "Жанна",
    "Зинаида", "Злата", "Инна", "Ирина", "Карина", "Кира", "Кристина", "Лариса", "Лидия", "Любовь",
    "Людмила", "Маргарита", "Марина", "Мария", "Милана", "Надежда", "Наталья", "Нина", "Оксана", "Ольга",
    "Полина", "Раиса", "Регина", "Светлана", "Снежана", "София", "Тамара", "Татьяна", "Ульяна", "Эвелина",
    "Юлия", "Яна", "Абрам", "Агафья", "Азарий", "Аким", "Алина", "Алихан", "Альбина", "Амелия",
    "Амир", "Амина", "Анфиса", "Арсений", "Ася", "Бэлла", "Варя", "Вениамин", "Глеб", "Елисей",
    "Захар", "Зоряна", "Зоя", "Инга", "Инесса", "Камилла", "Клим", "Кристоф", "Лука", "Майя",
    "Милан", "Мирон", "Миша", "Наум", "Платон", "Радмила", "Ренат", "Ринат", "Роза", "Руслана",
    "Савелий", "Слава", "Таисия", "Филипп", "Шамиль", "Эмиль", "Юнона", "Ян"
]

SURNAMES = [
    "Иванов", "Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Соколов", "Михайлов", "Новиков", "Фёдоров",
    "Морозов", "Волков", "Алексеев", "Лебедев", "Семенов", "Егоров", "Павлов", "Козлов", "Степанов", "Николаев",
    "Орлов", "Андреев", "Макаров", "Никитин", "Захаров", "Зайцев", "Соловьёв", "Борисов", "Яковлев", "Григорьев",
    "Романов", "Воробьёв", "Сергеев", "Кузьмин", "Фролов", "Александров", "Дмитриев", "Королев", "Гусев", "Киселёв",
    "Ильин", "Максимов", "Поляков", "Сорокин", "Виниченко", "Петухов", "Лебедев", "Савин", "Трофимов", "Мартынов",
    "Тихомиров", "Карпов", "Гордеев", "Антонов", "Селезнёв", "Панфилов", "Баранов", "Калинин", "Анисимов", "Галкин",
    "Лазарев", "Коновалов", "Белоусов", "Мельников", "Герасимов", "Коновалов", "Ефимов", "Громов", "Фомин", "Давыдов",
    "Мельников", "Петухов", "Голубев", "Кириллов", "Воронин", "Денисов", "Крылов", "Беляков", "Тимофеев", "Маслов",
    "Зубков", "Лукин", "Тетерин", "Моисеев", "Ершов", "Панков", "Пастухов", "Федосеев", "Устинов", "Нефедов",
    "Суворов", "Гуляев", "Лапин", "Прохоров", "Наумов", "Соболев", "Рыбаков", "Селиванов", "Шубин", "Лапшин",
    "Горшков", "Сафонов", "Чернов", "Филатов", "Лазарев", "Медведев", "Евдокимов", "Савельев", "Симонов", "Брусков",
    "Малинин", "Смоляков", "Архипов", "Терентьев", "Кочетков", "Погодин", "Вешняков", "Баженов", "Гусаров", "Бухаров",
    "Овсянников", "Рогов", "Карпин", "Чистяков", "Котов", "Рубцов", "Ромашин", "Горин", "Фокин", "Грачев",
    "Рожков", "Титов", "Владимиров", "Федосов", "Градов", "Шаров", "Курочкин", "Шашков", "Кожевников", "Щербаков",
    "Круглов", "Черепанов", "Обухов", "Крюков", "Жуков", "Третьяков", "Сухоруков", "Брагин", "Соколовский", "Фадеев"
]

def create_user_list(ratio):
    users = [User(username=f'{choice(SURNAMES)}_{choice(NAMES)}_{randint(1950, 2010)}', password='111') for _ in
             range(ratio)]
    return users


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        users = create_user_list(kwargs['ratio'])
        User.objects.bulk_create(users)

    def add_arguments(self, parser):
        parser.add_argument("-ratio", type=int)
