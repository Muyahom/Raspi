f = open ('PWD.txt', 'w', encoding='utf-8')

a = input("비밀번호를 입력하세요. 숫자 4자리 입력 후 ENTER : ")

f.write(a)
f.close()

