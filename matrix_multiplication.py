#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 09:29:47 2018

@author: rishabhshetty
"""
import numpy as np 


## Getting the size of theoutput matrix 
def get_size(mat_1,mat_2):
    multiplied_matrix = np.zeros((len(mat_1),len(mat_2[0])))
    return(multiplied_matrix)    
    

    
## Multiplying the matrix
def matrix_multi(matrix_1,matrix_2):
    result = get_size(matrix_1,matrix_2)
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                try:
                    result[i][j] += matrix_1[i][k] * matrix_2[k][j]
                except IndexError:
                    pass
    return result