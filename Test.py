import RPi.GPIO as GPIO
import time

f = open('PWD.txt', 'r', encoding='utf-8')
line = f.readline()

while True:
	a = input("비밀번호를 입력하세요 : ")
	
	if a in line: 
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		GPIO.setup(17, GPIO.OUT)

		print("Open")
		GPIO.output(17, GPIO.LOW)
		time.sleep(1)

		GPIO.output(17, GPIO.HIGH)
		time.sleep(7)

		print("close")
		GPIO.output(17, GPIO.LOW)
		time.sleep(1)

		GPIO.output(17, GPIO.HIGH)
		time.sleep(7)
		break

	else:
		print("비밀번호가 맞지 않습니다. 다시 입력해주세요.")
