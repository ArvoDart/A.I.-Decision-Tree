# A.I.-Decision-Tree
# Author: Sergio Orozco
# Date: February 24 2019
# For: A.I. Project 1
# Language: Python
This file contains the python runner file for the decision tree classifier program as well as sample csv data files

Program Description:
1. This program does very little input verification, therefore it is imperative that file names are correct, else the program 
  will crash.
2. This program can process an unlimited amount of trees,  but will only store them if user chooses the option in the menu
3. The program loads the csv file attributes and targets automatically, so one only needs to type the csv file name
4. The class target data is defined as the last column vector of the csv file
5. In the tree traversal, because parallel arrays are used to traverse the binary tree, the program is forced to ask the user for the same data that they've input before. It has no memory of previous input values
