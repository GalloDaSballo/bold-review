SHARES = 1e18
DEBT = 1e18

multiplier = 2000e18

DEBT *= multiplier

## PPFS is raised

## V1 lastGoodPrice
price = 2610548359850000000000

MAX_COLL = 120362414e18

def get_deposit_result(debtIncrease):
  return SHARES * debtIncrease // DEBT

def main():
  print("debt", DEBT)
  print("2000e18", get_deposit_result(2000e18))
  print("2e18", get_deposit_result(2e18))




main()