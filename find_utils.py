def find_coins_greedy(sum, coins):
    coins_count = {}
    
    for coin in coins:
        count = sum // coin
        if count > 0:
            coins_count[coin] = count
        sum -= coin * count

    return coins_count


def find_min_coins(sum, coins):
    min_coins_required = [0] + [float('inf')] * sum
    coin_used = [0] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin

    coins_count = {}
    current_sum = sum

    while current_sum > 0:
        coin = coin_used[current_sum]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_sum -= coin

    coins_count_ordered = {coin: coins_count.get(coin, 0) for coin in coins if coin in coins_count}

    return coins_count_ordered


if __name__ == '__main__':
    pass
