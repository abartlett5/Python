def main():
    person = input('What is your name?: ')
    print('Hello', person)
    xString = input('Enter a number: ')
    num = ParseToInt(xString)
    while(type(num) is not int):
        print('Stop being an idiot and type a real number. Dumbass.')
        xString = input('Try again, enter a number: ')
        num = ParseToInt(xString)
    x = int(xString)
    n = x
    sum = 0
    for i in range (1,n+1):
        sum = sum + i
    print('The sum of the numbers in this range is', sum)

def ParseToInt(s):
    try:
        return int(s)
    except:
        return None
    
if __name__ == "__main__":
    main()


   


