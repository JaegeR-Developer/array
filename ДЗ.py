def filter_strings(arr):
    result = []
    for string in arr:
        if len(string) <= 3:
            result.append(string)
    return result

# Примеры данных для тестирования
array1 = ["Hello", "2", "world", ":-)"]
array2 = ["1234", "1567", "-2", "computer science"]
array3 = ["Russia", "Denmark", "Kazan"]

# Вызов функции для каждого примера
result1 = filter_strings(array1)
result2 = filter_strings(array2)
result3 = filter_strings(array3)

print(result1)
print(result2)
print(result3)