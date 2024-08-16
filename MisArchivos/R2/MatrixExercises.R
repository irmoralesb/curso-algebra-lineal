library(matlib)
#install.packages("pracma")
#library("pracma")

A = rbind(c(1,2,0,-3),
          c(3,-1,-7,-9),
          c(-1,2,4,3))

B = cbind(c(3,2,1))

Solve(A,B)