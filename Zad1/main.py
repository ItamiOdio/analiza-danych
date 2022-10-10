import statistics

def max_min(my_list):
    list_max = max(my_list)
    list_min = min(my_list)
    normalized = []
    for x in my_list:
        y = (x-list_min)/(list_max-list_min)
        normalized.append(y)
    return normalized


def standarization(my_list):
    list_avg = statistics.mean(my_list)
    # print(list_avg)
    list_dev = statistics.pstdev(my_list)
    # print(list_dev)
    standarized = []
    for a in my_list:
        y = (a-list_avg)/list_dev
        # print(y)
        standarized.append(y)

    return standarized

arr = [49.50, 47.85, 45.43, 44.82, 47.21, 53.00, 47.95, 54.99, 64.78, 68.83, 69.19, 70.89, 77.97, 67.15, 59.84]
arr2 = [195, 173, 194, 172, 179, 186]
norm1 = max_min(arr)
norm2 = max_min(arr2)
stand = standarization(arr)
stand2 = standarization(arr2)


# Max/min
print(norm1)
print(norm2)
print()

# Standaryzacja
print(stand)
print(stand2)

