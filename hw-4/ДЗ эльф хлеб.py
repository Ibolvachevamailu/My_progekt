def share_bread(N, K):
    x = K // N
    y = K % N
    print(f'{x}, {y}')
    return x, y

share_bread(3, 14)
