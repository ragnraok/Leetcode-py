def removeElement(self, A, elem):
    B = []
    for i in A:
        if i != elem:
            B.append(i)
    A = B
    return len(B)
