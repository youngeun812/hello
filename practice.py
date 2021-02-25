'''자료형'''
# print(3)
# print(3.14+2)

# print('풍선')
# print("선물"*8)

# #boolean
# print(5>10)
# print(5<10)
# print(False)
# print(not True)
# print(not(5>10))

'''변수''' 
# 애완동물을 소개해 주세요
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age>=3

# print("우리집 " + animal + name)
# print(name + str(age) +"살, 산책을 좋아함") # + str(age)
# print(name, age, "살, 산책을 좋아함")       # , age,
# print(name+ " 어른인가? "+ str(is_adult))

'''퀴즈1'''
# tation = "사당"
# print(station + "행 열차가 들어오고 있습니다")

'''연산자'''
# print(1+1)
# print(6/3)
# print(2**3)  # 2^3
# print(5%3)   # 나머지 2
# print(10//3) # 몫 3
# print(10>3)  # true
# print(4>=7)  # false
# print(3==3)  # true

# print(1!=3)  # true
# print(not (1!=3)) #false

# print((3>0) and (3<5)) #true
# print((3>0) & (3<5))   #true

# print((3>0) or (3>5)) #ture
# print((3>0) | (3>5))  #ture

# print(5>4>3)   #true
# print(5>4>7)   #false

'''수식'''
# print(2+3*4)
# print((2+3)*4)

# number = 2
# number = number+2
# number += 2
# number *= 2
# number /= 2
# number -= 2
# number %=2  #나머지

''''''
'''숫자처리함수'''
# print(abs(-5))      #5
# print(pow(4, 2))    #제곱 4^2
# print(max(5, 12))   #12
# print(min(5, 12))   #5
# print(round(3.14))  #3
# print(round(4.99))  #5

# from math import *      # math library안에 있는 것을 모두 이용하겠다.
# print(floor(4.99))  #내림   4
# print(ceil(3.14))   #올림   4
# print(sqrt(16))     #제곱근  4

'''랜덤함수'''
# from random import *
# print(random())      # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random()*10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random()*45) + 1) # 1 ~ 45 이하의 임의의 값 생성

# print(randrange(1, 46))  # 1 ~ 46 미만의(1-45이하의) 임의의 값 생성

# print(randint(1, 45)) #1~45이하의 임의의 값 생성

'''퀴즈2'''
# from random import *

# ran = randint(4, 28) #ran = randrange(4, 29)
# print("오프라인 스터디 모임 날짜는 매월 " + str(ran) + "일로 선정되었습니다.")


'''문자열'''
# sentence = '나는 소년입니다.'
# print(sentence)

# sentence2 = "파이썬은 쉬워요"
# print(sentence2)

# sentence3 = """
# 나는 소년,
# 파이썬 쉽다.
# """
# print(sentence3)

'''슬라이싱'''
# jumin = "991023-1234567"

# print("성별: " + jumin[7]) #1
# print("연: " + jumin[0:2]) #99, 0부터 2직전까지 (0,1)
# print("월: " + jumin[2:4]) #10

# print("생년월일: " + jumin[:6]) #991023 , 처음부터 6직전까지
# print("뒤 7자리: " + jumin[7:]) #1234567 , 7부터 끝까지

# print("뒤 7자리(뒤에서부터): " + jumin[-7:] ) #1234567, 맨 뒤에서 7번째부터 끝까지

'''문자열 처리함수'''
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())  #true
# print(len(python))  #17
# print(python.replace("Python", "Java"))

# location = python.index("n") # 어디에 있는지 위치 번호 알려줌, index 위치
# print(location)
# location = python.index("n", location+1)
# print(location)

# print(python.find("n"))

# #index vs find 차이점 : 
# print(python.find("Java"))  # -1반환
# # print(python.index("Java")) # error반환

# print(python.count("n"))


'''문자열 포맷'''
# print("a" + "b")
# #방법1 %
# print("나는 %d살입니다." %20) #d는 정수값만 가능
# print("나는 %s을 좋아해요." %"파이썬") #s는 문자열
# print("apple은 %c로 시작해요" %"A") #character
# print("나는 %s을 %s좋아해요." %("파랑", "빨간")) #s는 문자열

# #방법2 {}
# print("나는 {}살입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# #방법3 
# print("나는 {age}살, {color}색을 좋아합니다." .format(age=20, color="빨간"))

