import random
# l = list() # bu faqat bita argument qabul qiladi
# l = [] # istalgancha lementlarr vergul orqali korsatiadi
# print(len(l))

arr = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
for i in arr:
    print(i)

# arr[0] = 0 # element ozgartirish
# print(arr)

# # print(arr[0]) # 1-elment
# # print(arr[-1]) # oxirgi elemnt
# # print(arr[len(arr)-1])

# arr.append(0)
# print(arr)

# # RANDOM
# print(random.choice("abc")) # 1 ta tasodifiy element qaytaradi
# print(random.shuffle(arr)) # array ni chalkashtiradi 
# print(random.sample(arr, 2)) #siz ko'rsatgan ketma-ketlikda siz korsatgan elemntni random qilib  oladi
# print(random.randint(1, 10)) # sonlar orasida bitta butun random son qaytaradi
# print(random.randrange(10, 100, 2))

# task 1
# print(random.sample(arr, 5))

# task 2
# print(random.sample(arr, 3))
# if arr < 7:
#     print("7 dan kichik")

# task 3
# print(random.shuffle(arr))
# if arr < 5:
#     print("katta")
# else:
#     print("katta")

# task 4
# random20 =  random.sample(arr, 20)
# if random20 <= 99:
#     print(random20 ** 2)
# else:
#     print(random20 ** 3)

# task 5
# def diapazon(x,y):

# task 6
num = int(input("3-ta son kiriting: "))


