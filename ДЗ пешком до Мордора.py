import numpy as np

def cal_euclidean(array_a: np.ndarray, array_b: np.ndarray):
        distance = np.sqrt(np.sum((a - b) ** 2))
        return distance


def cal_manhattan(array_a: np.ndarray, array_b: np.ndarray):
    distance = np.sum(np.abs(a)-np.abs(b))
    return distance
#
def cal_cosine(array_a: np.ndarray, array_b: np.ndarray):
    distance = np.dot(a, b)/(np.linalg.norm(a) * np.linalg.norm(b))
    return distance

a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))