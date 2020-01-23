#!/usr/bin/python

import sys
import itertools

def rock_paper_scissors(n):
  rps = ['rock', 'paper', 'scissors']
  rpsn = rps * n
  combinations = []

  if n == 0:
    return [[]]
  elif n == 1:
    for x in rpsn:
      new = [x]
      combinations.append(new)
  elif n == 2:
    for x in rpsn:
      for y in rpsn:
        new = [x, y]
        combinations.append(new)
  elif n == 3:
    for x in rpsn:
      for y in rpsn:
        for z in rpsn:
          new = [x, y, z]
          combinations.append(new)
  return combinations

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')