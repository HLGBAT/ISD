
def bsearch(array, key):
    MIN = 0
    MAX = len(array)-1
    MID = (MIN+MAX)//2
    if key == array[MID]:
        return MID
    if MIN > MAX:
        return False
    while key == array[MID]:
        if key < array[MID]:
            MAX == MID
            MID = (MIN + MAX)//2
        elif key > array[MID]:
                MIN = MID
                MID = (MIN + MAX)//2
        else:
            break
    print(MID)
    return(array,key)

print('Please input your numbers:')
numbers = input()
b = [int(number) for number in numbers.split(' ')]
print(b)
array = sorted(b)
print(array)
print('Please input your key:')
key = input()
position = bsearch(array, key)
print(format(position))
