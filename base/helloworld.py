from __future__ import annotations

print("Hello World from Python")

# name = input ("What is your name")
# print("Welcome to python " + name)

import sys
import os
import builtins

#type hint with return type (-> int)
def add(num : int) -> int:
    return num + 10

print('-----------------------------------')
print (sys.path)

print('-----------------------------------')
print(sys.api_version)

print('-----------------------------------')
print(dir(os))

print('-----------------------------------')
print(dir(builtins))


print('-----------------------------------')

print(dir(annotations))