from unittest.case import _AssertRaisesContext


def test():
    # Empty string
    assert(add("") == 0),"Empty String doesn't return 0"

    # 1 Number
    assert(add("1") == 1)," String \"1\" doesn't return 1"
    assert(add("2") == 2)," String \"2\" doesn't return 2"

    # 2 Number
    assert(add("1,2") == 3)," String \"1,2\" doesn't return 3"
    assert(add("2,3") == 5)," String \"2,3\" doesn't return 5"

    # 3 Number
    assert(add("1,2,3") == 6)," String \"1,2,3\" doesn't return 6"
    assert(add("2,3,5") == 10)," String \"2,3,5\" doesn't return 10"

    # 4 Number
    assert(add("1,2,3,4") == 10)," String \"1,2,3,4\" doesn't return 10"
    assert(add("2,3,5,10") == 20)," String \"2,3,5,10\" doesn't return 20"

    # with Alphabet and Number
    assert(add("1,a") == 2)," String \"1,a\" doesn't return 2"
    assert(add("2,b,c") == 7)," String \"2,b,c\" doesn't return 7"
    assert(add("1,2,a,c") == 7)," String \"1,2,a,c\" doesn't return 7"

    # # value greater than 1000
    # assert(add("1,a,1001") == 2)," String \"1,a,1001\" doesn't return 2"
    # assert(add("2,1000") == 2)," String \"2,1000\" doesn't return 2"

    # # with negative Number
    # _AssertRaisesContext(add("-1,2") == 10)," String \"1,2,3,4\" doesn't return 10"
    # assert(add("-2,3,-5,10") == 20)," String \"2,3,5,10\" doesn't return 20"

    print("PASSED ALL CASES")

def add(numberString):
    if(len(numberString) == 0):
        return 0
    elif (len(numberString) == 1):
        return int(numberString)
    else:
        l = [0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        result = 0
        nums = numberString.split(",")
        
        # for num in nums:
        #     if int(num) < 0:
        #         raise Exception("Negatives not allowed",num)
        #         continue

        for num in nums:
            # if int(num) > 1000:
            #     result += 0
            if num in l:
                result += int(l.index(num))
            else:
                result += int(num)
        
        return result






test()

