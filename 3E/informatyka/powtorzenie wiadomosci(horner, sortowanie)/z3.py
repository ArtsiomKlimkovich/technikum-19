def isRosnacy(ciag):
    for i in range(len(ciag)-1):
        if ciag[i] >= ciag[i+1]:
            return False
    return True

ciag = list(map(int, input("input ciag: ").split()))
if isRosnacy(ciag):
    print("tak")
else:
    print("nie")