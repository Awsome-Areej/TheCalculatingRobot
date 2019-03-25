def even_number(n):
    number = n
    if number%2==0:
        for a in range(n):
            print "COMPUTING, COMPUTING, "
        print "BEEEEEEEEEEP"
        print "EVEN NUMBER"
    elif number%2==1:
        for a in range(n):
            print "COMPUTING, COMPUTING, "
        print "BEEEEEEEEEEP"
        print "ODD NUMBER"
    else:
        for a in range(n):
            print "COMPUTING, COMPUTING, "
            print "BEEP"
            print "ERROR"
        print "CAN NOT COMPUTE"
