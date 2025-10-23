import time

currentTime = time.localtime()

formatedTime = time.asctime(currentTime)
formatedTime2 = time.strftime("%A, %B, %d %H:%M:%S %p", currentTime)
print(formatedTime)
print(formatedTime2)
