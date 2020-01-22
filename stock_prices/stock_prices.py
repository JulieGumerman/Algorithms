#!/usr/bin/python

import argparse

def find_max_profit(prices):
  cur_min_price = 0
  cur_max_price = 0
  cur_max_profit = 0

  for x in prices:
    if cur_min_price == 0:
      cur_min_price = x
    elif x < cur_min_price :
      cur_min_price = x
    if x > cur_max_price:
      cur_max_price = x
    
  maximum = cur_max_price - cur_min_price
  return maximum



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()



  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))