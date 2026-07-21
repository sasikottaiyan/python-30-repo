# def reversing(n):
#     total=""
#     for i in str(n):
#         total=i+total
#     convert=int(total)
#     return convert
# print(reversing(200))


def EvenDiv(n):
    count=0
    for i in str(n):
        if i !=0 and n%i==0:
            count+=i
        return count
print(EvenDiv(12))
