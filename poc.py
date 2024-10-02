"""
    The code below demosntrates that:
    - Given a rebased share
    - The maximum amount of debt forgiven for a Trove will be roughly equal to the order of magnitude
        difference between the shares of the Trove and the Shares of the Batch
    
"""
## _latestTroveData.recordedDebt = _latestBatchData.recordedDebt * batchDebtShares / totalDebtShares;

##  batchDebtSharesDelta = currentBatchDebtShares * debtIncrease / _batchDebt;

## Cannot generate a new share

def get_debt(total_debt, trove_shares, total_shares):
    return total_debt * trove_shares // total_shares


## It takes forever for this to work

def main():
    ## We need counter to reach 1e9
    GOAL = 10 ## 10 Million shares at a time

    TOTAL_DEBT = 20003008224108095508850000 * 10000 ## 200 BLN, prob max reasonable we can achieve
    TROVE_SHARES = 1e18 ## 10 e27
    TOTAL_SHARES = 1000150411205404775442000 * 10000

    INIITIAL_DEBT = get_debt(TOTAL_DEBT, TROVE_SHARES, TOTAL_SHARES)
    print("INIITIAL_DEBT", INIITIAL_DEBT/1e18)

    print("Percent ownership", TROVE_SHARES / TOTAL_SHARES * 100)
    print("Reverse Ratio", TOTAL_SHARES / TROVE_SHARES) ## This is the value we get by brute forcing
    ## This is the max amount that can be forgiven per open | close ratio

    ## 1e-10
    
    COUNTER = 0
    while (COUNTER < GOAL):
        COUNTER = loop(TOTAL_DEBT, TOTAL_SHARES, TROVE_SHARES)
        TOTAL_DEBT += COUNTER

    

def loop(TOTAL_DEBT, TOTAL_SHARES, TROVE_SHARES):
    COUNTER = 1

    CURRENT_DEBT = TOTAL_DEBT
    CURRENT_SHARES = TOTAL_SHARES
    MY_SHARES = TROVE_SHARES

    MY_DEBT = get_debt(CURRENT_DEBT, MY_SHARES, CURRENT_SHARES)
    
    while(True):
        COUNTER *= 10
        ## How do you know when it increases the share?
        CURRENT_DEBT += COUNTER

        NEW_DEBT = get_debt(CURRENT_DEBT, MY_SHARES, CURRENT_SHARES)
        if(NEW_DEBT != MY_DEBT):
            break
        
    
    print("COUNTER", COUNTER)

    TOTAL_DEBT += COUNTER


    return COUNTER

main()