# #방법4
# age = 200
# color = "빨간ddd"
# print(f"나는 {age}살, {color}색을 좋아합니다.")

'''탈출문자'''
# print("백문이 불여일견 \n 백견이 불여일타")
# print('저는 "나도코딩"입니다')
# #  \" : 문장 내에서 "
# print("저는 \"나도코딩\"입니다") # \"
# # \\ : 문장 내에서 \
# print("\\Users\\yelee\\Desktop") #\Users\yelee\Desktop 이거 출력하려면 앞에 \붙여야 된다.

# # \r : 커서를 맨 앞으로 이동해서 덮어쓰기
# print("Red Apple\rPine") # PineApple 출력

# # \b : 백스페이스 역할 (한글자 삭제)
# print("Redd\bApple") # RedApple 출력

# # \t : 탭
# print("Red\tApple")

'''퀴즈3'''
'''
ex) http://naver.com
규칙1: http:// 부분은 제외 => naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
            (nav)           (5)             (1)         (!)
ex) 생성된 비밀번호: nav51!
'''
# site = "http://naver.com"
# #규칙1
# my_str = site.replace("http://", "")    #naver.com
# #규칙2
# my_str = my_str[:my_str.index(".")]     #naver
# #규칙3
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

# print("{0}의 생성된 비밀번호는 {1}" .format(site, password))


'''리스트 []'''
# #지하철 칸별로 10, 20, 30명
# subway = [10,20,30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호는 몇번째 칸에?
# print(subway.index("조세호"))

# #하하를 더해라
# subway.append("하하")
# print(subway)

# #정형돈을 유재석, 조세호 사이에 넣어라
# subway.insert(1, "정형돈")
# print(subway)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# #같은 이름의 사람이 몇 명인지 확인
# subway.append("유재석")
# print(subway.count("유재석"))

# #정렬도 가능
# num_list = [5,2,3,1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

# #다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# #리스트 확장
# num_list = [5,2,3,1]
# mix_list = ["조세호", 20, True]
# num_list.extend(mix_list)
# print(num_list)


'''딕셔너리(사전) key:value   {}'''
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])    
# print(cabinet.get(3)) # 위아래 둘다 같음

# # print(cabinet[5])     #keyerror, 값이 없어서 뒤에꺼 출력 못함
# print(cabinet.get(5))   #none, 뒤에꺼 출력
# print(cabinet.get(5, "사용가능"))

# print(3 in cabinet) #True
# print(5 in cabinet) #False

# cabinet = {"A-3":"유재석"}
# print(cabinet["A-3"])

# #새손님 더하기
# cabinet["c-20"] = "조세호"
# print(cabinet)

# #같은 key에 업데이트하기
# cabinet["A-3"] = "김종국"
# print(cabinet)

# #지우기
# del cabinet["A-3"]
# print(cabinet)

# #key들만 출력
# print(cabinet.keys())

# #value들만 출력
# print(cabinet.values())

# #key, value 출력
# print(cabinet.items())

# #다 지우기!
# cabinet.clear()
# print(cabinet)


'''튜플: 리스트처럼 내용 변경, 추가 안됨, 하지만 속도가 빠름'''
# menu = ("돈까스", "치즈까스") #절대 메뉴변경 없을때
# print(menu[0])

# #
# name = "김종국"
# age = "20"
# hobby = "코딩"
# print(name, age, hobby)
# #위 내용 튜플사용해서 쉽게
# (name, age, hobby) = ("김종국", 20, "코딩")


'''집합(set): 중복 안됨, 순서 없음  {}'''
# my_set = {1,2,3,3,3}
# print(my_set) 

# #
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# #교집합(java와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))
# #합집합
# print(java | python)
# print(java.union(python))
# #차집합(java는 할 수 있지만 python을 할 수 없는 개발자)
# print(java - python)
# print(java.difference(python))
# #python할 수 있는 사람 더하기
# python.add("김태호")
# print(python)
# #java에서 지우기
# java.remove("김태호")
# print(java)


'''자료구조의 변경: 리스트[], 딕셔너리{}, 튜플(), 집합{}'''
# menu = {"커피", "우유", "주스"} #set
# print(menu, type(menu)) # {'우유', '주스', '커피'} <class 'set'>

# menu = list(menu) #list로 바꾸기
# print(menu, type(menu)) # ['우유', '주스', '커피'] <class 'list'>

