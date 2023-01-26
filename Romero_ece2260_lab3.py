import numpy as np

def det_2x2(A):
    detA = (A[0,0]*A[1,1])-(A[0,1]*A[1,0])
    return detA
def det_3x3(A):
    A1 = np.array([[A[1,1],A[1,2]],[A[2,1],A[2,2]]])
    A2 = np.array([[A[1,0],A[1,2]],[A[2,0],A[2,2]]])
    A3 = np.array([[A[1,0],A[1,1]],[A[2,0],A[2,1]]])
    detA = A[0,0]*det_2x2(A1) - A[0,1]*det_2x2(A2) + A[0,2]*det_2x2(A3)
    return detA
def cramer_2x2(A,b):
    Xt = np.array([[b[0],A[0,1]],[b[1],A[1,1]]])
    Yt = np.array([[A[0,0],b[0]],[A[1,0],b[1]]])
    xx = det_2x2(Xt)/det_2x2(A)
    yy = det_2x2(Yt)/det_2x2(A)
    x = np.array([[xx],[yy]])
    return x
def cramer_3x3(A,b):
    Xt = np.copy(A)
    Yt = np.copy(A)
    Zt = np.copy(A)
    Xt[0,0] = b[0]; Xt[1,0] = b[1]; Xt[2,0] = b[2]
    Yt[0,1] = b[0]; Yt[1,1] = b[1]; Yt[2,1] = b[2]
    Zt[0,2] = b[0]; Zt[1,2] = b[1]; Zt[2,2] = b[2]
    xx = (det_3x3(Xt))/(det_3x3(A))
    yy = det_3x3(Yt)/det_3x3(A)
    zz = det_3x3(Zt)/det_3x3(A)
    x = np.array([[xx],[yy],[zz]])
    return x
def main():
    A = np.array([[1,2,3],[3,1,-3],[-3,4,7]])
    b = np.array([-5,4,-7])
    print(cramer_3x3(A,b))

if __name__=="__main__":
    main()