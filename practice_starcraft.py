from random import *

# 일반 유낫
class Unit: 
    def __init__(self, name, hp, speed):
        self.name = name     
        self.hp = hp  
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))    

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} 은 체력이 없습니다.".format(self.name))

#############
# 지상 공격 유닛
class AttackUnit(Unit):    # Unit을 상속받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 상속받음!!
        self.damage = damage 

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}".format(self.name, location, self.damage))

# 지상 공격 유닛: 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    #스팀팩: 일정 시간 동안 공격 속도 증가, 자기 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
        else:
            print("{0} : 체력 부족, 스팀팩 사용 안합".format(self.name))

# 지상 공격 유닛: 탱크
class Tank(AttackUnit):
    # 특수 모드(시즈모드): 탱크를 지상에 고정시켜, 더 높은 파워로 공격, 이동 불가
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_developed = False
    
    def set_seize_mode(self):
        # seize 모드가 아애 안만들어져 있을때
        if Tank.seize_developed == False:
            return
        
        # seize 모드가 만들어져 있을때
        # 1. 현재 시드모드가 아닐떄 -> 시즈모드로 바꿔줌
        if self.seize_developed == False:
            print("{0}: 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_developed == True

        # 2. 현재 시즈모드 일때 -> 시즈모드 해제
        if self.seize_developed == True:
            print("{0}: 시즈모드를 해제.".format(self.name))
            self.damage /=2
            self.seize_developed == False


#######################
# 공중 공격 유닛: 날 수 있음
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 공중 공격 유닛: 공격(AttackUnit) + 날 수 있는(Flyable) 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):      
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) ## speed 0으로 받음
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 공중 공격 유닛: 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #처음 만들어질땐 클로킹 모드 아님 ( 해제 상태 )

    def clocking(self):
        if self.clocked == True: #클로킹 모드 -> 모드 해제
            print("{0}: 클로킹 모드 해제합니다.".format(self.name))
            self.clocked == False
        else:
            print("{0}: 클로킹 모드 설정합니다.".format(self.name))
            self.clocked == True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player: gg")
    print("[Player] 님이 게임에서 퇴장하였습니다")


# 1. 실제 게임 시작
game_start()

# 2.
#마린 3개 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
#탱크 2개
t1 = Tank()
t2 = Tank()
#레이스 1개
w1 = Wraith()

#유닛 일괄 관리
attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

# 3.
#전군 이동
for unit in attack_unit:
    unit.move("1시")

# 4. 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발 완료")
#공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스:클로킹)
for unit in attack_unit:
    if isinstance(unit, Marine): # if 현재 unit이 미란이면 스팀팩
        unit.stimpack()
    if isinstance(unit, Tank):
        unit.set_seize_mode()
    if isinstance(unit, Wraith):
        unit.clocking()

# 5.전군 공격
for unit in attack_unit:
    unit.attack("1시")


# 6.전군 피해
for unit in attack_unit:
    unit.damaged(randint(5, 21)) #공격 랜덤으로 받음


#게임 종료
game_over()
