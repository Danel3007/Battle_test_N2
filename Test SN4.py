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
from FinalBoss import FinBossRoom


def input_choice(choices):
    with term.cbreak(), term.hidden_cursor():
        choice = 0

        loc = term.height - len(choices) - 1
        for i in range(len(choices)):
            print()

        while True:
            #print(f"{term.home}{term.clear}")
           
            for i in range(len(choices)):
                with term.location(0, loc + i):
                    c = choice % len(choices)
                    if c == i:
                        print(f"{term.underline}{choices[i]}{term.no_underline}", end='')
                    else:
                        print(f"{choices[i]}", end='')
            
            val = term.inkey()

            if val.name == 'KEY_DOWN':
                choice += 1
            elif val.name == 'KEY_UP':
                choice -= 1
            elif val.name == "KEY_ENTER":
                break

        return choice % len(choices)

print('                 ПРОЧИТАЙТЕ                 ')
print('         Если вы набираете что либо        ')
print('      то убедитесь что вы набрали всё,   ')
print('   что хотели, и после этого жмите Enter,')
print('  просто автор ленивая *опа и он не хочет')
print('       тратить время на исправление')
print('       Нажмите Enter если прочитали')
input()
t.sleep(2)
print('       The Adventure     ')
print('Нажмите Enter чтобы начать')
input()
print('Запускаем игру...')
t.sleep(2)

game_state = {
  'items':[

  ],
  'trial': 0,
  'player_health':100,
  'taken':0,
  'charge':0,
  'scared':0,
  'memo':0,
  'choose':0,
  'meter':0,
  'wall':0,
  'sharp':0,
  'lamp':0,
  'knife':0,
  'shoruken':0,
  'pipe':0,
  'crab':0,
  'ballon':0,
  'potions':0
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
itm_dict = ["лампа.","труба.","ножик.","газовый баллон.","питомец-хедкраб.",'сюрикен.']
pass1_dict = ["ведет средневековый туннель","ведет лестница вверх.","ведет горка с лестницей.","ведет велодорожка."]
mini_boss_dict = ['Дарт Вейдер(Звездные Войны)','Донки Конг','Призрак(PACMAN)','Локи(Марвел)','Майлз Эджуорт(Ace Attorney)']
final_boss_dict = ['Санс(Undertale)','Дио Брандо(ДжоДжо Часть 3)']

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
    [ random_FinalBossRoom(), random_FinalBossRoom() ]
]

def increment():
    global counter
    while True:
        counter = counter + 1
        t.sleep(1)

def caesar(text, shift):
    ciphertext = ''

    for c in text:
        if c == ' ':
            ciphertext += ' '
            continue

        index = ord(c)

        alpha_no = index - ord('А')
        shifted = (alpha_no + shift) % 32

        new_index = ord('А') + shifted

        ciphertext += chr(new_index)

    return ciphertext

def int_input():
    text = input()
    try:
        return int(text)
    except ValueError as err:
        return 0

        
