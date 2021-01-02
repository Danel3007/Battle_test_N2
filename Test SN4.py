a = 'lol'
b = 'lol'
c = 'lol'
import random
import threading
end = True
meter = 0
import time as t
import random, os, sys
import signal

from state import read_state, write_state
from Battle_test_N2 import BossRoom

print('                 ПРОЧИТАЙТЕ                 ')
print('         Если вы набираете что либо        ')
print('      то убедитесь что вы набрали всё,   ')
print('   что хотели, и после этого жмите Enter,')
print('  просто автор ленивая *опа и он не хочет')
print('       тратить время на исправление')
print('       Нажмите Enter если прочитали')
input()

game_state = {
  'items':[
    'kek',
    'hello there',
    'ronaldinho soccer',
    'megalovania',
    'aeiou'
  ],
  'player_health':100,
  'taken':0,
  'charge':0,
  'scared':0,
  'memo':0,
  'choose':0,
  'meter':0,
  'wall':0,
  'sharp':0,
}

coffee = 0
counter = 0

def miniBossFight():
    pass

class StartRoom:
    def __init__(self, lamp, item, passage):
        self.item = item
        self.lamp = lamp
        self.passage = passage
        
class ItemRoom:
    def __init__(self, lamp, item, passage):
        self.item = item
        self.lamp = lamp
        self.passage = passage

class Room:
    def __init__(self, lamp, passage):
        self.lamp = lamp
        self.passage = passage
        
class TestRoom1:
    def __init__(self, lamp):
        self.lamp = lamp

class TestRoom2:
    def __init__(self, lamp):
        self.lamp = lamp

class TestRoom3:
    def __init__(self, lamp):
        self.lamp = lamp

class TestRoom4:
    def __init__(self, lamp):
        self.lamp = lamp


class FinalBossRoom:
    def __init__(self, name):
        self.name = name

class MiniBossRoom:
    def __init__(self, name, passage):
        self.name = name
        self.passage = passage

lamp_dict = ["лампа.","неоновая лампа.","подсвечник.","диско-шар.",'хэллоуинская тыква.','стробоскоп.','люстра.','банка со светлячками.']
itm_dict = ["труба.","ножик.","газовый баллон.","питомец-хедкраб.",'сюрикен.','бумеранг.','коготь Росомахи.','клинок из дамасской стали.']
pass1_dict = ["ведет средневековый туннель","ведет лестница вверх.","ведет горка с лестницей.","ведет велодорожка."]
mini_boss_dict = ['Дарт Вейдер(Звездные Войны)','Донки Конг','Призрак(PACMAN)','Локи(Марвел)','Майлз Эджуорт(Ace Attorney)']
final_boss_dict = ['Дарт Сидиус(Звездные Войны)','Санс(Undertale)']

def random_ItemRoom():
    return ItemRoom(
        random.choice(lamp_dict),
        random.choice(itm_dict),
        random.choice(pass1_dict),
        )

def random_TestRoom1():
    return TestRoom1(
        random.choice(lamp_dict),
)

def random_TestRoom2():
    return TestRoom2(
        random.choice(lamp_dict),
)

def random_TestRoom3():
    return TestRoom3(
        random.choice(lamp_dict),
)

def random_TestRoom4():
    return TestRoom4(
        random.choice(lamp_dict),
)

def random_StartRoom():
    return StartRoom(
        random.choice(lamp_dict),
        random.choice(itm_dict),
        random.choice(pass1_dict),
        )

def random_MiniBossRoom():
    return MiniBossRoom(
        random.choice(mini_boss_dict),
        random.choice(pass1_dict),
        )

def random_FinalBossRoom():
    return FinalBossRoom(
        random.choice(final_boss_dict)        
        )

def random_Room():
    return Room(
        random.choice(lamp_dict),
        random.choice(pass1_dict),
        )

