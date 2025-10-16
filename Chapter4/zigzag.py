import sys, time

def first_zigzag(maxRange=8):
    indent = 0
    isIncreasing = True

    try:
        while True:
            if isIncreasing:
                print(" " * indent, end="")
                print("*" * maxRange)
                indent += 1
                time.sleep(.5)
                if indent == maxRange:
                    isIncreasing = False
            else:
                print(" " * indent, end= "")
                print("*" * maxRange)
                indent -= 1
                time.sleep(.5)
                if indent <= 0:
                    isIncreasing = True

    except KeyboardInterrupt:
        sys.exit()        


first_zigzag()

