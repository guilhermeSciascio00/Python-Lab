import sys, time

indent = 0
isIncreasing = True
maxRange = 8

try:
    while True:
        if isIncreasing:
            indent += 1
            print(" " * indent, end="")
            print("*" * maxRange)
            time.sleep(20)
            if indent == maxRange:
                isIncreasing = False
        else:
            indent -= 1
            print(" " * indent, end= "")
            print("*" * maxRange)
            if indent <= 0:
                isIncreasing = True

except KeyboardInterrupt:
    sys.exit()        
