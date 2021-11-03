def input_matrix():
  '''
  This function will ask for 4 floating point numbers, 
  and will return the corresponding 2x2 matrix in row order form 
  ---
  For example if the user enters the following inputs:
    1.5
    2.0
    -3
    4
  then the function should return (1.5, 2.0, -3.0, 4.0)
  '''
  print("Enter four floating point numbers:")
  ##########################
  ### START OF YOUR CODE ###
  ##########################

 a = float(input('a:'))
 b = float(input('b:'))
 c = float(input('c:'))
 d = float(input('d:'))

 return(a, b, c, d)


  ##########################
  ###  END OF YOUR CODE  ###
  ##########################

def inverse(M):  
  '''
  This function will take a matrix in row order form
  if the determinant is 0, it will warn the user and return None
  otherwise it will return the inverse of the Matrix in row order form
  ---
  For example inverse((1,1,1,1)) will result in an error message: 
  "determinant is 0, inverse does not exist"
  and inverse((1,2,3,4)) will return (-2.0, 1.0, 1.5, -0.5)
  '''
  ##########################
  ### START OF YOUR CODE ###
  ##########################

  a, b, c, d = M
 det_M = d*a - b*c
 if det_M == 0:
  print("Determinant is 0, the inverse does not exist.")
  else: 
    return ( d/det_M, -b/det_M, -c/det_M, a/det_M)

  ##########################
  ###  END OF YOUR CODE  ###
  ##########################

def matmul(M1, M2):
  '''
  This function will take two matrices M1 and M2 in row order form
  and will return M1 multiplied by M2 in row order
  ---
  for example matmul((1,2,3,4), (2,3,4,5)) will return
  (10, 13, 22, 29)
  '''
  ##########################
  ### START OF YOUR CODE ###
  ##########################

  a1, b1, c1, d1 = M1
  a2, b2, c2, d2 = M2

 return(a1*a2+b1*c2, a1*b2+b1*d2, c1*a2+d1*c2, c1*b2+d1*d2)

  ##########################
  ###  END OF YOUR CODE  ###
  ##########################

def almost_identity(M, epsilon):
  '''
  This function will take matrix M in row order form 
  and a small positive number epsilon.
  if the absolute difference between any element of
  matrix M and the corresponding element of the identiy
  matrix is greater than epsilon, print an error message saying:
    "This matrix is not equal to the identiy matrix."
  Otherwise simply print the following message:
    "This matrix is approximately equal to the identiy matrix."
  ---
  for example almost_identiy((1.1, 0, 0, 0.9), 0.01)
  should show the error:
    "This matrix is not equal to the identiy matrix."
  and almost_identity((1.1, 0, 0, 0.9), 0.2) should print:
    "This matrix is approximately equal to the identiy matrix."
  '''
  ##########################
  ### START OF YOUR CODE ###
  ##########################

  '''
  finds the absolute difference between any element of
  matrix M
  '''

 if ( M >= epsilon)
 print("This matrix is not equal to the identiy matrix.") 
 else: 
 return("This matrix is approximately equal to the identiy matrix.")

  ##########################
  ###  END OF YOUR CODE  ###
  ##########################

def main():
  M = input_matrix()
  print("Matrix M in row order form:")
  print(M)
  M_inv = inverse(M)
  print("Inverse of matrix M in row order form")
  print(M_inv)
  identity = matmul(M, M_inv)
  print("Result of multiplying M with its inverse in row order form:")
  print(identity)
  almost_identity(identity, 1e-4)

if __name__ == "__main__":
  main()
