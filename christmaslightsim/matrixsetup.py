num_lights = 10

bar_length = 5

step = 1

for i in range(0,num_lights,2):
    print(i)
    step = [1 if x < (bar_length + i) and x >= i else 0 for x in range(num_lights)]
    print(step)