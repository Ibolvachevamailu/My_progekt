import lessons as np

def cal_euclidean(a: int, b: int):
    i = 10
    a = int(a)
    b = int(b)
    for i in range(a, b):
        distance = ((a - b) ** 2) ** 0.5
        i += 10
    return distance

# def cal_manhattan(a, b):
#     ## Your code here
#     return distance
#
# def cal_cosine(a, b):
#     ## Your code here
#     return distance
a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
# print(cal_manhattan(a, b))
# print(cal_cosine(a, b))