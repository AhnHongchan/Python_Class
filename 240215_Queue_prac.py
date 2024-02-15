N = 10
q = [0] * 10
front = rear = -1

while rear <= 1:
    rear += 1
    q[rear] = 10 * (rear + 1)

while front != rear:
    front += 1
    print(q[front])