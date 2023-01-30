def moyenne(note):
    H,B=0,0
    for i in range(len(note)):
        N = note[i][0]
        C = note[i][1]


        H = (N*C)+H
        B += C

    return H/B

#moyenne([(15,2),(9,1),(12,3)])