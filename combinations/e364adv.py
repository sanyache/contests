from math import factorial

# for i in range(ord('a'), ord('z')+1):
#     print(chr(i), end=' ')

def find_word_by_index_optimized(n, k):
    letters = [chr(i) for i in range(97, 97 + n)]  # Перші N латинських літер
    result = []
    k -= 1  # Перетворюємо 1-індексацію в 0-індексацію

    for i in range(n):
        fact = factorial(n - 1 - i)  # Факторіал для поточного рівня
        index = k // fact  # Обчислюємо індекс для поточної літери
        result.append(letters.pop(index))  # Вибираємо літеру
        k %= fact  # Оновлюємо залишок

    return ''.join(result)

n, k = map(int, input().split())
print(find_word_by_index_optimized(n, k))
