#!/bin/python3
#https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0]) #7

m = int(first_multiple_input[1]) #3

matrix = []
matrix_list = []
words = []
phrase = ""

for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

    matrix_2 = []
    for j in range(m):
        matrix_2.append(matrix_item[j])
    matrix_list.append(matrix_2)

for column in range(m):
    for row in range(n):
        matrix_char = matrix_list[row][column]
        phrase += matrix_char

result = re.sub(r'(?<=\w)([^A-Za-z]+)(?=\w)', ' ', phrase)
