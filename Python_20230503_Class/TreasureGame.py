print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("보물섬에 오신 것을 환영합니다! 보물을 찾아보세요.")

choice1 = input("당신은 갈림길에 있습니다. 오른쪽(r), 왼쪽(l)을 선택하세요 : ").lower()

if choice1 == "l" :
	choice2 = input("호수를 만났습니다. 기다릴 것인지(w) 수영할 것인지(s) 선택하세요 : ").lower()
   
	if choice2 == "w" :
		choice3 = input("3개의 문 앞에 도착했습니다. 빨간색(r), 노란색(y), 파란색(b) 중 어떤 문을 선택할까요? : ").lower()
   
		if choice3 == "r" :
			print("불구덩이에 빠졌습니다. 게임을 종료합니다.")
		elif choice3 == "y" :
			print("보석을 발견했습니다! 이름을 입력하세요.")
			name = input("이름을 입력하세요 : ")
			print("게임의 우승자는" + name + "입니다!")
		elif choice3 == "b" :
			print("바다에 빠졌습니다. 게임을 종료합니다.")
		else :
			print("게임을 종료합니다.")
	else :
		print("게임을 종료합니다.")
else :
	print("게임을 종료합니다.")