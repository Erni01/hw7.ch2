# 7. For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
# Try to use the cascade if-elif-else for it.


def number(x):
    if x >= 1:
        print(1)
    elif x <= -1:
        print(-1)
    else:
        print(0)


number(5)