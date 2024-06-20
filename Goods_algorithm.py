
def knapsack(values, weights, capacity):
    if capacity <= 0 or not values or not weights:
        return 0, 0, []

    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    w = capacity
    total_weight = 0
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            total_weight += weights[i - 1]
            w -= weights[i - 1]

    return dp[n][capacity], total_weight, selected_items
