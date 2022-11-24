def multi(x,z):
    n=0
    if(x >= 0):
        if(z >= 0):
            for i in range(x):
                n+=z
            return n
        else:
            for i in range(x):
                n-=z
            return n
    else:
        if(z >= 0):
            for i in range(-x):
                n+=z
            return n
        else:
            for i in range(-x):
                n-=z
            return n