Longest Common Subsequence in Python

Given two strings, write a program to determine the longest common subsequence between them. Each string can have a maximum length of 50 characters. Note, this subseqeunce need not be contiguous.

Input:
Your program should read lines of text from standard input. Ignore empty lines. Each non-empty line will contain two semicolon separated strings. You can assume that there is only one unique subsequence per line.

Output:
For each line of input, print to standard output the longest common subsequence. Ensure that there are no trailing spaces on each line you print.

Test 1

Test Input:
XMJYAUZ;MZJAWXU

Expected output:
MJAU


Code Template:
import sys

for line in sys.stdin:
    print(line, end="")