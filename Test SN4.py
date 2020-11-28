a = 'lol'
b = 'lol'
c = 'lol'
import random
end = True
meter = 0
import time as t
import random, os
import signal

from state import read_state, write_state
from Battle_test_N2 import BossRoom

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
boss_dict = ['Дарт Сидиус(Звездные Войны)','Санс(Undertale)']

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
        random.choice(boss_dict)        
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
    [ random_TestRoom1(), random_TestRoom1() ],
    [ random_MiniBossRoom(), random_MiniBossRoom() ],
    [ random_ItemRoom(), random_ItemRoom() ],
    [ random_TestRoom1(), random_TestRoom1() ],
    [ random_MiniBossRoom(), random_MiniBossRoom() ],
    [ random_ItemRoom(), random_ItemRoom() ],
    [ random_TestRoom1(), random_TestRoom1() ],
    [ random_MiniBossRoom(), random_MiniBossRoom() ],
    [ random_ItemRoom(), random_ItemRoom() ],
    [ random_TestRoom1(), random_TestRoom1() ],
    [ random_FinalBossRoom(), random_FinalBossRoom() ]
]


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
            
        if isinstance(room, TestRoom1):
            print('Птоирачй эотт тксет. Елси ты пнимашоеь эотт тсект, это хшооро, вдеь он пнаодибстя при ршнееии днаонй гмовооллкои.')
            print('Сшлауй сдюа, зпомнаи: птяь чтреые всемоь дветяь. Сотп, это нпрьвеилнао. Пиралвньо - чытрее всомеь дястеь.')
            print('Удачи :D')
            print('Аноним')
            print('Введите код:')
            code = int(input())
            if code==4810:
                print('Правильно :D')
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
