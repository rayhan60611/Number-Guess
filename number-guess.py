
def numberGuess(n):
    k=True
    global j
    j = n
    while(k):
        if j % 9 == 0:
            k=False
        else:
            j = j + 1



def numberInput():
    num2 = input("Please Give Final Number: ")
    if num2 == 'e' or num2 == 'E' or not num2.isnumeric() :
        print("Thank You For Playing & See You soon")
        exit() 
    else:
        list_num2=[]
        for i in range(len(num2)):
            list_num2.append(int(num2[i]))
        num2_sum = sum(list_num2)
        return num2_sum



while(True):
    n = numberInput()
    numberGuess(n)
    result = j-n
    if n % 9 == 0:
        print(f"Your Missing Number Will be Either 0 Or 9")
    else:
        print(f"Your Missing Number is {result}")
