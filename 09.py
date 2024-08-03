import timeit
import find_utils as fu


if __name__ == '__main__':

    cases = [([50, 25, 10, 5, 2, 1], 113),
             ([50, 25, 10, 5, 2, 1], 42),
             ([10, 6, 1], 12),
            ([50, 25, 10, 5, 2, 1], 54321)]
    functions = [fu.find_coins_greedy, fu.find_min_coins]

    for coins, cash_amount in cases:
        print(f"\n\tCase for {coins} and sum: {cash_amount}")
        for fun in functions:
            time = timeit.timeit(lambda: fun(cash_amount, coins), number=1000)
            print("Result for {}: {}".format(fun.__name__, fun(cash_amount, coins)))
            print("Time taken for {}: {:.6f} seconds".format(fun.__name__, time))
