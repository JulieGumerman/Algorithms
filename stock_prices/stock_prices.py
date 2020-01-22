#!/usr/bin/python

import argparse

def find_max_profit(prices):
  cur_min_price = 0
  cur_max_price = 0
  cur_max_profit = 0

  for x in prices:
    if x == 0:
      pass
    elif x > cur_max_price:
      cur_max_price = x
      max_price_index = prices.index(cur_max_price)
      temp_arr = prices[:max_price_index]

      for j in temp_arr:
        if cur_min_price == 0:
          cur_min_price = j
        elif len(temp_arr)==2:
          cur_min_price = temp_arr[0]
          cur_max_price = temp_arr[1]
        elif j < cur_min_price:
          cur_min_price = j
        
  cur_max_profit = cur_max_price - cur_min_price
  return cur_max_profit



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()



  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))