# menu = tuple(menu)  #tuple로 바꾸기
# print(menu, type(menu)) # ('우유', '주스', '커피') <class 'tuple'>

# menu = set(menu)
# print(menu, type(menu))

'''퀴즈4: shuffle, sample, 1:55:00'''
# from random import *

# users = range(1,21) #1~20사이의 사람
# print(type(users)) #type이 range여서
# lst = list(users)  #list로 밖꿔서 출력
# shuffle(lst)       #한번 섞고

# winners = sample(lst,4) #랜덤으로 뽑아 내고

# print("---당첨자 발표---")
# print("치킨 당첨자: {0}" .format(winners[0]))
# print("커피 당첨자: {0}" .format(winners[1:]))
# print("---축하합니다---")


'''if: elif: else:'''
'''input: 사용자 입력 가능'''

# weather = input("오늘 날씨는 어때요?(비,미세,or) ")
# if weather=="비" or weather=="눈":
#     print("우산 필요")
# elif weather=="미세":
#     print("마스크")
# else:
#     print("노 준비물")


# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요!")
# elif 10 <= temp and temp < 30:
#     print("딱 좋아요0~")
# elif 0 <= temp < 10:
#     print("외투 챙겨요~")
# else:
#     print("너무 추워요!")


'''for'''
# for waitingNum in [0,1,2,3,4]:
#     print("대기번호: {0}" .format(waitingNum))

# for waitingNum in range(5):
#     print("대기번호: {0}" .format(waitingNum))

# for waitingNum in range(1,6):
#     print("대기번호: {0}" .format(waitingNum))


# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피준비요.".format(customer))


'''while'''
# customer = "토르"
# index = 5
# while index >=1:
#     print("{0}, 커피 찾아가세요. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index==0:
#         print("커피 폐기됐어요")

# customer2 = "토르"
# person = "unknown"
# while person != customer2:
#     print("{0}, 커피 준비됐어요.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

'''continue / break'''
# absent = [2, 5] #결석
# no_book = [7]   #책을 안가져옴
# for student in range(1,11):
#     if student in absent:
#         continue    #계속 해서 다음 반복
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0} 교무실로 따라와" .format(no_book))
#         break       #여기서 프로그램 끝냄
#     print("{0}, 책을 읽어봐" .format(student))

'''for문 한줄로'''
# #출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101 102 103 104
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)

# #학생 이름을 길이로 변환
# student = ["Iron man", "Thor", "I am groot"]
# student = [len(i) for i in student]
# print(student)

# #학생 이름을 대문자로 변환
# student = ["Iron man", "Thor", "I am groot"]
# student = [i.upper() for i in student]
# print(student)

'''퀴즈5: 2:25:00'''
# from random import *

# count = 0 #총 탑승 승객 수
# for customer in range(1, 51): #1~50이라는 수 (승객)
#     time = randrange(5,51)    #5~50분 소요 시간
#     if 5<=time<=15:           #5~15분 이내의 손님, 탑승 승객 수 증가 처리, 매칭 성공
#         print("[0] {0}번쨰 손님 (소요시간: {1}분)" .format(customer, time))
#         count += 1
#     else:                     #매칭 실패
#         print("[] {0}번쨰 손님 (소요시간: {1}분)" .format(customer, time))

# print("총 탑승 승객: {0}분" .format(count))



'''함수'''
# def open_account(): #함수는 정의만 해놓치, 부르기 전까지는 실행되지 않는다
#     print("새로운 계좌가 생성되었습니다.")
# open_account() #실행하기


# def deposit(balance, money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance+money))
#     return balance+money
# balance = 0 #잔액
# balance = deposit(balance, 1000)
# print(balance)

# def withdraw(balance, money): #출금
#     if balance>=money:
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금안됩니다.")
# balance = withdraw(balance, 500)
# print(balance)

# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100 #수수료
#     return commission, balance-money-commission
# comm, balance = withdraw_night(balance, 100)
# print(comm, balance)


'''기본값 설정'''
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주사용언어: {2}".format(name, age, main_lang))
# profile("유재석", 20, "python")
# profile("김태호", 30, "java")

# 만약 age, main_lang이 같다면
# def profile(name, age=17, main_lang="파이썬"): #바로 값 설정
#     print("이름: {0}\t나이: {1}\t주사용언어: {2}".format(name, age, main_lang))
# profile("유재석")
# profile("김태호")


