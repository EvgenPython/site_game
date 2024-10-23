# *
# **
# ***
# ****
# *****
#

#
# *
# **
# * *
# *  *
# *****

# *****
# *  *
# * *
# **
# *

# 10
 #     *
 #    * *
 #   *   *
 #  *     *
 # *********
# *
# **
# ***
# ****
# *****

# *****
# ****
# ***
# **
# *

# a = int(input("a "))
# for i in range(a):
#     for j in range(0, a-i):
#         print("*", end="")
#     print()


# *
# **
# * *
# *  *
# *****

a = int(input("a "))
for i in range(a):
    for j in range(0, a):
        if j == 0 or i == (a-1) or i==j:
            print('*', end="")
        else:
            print(" ", end='')
    print()