room_map = [
    [ random_StartRoom(), random_StartRoom() ],
    [ random_TestRoom1(), random_TestRoom1() ],
    [ random_MiniBossRoom(), random_MiniBossRoom() ],
    [ random_ItemRoom(), random_ItemRoom() ],
    [ random_TestRoom2(), random_TestRoom2() ],
    [ random_MiniBossRoom(), random_MiniBossRoom() ],
    [ random_ItemRoom(), random_ItemRoom() ],
    [ random_TestRoom3(), random_TestRoom3() ],
    [ random_MiniBossRoom(), random_MiniBossRoom() ],
    [ random_ItemRoom(), random_ItemRoom() ],
    [ random_TestRoom4(), random_TestRoom4() ],
    [ random_MiniBossRoom(), random_MiniBossRoom() ],
    [ random_ItemRoom(), random_ItemRoom() ],
    [ random_TestRoom1(), random_TestRoom1() ],
    [ random_FinalBossRoom(), random_FinalBossRoom() ]
]

def increment():
    global counter
    while True:
        counter = counter + 1
        t.sleep(1)
        
def start():
    level = 0
    room_number = 0

    while True:
        room = room_map[level][room_number]

        if level >= len(room_map)-1:
            break
        
        passages = room_map[level + 1]

        labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

        if isinstance(room, StartRoom):
            print('Вы просыпаетесь в какой-то комнате. Вам становится немного не по себе.')
            print('Вы видите сумку. В сумке лежит',room.item)
            print('Вы встаете и осматриваете комнату. Серые стены, на потолке висит',room.lamp)

        if isinstance(room, MiniBossRoom):
            print()
            room = BossRoom()
            result = room.battle(game_state)


        if isinstance(room, ItemRoom):
            print('В углу стоит чемоданчик. Там лежит',room.item)


        if isinstance(room, Room):
            print('На потолке висит',room.lamp)
            for i in range(len(passages)):
                print('{}: Из комнаты {}'.format(labels[i],passages[i].passage))
            
        if isinstance(room, TestRoom3):
            global counter
            print('Вы входите в желтую и просторную комнату')
            print('Вы видите записку (да ладно!): "Код состоит из четырех цифр и спрятан в комнате."')
            print('"Удачи :D"')
            print('"Аноним III"')
            print('Когда уже закончатся эти анонимы?')
            while True:
                global counter
                print('Что будете делать?')
                print('A: Посмотреть на стену справа')
                print('B: Посмотреть на стену слева')
                print('C: Посмотреть на стену спереди')
                print('D: Посмотреть на стену сзади')
                print('E: Ввести код')
                choice = str(input())
                if choice=='A':
                    while True:
                        print('Вы смотрите на стену справа')
                        print('Вы видите 4 синих книги.')
                        print('1: Пролистать первую')
                        print('2: Пролистать вторую')
                        print('3: Пролистать третью')
                        print('4: Пролистать четвертую')
                        print('5: Назад')
                        choice2 = int(input())
                        if choice2==1:
                            print('Вы пролистали книгу.')
                            print('Там пусто.')
                            continue
                        if choice2==2:
                            print('Вы пролистали книгу.')
                            print('В ней есть надпись: "Первый Мститель"')
                            continue
                        if choice2==3:
                            print('Вы пролистали книгу.')
                            print('В ней есть надпись: "aeiou"')
                            continue
                        if choice2==4:
                            print('Вы пролистали книгу.')
                            print('Она заполнена фразами "Lorem ipsum dolor sit amet."')
                            continue
                        if choice2==5:
                            break

                if choice=='B':
                    while True:
                        print('Вы смотрите на стену слева')
                        print('Там висит три полки')
                        print('1: Посмотреть на первую полку')
                        print('2: Посмотреть на вторую полку')
                        print('3: Посмотреть на третью полку')
                        print('4: Назад')
                        choice2 = int(input())
                        if choice2==1:
                            print('Вы посмотрели на первую полку.')
                            print('Там есть статуя Мыслителя.')
                            print('Вы присмотрелись...')
                            print('...')
                            print('Он опирается на щит Капитана Америки.')
                            print('На щите нарисована цифра 5')
                            print('Эх... Искусство...')
                            continue
                        if choice2==2:
                            print('Вы посмотрели на вторую полку.')
                            print('Там есть чья-то фотография.')
                            print('Это человек в красном жилете и белой рубашке.')
                            print('У него странная прическа и большой браслет на левой руке.')
                            print('А ещё он куда-то показывает. Знакомая картина...')
                            print('Внизу написано:"Второе число - порядковый номер."')
                            continue
                        if choice2==3:
                            print('Вы посмотрели на третью полку')
                            print('Там стоит модель фонтана в виде восьмиугольника.')
                            print('В центре стоит постамент со звездой, а на нем табличка.')
                            print('Там написано - "L is real 2401"')
                            print('Может это код?')
                            continue
                        if choice2==4:
                            break

                if choice=='C':
                    while True:
                        print('Вы смотрите на стену спереди')
                        print('Вы видите дверь с замком, и две тумбы по бокам.')
                        print('1: Открыть первую')
                        print('2: Открыть вторую')
                        print('3: Выйти')
                        choice2 = int(input())
                        if choice2==1:
                            print('Вы подошли к тумбе слева')
                            print('Там две задвижки')
                            print('Какую откроете?')
                            print('1: Верхнюю')
                            print('2: Нижнюю')
                            continue
                        
                        if choice2==2:
                            print('Вы подошли к тумбе справа.')
                            print('Это просто деревянный куб.')
                            print('Сбоку наклеены стикеры:')
                            print('  F G H I J')
                            print('A 5 6 3 8 1')
                            print('B 0 2 8 3 3')
                            print('C 1 0 3 9 7')
                            print('D 4 5 7 2 8')
                            print('E 7 9 5 8 3')
                            print('3:DJ')
                            continue

                        if choice2==3:
                            break

                if choice=='D':
                    while True:
                        global counter
                        print('Вы смотрите на стену сзади')
                        print('Вы видите комфортное кресло.')
                        print('Рядом стоит тумба, а на ней кофе.')
                        print('1: Сесть в кресло.')
                        print('2: Назад')
                        choice2 = int(input())
                        if choice2==1:
                                print('Вы сели в кресло')
                                t.sleep(1)
                                print('...')
                                t.sleep(3)
                                while True:
                                    global counter
                                    global coffee
                                    if coffee==8:
                                        print('Вы выпили весь кофе.')
                                        print('На дне кружки есть надпись:')
                                        print('Последняя цифра - 9')
                                        print('Ну что ж, пригодится')
                                    
                                    print('1: Попить кофе')
                                    print('2: Посидеть и подумать')
                                    print('3: Встать с кресла')
                                    choice2 = int(input())
                                    if choice2==1:
                                        print('Вы глотнули кофе. Он горький, но вкусный.')
                                        coffee = coffee + 1
                                        continue

                                    if choice2==2:
                                        counter = 0
                                        print('Вы сели в кресло.')
                                        print('Оно мягкое :D')
                                        print('1:Выйти')
                                        tim = threading.Thread(target = increment)
                                        tim.start()
                                        choice2 = int(input())
                                        if choice2 == 1:
                                            print('Вы сидели',counter,'секунд')
                                            if counter>=301:
                                                print('???:"Он слишком долго здесь сидит"')
                                                t.sleep(1)
                                                print('????:"Может, у него проблемы?"')
                                                t.sleep(1)
                                                print('???:"Да, он не подходит"')
                                                t.sleep(1)
                                                print('????:"Выпускаем его"')
                                                t.sleep(1)
                                                print('Часть стены отодвинулась')
                                                t.sleep(1)
                                                print('За ней показалась лестница')
                                                t.sleep(1)
                                                print('Идти туда?')
                                                t.sleep(1)
                                                print('Введите ДА или НЕТ:')
                                                choice2 = str(input())
                                                if choice2=='ДА':
                                                    print('Вы прошли в проход и поднялись по лестнице')
                                                    t.sleep(1)
                                                    print('Вы вышли через дверь')
                                                    t.sleep(1)
                                                    print('Снаружи простиралось до самого горизонта пшеничное поле.')
                                                    t.sleep(1)
                                                    print('...')
                                                    t.sleep(1)
                                                    print('...')
                                                    t.sleep(1)
                                                    print('...')
                                                    print('Вы услышали, как дверь сзади хлопнула')
                                                    t.sleep(1)
                                                    print('Хмм... Что теперь делать...')
                                                    t.sleep(2)
                                                    print('Секретная концовка №1 открыта.')
                                                    sys.exit()
                                                elif choice2=='НЕТ':
                                                    print('????:"Почему он не идет?"')
                                                    t.sleep(1)
                                                    print('???:"Хехе. Мы дали ему шанс."')
                                                    t.sleep(1)
                                                    print('???:"Закрывай проход!"')
                                                    t.sleep(1)
                                                    print('????:"Эмм... Хорошо, сэр."')
                                                    t.sleep(1)
                                                    print('Проход закрылся, и пол под вашими ногами раздвинулся.')
                                                    t.sleep(1)
                                                    print('Вы упали в яму внизу')
                                                    t.sleep(2)
                                                    print('Секретная концовка №2 открыта.')
                                                    sys.exit()
                                        continue

                                    if choice2==3:
                                        continue
                        
                    if choice2==2:
                            break
                    
                
                if choice=='E':
                    print('Введите код:')
                    code = int(input())
                    if code==6969:
                        print('Вы ввели 6969')
                        print('Из замка раздался звук:')
                        print('"Серьёзно?"')
                        print('Дверь не открылась')
                        continue
                    if code==2401:
                        print('Вы ввели 2401.')
                        print('Из замка раздался звук:')
                        print('"Ахахах попался! Тут нет Луиджи."')
                        print('Дверь не открылась')
                        continue
                    if code==5489:
                        print('Вы ввели 5489')
                        t.sleep(1)
                        print('...')
                        t.sleep(1)
                        print('Дверь открылась!')
                        break
                
        if isinstance(room, TestRoom1):
            print('Вы видите кодовый замок с запиской.')
            print('"Птоирачй эотт тксет. Елси ты пнимашоеь эотт тсект, это хшооро, вдеь он пнаодибстя при ршнееии днаонй гмовооллкои."')
            print('"Сшлауй сдюа, зпомнаи: птяь чтреые всемоь дветяь. Сотп, это нпрьвеилнао. Пиралвньо - чытрее всомеь дястеь."')
            print('"Удачи :D"')
            print('"-Аноним"')
            while True:
                print('Введите код:')
                code = int(input())
                if code==4810:
                    print('Правильно :D')
                    break
                else:
                    print('Неправильно')
                    continue

        if isinstance(room, TestRoom2):
            print('Вы видите кодовый замок (опять?) с запиской.')
            print('"Найди знак доллара и напиши где он"')
            print('Ниже видно вот что:')
            print('    A B C D E F G H I J K L M N')
            print('                               ')
            print('1   8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('2   8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('3   8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('4   8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('5   8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('6   8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('7   8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('8   8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('9   8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('10  8 8 8 8 8 8 8 8 8 8 8 $ 8 8')
            print('11  8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('12  8 8 8 8 8 8 8 8 8 8 8 8 8 8')
            print('"Удачи :D"')
            print('"-Аноним II"')
            while True:
                print('Введите код (сначала заглавную букву, потом цифру, слитно):')
                code = str(input())
                if code=='L10':
                    print('Правильно :D')
                    break
                else:
                    print('Неправильно')
                    continue

        if isinstance(room, TestRoom4):
            n69=0
            print('Вы видите кодовый замок (да сколько можно?) с запиской.')
            print('"aeiou"')
            print('"Удачи :D"')
            print('"-Аноним IV"')
            print('И что делать?')
            t.sleep(1)
            print('...')
            t.sleep(1)
            print('Вы перевернули записку')
            print('Там написано: "Сдвиг - 4 буквы влево"')
            print('УГЦА ХИРА ЗИЁГЦА ТЗМС""')
            while True:
                print('Введите код:')
                code = int(input())
                if code==5791:
                    print('Правильно :D')
                    break
                elif code==6969:
                    print('Неправильно')
                    n69=n69+1
                    if n69==4:
                        print('???:"Он настолько испорчен?"')
                        t.sleep(1)
                        print('????:"Видимо да"')
                        t.sleep(1)
                        print('???:"Он нам не подходит, заканчивайте тестирование"')
                        t.sleep(1)
                        print('???:"Да, сэр."')
                        t.sleep(1)
                        print('Пол под вашими ногами открылся и вы упали вниз.')
                        t.sleep(2)
                        print('Секретная концовка №3 открыта.')
                        sys.exit()
                    else:
                        continue
                    
                else:
                    print('Неправильно')
                    continue

        #for passage in passages:
        #    print('Из комнаты',passage.passage)
        
        print('Enter: Перейти в следующую комнату')
        input()

        level += 1

#Shutdown :\
def handler(signum, frame):
    print()
    write_state(game_state)
    sys.exit(0)

signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGINT, handler)

start()
