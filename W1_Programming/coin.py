def find_change(coins = [1,5,10,25], val = 92):
    '''
    Input: list of coin denominations, int value to make change
    Output: int smallest number of coins needed to make change
    '''
    coins = sorted(coins, reverse = True)
    number = 0

    for c in coins:
        n = val // c
        number += n
        val -= c*n
    return number

if __name__ == '__main__':
    print(find_change())
