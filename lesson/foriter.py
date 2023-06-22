def nested_loop():
    n = 10
    count = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    count += 1

    return count

result = nested_loop()
print(result)

