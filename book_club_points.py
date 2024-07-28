books = int(input('Hi, Enter the number of book that you have purchased '))

if books == 0 :
     print("you should parches at lest one book ")
elif books == 2 :
     print(" you will get  5 points, nice keep going ")
elif books == 4 :
    print("you will get the 10 points, keep going ")
elif books == 6 :
    print('you will get the 15 points, keep going')
elif books >= 8 :
    print("you will get 30 points, keep going")
else:
    print('  zyou should buy minimum one book')