def start():
    level = 0
    room_number = 0

    while True:
        room = room_map[level][room_number]

        #if level >= len(room_map)-1:
        #    break

        if level == len(room_map)-1:
            passages = []
        else:
            passages = room_map[level+1]

        labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

        if isinstance(room, StartRoom):
            print('Вы просыпаетесь в какой-то комнате. Вам становится немного не по себе.')
            input()
            print('Вы видите сумку. В сумке лежит',room.item)
            game_state['items'].append(room.item)
            input()
            print('Вы встаете и осматриваете комнату. Серые стены, на потолке висит',room.lamp)

        if isinstance(room, MiniBossRoom):
            print()
            room = BossRoom()
            result = room.battle(game_state)

        if isinstance(room, FinalBossRoom):
            print()
            room = FinBossRoom()
            result = room.battlef(game_state)

            if result == "WIN":
                print('')
            else:
                print('Вы проиграли :(')

            break

        if isinstance(room, ItemRoom):
            while True:
                if room.item not in game_state['items']:
                    game_state['items'].append(room.item)
                    print('В углу стоит чемоданчик. Там лежит',room.item)
                    break
                else:
                    continue
            print('Также там лежат 5 зелий лечения.')
            game_state['potions'] += 5


        if isinstance(room, Room):
            print('На потолке висит',room.lamp)
            for i in range(len(passages)):
                print('{}: Из комнаты {}'.format(labels[i],passages[i].passage))
            
        if isinstance(room, TestRoom3):
            global counter
            print('Вы входите в желтую и просторную комнату')
            input()
            print('Вы видите записку (да ладно!): "Код состоит из четырех цифр и спрятан в комнате."')
            input()
            print('"Удачи :D"')
            input()
            print('"Аноним III"')
            input()
            print('Когда уже закончатся эти анонимы?')
            input()
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
                        input()
                        print('Вы видите 4 синих книги.')
                        input()
                        print('1: Пролистать первую')
                        print('2: Пролистать вторую')
                        print('3: Пролистать третью')
                        print('4: Пролистать четвертую')
                        print('5: Назад')
                        choice2 = int(input())
                        if choice2==1:
                            print('Вы пролистали книгу.')
                            input()
                            print('Там пусто.')
                            input()
                            continue
                        if choice2==2:
                            print('Вы пролистали книгу.')
                            input()
                            print('В ней есть надпись: "Первый Мыслитель"')
                            input()
                            continue
                        if choice2==3:
                            print('Вы пролистали книгу.')
                            input()
                            print('В ней есть надпись: "aeiou"')
                            input()
                            continue
                        if choice2==4:
                            print('Вы пролистали книгу.')
                            input()
                            print('Она заполнена фразами "Lorem ipsum dolor sit amet."')
                            input()
                            continue
                        if choice2==5:
                            break

                if choice=='B':
                    while True:
                        print('Вы смотрите на стену слева')
                        input()
                        print('Там висит три полки')
                        input()
                        print('1: Посмотреть на первую полку')
                        print('2: Посмотреть на вторую полку')
                        print('3: Посмотреть на третью полку')
                        print('4: Назад')
                        choice2 = int(input())
                        if choice2==1:
                            print('Вы посмотрели на первую полку.')
                            input()
                            print('Там есть статуя Мыслителя.')
                            input()
                            print('Вы присмотрелись...')
                            input()
                            print('Он опирается на щит Капитана Америки.')
                            input()
                            print('На щите нарисована цифра 5')
                            input()
                            print('Эх... Искусство...')
                            input()
                            continue
                        if choice2==2:
                            print('Вы посмотрели на вторую полку.')
                            input()
                            print('Там есть чья-то фотография.')
                            input()
                            print('Там написано:"Второе - сколько цифр в коде."')
                            input()
                            continue
                        if choice2==3:
                            print('Вы посмотрели на третью полку')
                            input()
                            print('Там стоит модель фонтана в виде восьмиугольника.')
                            input()
                            print('В центре стоит постамент со звездой, а на нем табличка.')
                            input()
                            print('Там написано - "L is real 2401"')
                            input()
                            print('Может это код?')
                            input()
                            continue
                        if choice2==4:
                            break

                if choice=='C':
                    while True:
                        print('Вы смотрите на стену спереди')
                        input()
                        print('Вы видите дверь с замком, и две тумбы по бокам.')
                        input()
                        print('1: Открыть первую')
                        print('2: Открыть вторую')
                        print('3: Выйти')
                        choice2 = int(input())
                        if choice2==1:
                            print('Вы подошли к тумбе слева')
                            input()
                            print('Там две задвижки')
                            input()
                            print('Какую откроете?')
                            input()
                            print('1: Верхнюю')
                            print('2: Нижнюю')
                            continue
                        
                        if choice2==2:
                            print('Вы подошли к тумбе справа.')
                            input()
                            print('Это просто деревянный куб.')
                            input()
                            print('Сбоку наклеены стикеры:')
                            input()
                            print('  F G H I J')
                            print('A 5 6 3 8 1')
                            print('B 0 2 8 3 3')
                            print('C 1 0 3 9 7')
                            print('D 4 5 7 2 8')
                            print('E 7 9 5 8 3')
                            print('Третья:DJ')
                            input()
                            continue

                        if choice2==3:
                            break

                if choice=='D':
                    while True:
                        global counter
                        print('Вы смотрите на стену сзади')
                        input()
                        print('Вы видите комфортное кресло.')
                        input()
                        print('Рядом стоит тумба, а на ней кофе.')
                        input()
                        print('1: Сесть в кресло.')
                        print('2: Назад')
                        choice2 = int(input())
                        if choice2==1:
                                print('Вы сели в кресло')
                                input()
                                while True:
                                    global counter
                                    global coffee
                                    if coffee==8:
                                        print('Вы выпили весь кофе.')
                                        input()
                                        print('На дне кружки есть надпись:')
                                        input()
                                        print('Последняя цифра - 9')
                                        input()
                                        print('Ну что ж, пригодится')
                                        input()
                                    
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
                                        input()
                                        print('Оно мягкое :D')
                                        input()
                                        print('Тут можно посидеть и подумать')
                                        input()
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
                    
                
                if choice==4:
                    print('Введите код:')
                    code = int(input())
                    if code==6969:
                        print('Вы ввели 6969')
                        input()
                        print('Из замка раздался звук:')
                        input()
                        print('"Серьёзно?"')
                        input()
                        print('Дверь не открылась')
                        input()
                        continue
                    if code==2401:
                        print('Вы ввели 2401.')
                        input()
                        print('Из замка раздался звук:')
                        input()
                        print('"Ахахах попался! Тут нет Луиджи."')
                        input()
                        print('Дверь не открылась')
                        input()
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
            input()
            print('"Птоирачй эотт тксет. Елси ты пнимашоеь эотт тсект, это хшооро, вдеь он пнаодибстя при ршнееии днаонй гмовооллкои."')
            input()
            print('"Сшлауй сдюа, зпомнаи: птяь чтреые всемоь дветяь. Сотп, это нпрьвеилнао. Пиралвньо - чытрее всомеь дястеь."')
            input()
            print('"Удачи :D"')
            input()
            print('"-Аноним"')
            input()
            while True:
                print('Введите код:')
                code = int_input()
                if code==4810:
                    print('Правильно :D')
                    break
                else:
                    print('Неправильно')
                    continue

        if isinstance(room, TestRoom2):
            print('Вы видите кодовый замок (опять?) с запиской.')
            input()
            print('"Найди знак доллара и напиши где он"')
            input()
            print('Ниже видно вот что:')
            input()
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
            input()
            print('"Удачи :D"')
            input()
            print('"-Аноним II"')
            input()
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
            input()
            print('"aeiou"')
            input()
            print('"Удачи :D"')
            input()
            print('"-Аноним IV"')
            input()
            print('И что делать?')
            input()
            print('Вы перевернули записку')
            input()
            hi = 'ПЯТЬ СЕМЬ ДЕВЯТЬ ОДИН'
            yo = random.randint(1,7)
            print('Там написано: "Сдвиг - ',yo,'"')
            print(caesar(hi,yo))
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
