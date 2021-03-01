while True:
    x = input()
    if x.isnumeric() and int(x) > 2 :
        break
        
x = int(x)

fibonacci = [0, 1]
print(len(fibonacci))

for i in range(x):
    index = len(fibonacci)
    y = fibonacci[index - 1] + fibonacci[index - 2]
    fibonacci.append(y)
    
print(fibonacci)
                    