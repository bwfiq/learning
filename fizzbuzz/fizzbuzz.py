for n in range(100):
    numberToEvaluate = n + 1
    if numberToEvaluate % 3 == 0:
        if numberToEvaluate % 5 == 0:
            print "FizzBuzz"
        print "Fizz"
    elif numberToEvaluate % 5 == 0:
        print "Buzz"
    else:
        print numberToEvaluate
