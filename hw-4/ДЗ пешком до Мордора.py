import numpy as np

def cal_euclidean(array_a: np.ndarray, array_b: np.ndarray) -> float:
        distance = np.sqrt(np.sum((array_a - array_b) ** 2))
        return distance


def cal_manhattan(array_a: np.ndarray, array_b: np.ndarray) -> float:
    distance = np.sum(np.abs(array_a - array_b))
    return distance
#
def cal_cosine(array_a: np.ndarray, array_b: np.ndarray) -> float:
    distance = np.dot(array_a, array_b)/(np.linalg.norm(array_a) * np.linalg.norm(array_b))
    return distance

a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))
