# Module 2 Practice 4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in numbers:
    if i > 1:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
        else:
            not_prime.append(i)
print('Простые: ', prime)
print('Не простые: ', not_prime)