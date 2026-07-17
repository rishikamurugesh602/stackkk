target = int(input())

position = list(map(int, input().split()))
speed = list(map(int, input().split()))

def carFleet(target, position, speed):
    cars = list(zip(position, speed))
    cars.sort(reverse=True)          # Sort by position (closest to target first)

    stack = []

    for pos, spd in cars:
        time = (target - pos) / spd
        stack.append(time)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

print(carFleet(target, position, speed))