# '''키워드값'''
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
# profile(name="유재석", main_lang="파이썬", age="20")
# profile(age="20", name="유재석", main_lang="파이썬")


'''가변인자 안쓰면: 번거로움'''
# def profile(name, age, lang1, lang2, lang3, lang4): 
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # end=" "는 줄 바꿈하지 않고 뒤에 이어서 쓰고 싶을때
#     print(lang1, lang2, lang3, lang4)
# profile("유재석", 20, "python", "java", "c", "c++")
# profile("김태호", 20, "python", "java", "", "")

'''가변인자: 가변인자 이렇게 써야 됨'''
# def profile(name, age, *language):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
#     for lan in language:
#         print(lan, end=" ")
#     print()
# profile("유재석", 20, "python", "java", "c", "c++")
# profile("김태호", 20, "python", "java")


'''지역변수:함수내에서만 사용 / 전역변수:프로그램내 어디서든'''
'''ex1:지역변수만 쓸때'''
# gun = 10
# def checkpoint(soldiers):
#     gun = 20
#     gun = gun-soldiers
#     print("함수내 남은 총: {0}".format(gun))

# print("전체 총: {0}".format(gun)) #10
# checkpoint(2)
# print("남은 총: {0}".format(gun)) #10, 변화없음 전역변수 값이 나오니깐


'''ex2:지역변수안의 값을 전역변수로 쓰고 싶을때: global 붙인다!'''
# gun = 10
# def checkpoint(soldiers):
#     global gun  ################
#     gun = gun-soldiers
#     print("함수내 남은 총: {0}".format(gun))

# print("전체 총: {0}".format(gun)) #10
# checkpoint(2)
# print("남은 총: {0}".format(gun)) #8


'''ex3: 보통은 global로 쓰지 않고 return 값으로 사용한다'''
# gun = 10
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("함수내 남은 총: {0}".format(gun))
#     return gun

# print("전체 총: {0}".format(gun)) #10
# gun = checkpoint_ret(gun, 2)
# print("남은 총: {0}".format(gun)) #8


'''퀴즈6: 2:54:00'''
# def std_weight(height, gender):
#     if gender=="남자":
#         return height*height*22
#     else:
#         return height*height*21

# height = 175*0.01
# gender = "남자"
# weight = round(std_weight(height, gender), 2) #소수점 둘쨰짜리까지 표시
# print(weight)



'''표준 입출력'''
# print("python", "java")
# print("python", "java", sep=",") #seperate
# print("python", "java", sep=" vs ")

# print("python", "java", sep=" , ", end ="? ")
# print("이어서 쓰기")

# import sys
# print("python", "java", file=sys.stdout) #표준출력
# print("python", "java", file=sys.stderr) #표준에러, log출력할때 에러 확인 할 떄 사용

# #출력 포맷 {딕셔너리}
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): # .items() -> key, value 가져올때 사용
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #왼쪽 정렬하는데 총 8개의 공간 확보, 오른쪽 정렬하는데 총 4개의 공간 확보

# # 은행 대기 순번표: 001, 002, 003, ....
# for num in range(1, 21):
#     # print("대기번호: " + str(num)) 
#     print("대기번호: " + str(num).zfill(3)) #앞에 0으로 채우기

# # 입력하기
# answer = input("아무 값 입력하시요: ") #사용자로 입력하면 항상 문자열로 입력됨 (숫자도 문자열str로 입력됨)
# print("입력한 값은 " + answer + " 입니다")


'''다양한 출력 포맷: 3:10:12'''
#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보 후 500출력
print("{0: >10}".format(500))

#양수일때는 +로 , 음수일떄는 -로
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

#왼쪽 절렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

#3자리 마다 콤마를 찍어주기
print("{0:,}".format(500000000000))
print("{0:+,}".format(500000000000))
print("{0:+,}".format(-500000000000))

#3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수도 확보, 빈자리를 ^^표시로
print("{0:^<+30,}".format(500000000000))

#소수점 출력
print("{0:f}".format(5/3))

#소수점 특정 자리수 까지만 표시 (소수점 3째 자리애서 반올림)
print("{0:.2f}".format(5/3)) 



'''파일 입출력'''
# 1.쓰기목적의 파일을 하나 만들고
score_file = open("score.txt", "w", encoding="utf8") #txt파일에, w:쓴다, utf8:한글적용
# 2.파일에 쓰고
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
# 3.파일 닫기
score_file.close()