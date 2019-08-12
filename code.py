fibnum = [-1,0, 1]
usernum = input("Which Fibonacci number do you want?\nExample:To get the third Fibonacci number type \"3\" \n ")
while 1 is 1:
    if int(usernum) is int.__pos__(int(usernum)):
        for x in range(0, int(usernum), 1):
            fibnum.append(int(fibnum[-1] + fibnum[-2]))
    #elif int(usernum) is int.__neg__(int(usernum)):
     #   for x in range(0, (int.abs(usernum), 1):
      #      fibnum.reverse(fibnum.append(int(fibnum[-1] + fibnum[-2])))
    print(fibnum[-1])
    fibnum = [-1, 0, 1]
    usernum = input("Which Fibonacci number do you want?\nExample:To get the third Fibonacci number type \"3\" \n ")
