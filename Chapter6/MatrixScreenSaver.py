import time, sys, random

WIDTH = 70

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if random.random() < 0.02:
                #Restart the stream counter in here
                #The stream lenght is between four or fourteen
                columns[i] = random.randint(4, 14)
                
            if columns[i] == 0:
                print(" ", end="")
            else:
                print(random.choice([0,1]), end="")
                columns[i] -= 1
                
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
