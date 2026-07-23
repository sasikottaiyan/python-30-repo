n=5
# for row in range(1,n+1):
#     for column in range(n):       #square
#         print("#", end="")
#     print()

# for i in range(n):
#     for j in range(n-i):                   #space
#         print(' ',end=" ")

#     for k in range(i+1):
#         print('*',end=' ')                #triangle
#     print()



# for i in range(n):
#     for j in range(i+1):                   #space
#         print(' ',end=" ")

#     for k in range(n-i):
#         print('*',end=' ')                #triangle
#     print()


# for i in range(n):
#     for j in range(i,n):                   #space
#         print(' ',end=" ")

#     for k in range(i+1):
#         print('*',end=' ')   

#     for p in range(i):
#         print('*',end=' ')
#                      #triangle
#     print()

#square====================

# n=5
# for i in range(n):
#     for j in range(n):
#         print('*',end=" ")
#     print()

#increasing triangle=================
# n=5
# for i in range(n):
#     for j in range(i+1):
#           print('*',end=" ")
#     print()

#decreasing triangle===================

# n=5
# for i in range(n):
#     for j in range(i,n):
#           print('*',end=" ")
#     print()

#right triangle========================

# n=5
# for i in range(n):
#     for j in range(n-i):
#           print(' ',end=" ")
#     for k in range(i+1):
#          print('*',end=' ')
#     print()
    
#triangle=============================

# n=5
# for i in range(n):
#     for j in range(n-i):
#           print(' ',end=" ")
#     for k in range(i+1):
#          print('*',end=' ')
#     for p in range(i):
#          print('*',end=' ')
#     print()

#reverse triangle====================

# n=5
# for i in range(n):
#     for j in range(i+1):
#           print(' ',end=" ")
#     for k in range(n-i):
#          print('*',end=' ')
#     for p in range(n-i-1):
#          print('*',end=' ')
#     print()

#diamond=========================

# n=5
# for i in range(n-1):
#     for j in range(n-i):
#           print(' ',end=" ")
#     for k in range(i+1):
#          print('*',end=' ')
#     for p in range(i):
#          print('*',end=' ')
#     print()


# for i in range(n):
#     for j in range(i+1):
#           print(' ',end='')
#     for k in range(n-i-1):
#          print('*',end=' ')
#     for p in range(n-i):
#              print('*',end=' ')
#     print()

#123==========================================

n=5
for i in range(1,n+1):
     for j in range(i):       
         print(i, end="")
     print()
    