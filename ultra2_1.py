import RPi.GPIO as GPIO
import time

import urllib.request
import requests
import json
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig = 16
echo = 20


def chDistance(distance):
    count = 0
    if distance < 5:
        count = 11
    elif distance < 10:
        count = 10
    elif distance < 15:
        count = 9
    elif distance < 20:
        count = 8
    elif distance < 25:
        count = 7
    elif distance < 30:
        count = 6
    elif distance < 35:
        count = 5
    elif distance < 40:
        count = 4
    elif distance < 45:
        count = 3
    elif distance < 50:
        count = 2
    else:
        count = 1
    data_en = {'pro_name':'GEORGIA', 'pro_count':count}
    data_par = json.dumps(data_en).encode("utf-8")
    request_makeattendence = urllib.request.Request("http://220.67.124.128:8080/product/update_product",data = data_par , method='PUT', headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(request_makeattendence)


GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

try:
    while True:
        GPIO.output(trig, False) # trig핀 low로 유지
        time.sleep(0.5)

          ## trig핀 high로 만들어서 초음파 보냄. 10ms동안 유지
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echo) == False: # echo핀 low일 때 시간 출력
            pulse_start = time.time()

        while GPIO.input(echo) == True: # echo핀 high일 때 시간 출력
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start # high로 유지한 시간 (거리)
        distance = pulse_duration * 17000
        distance = round(distance, 2)
          ##소수점 둘째자리까지

        print("Distance : ", distance, "cm")
        chDistance(distance)

except Exception as e:
    print(e)
    GPIO.cleanup()