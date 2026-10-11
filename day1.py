# Set 1: Two Sum

# Base problem: The Shopping Budget
# Riya has ₹900 in her gift card and wants to buy exactly two items that use up the full amount. Given the list of item prices, return the positions of the two items she should buy.

# Input: prices = [200, 700, 450, 300], budget = 900 → Output: [0, 1] (200 + 700)

prices = [200, 700, 450, 300]
budget = 900

for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        if prices[i] + prices[j] == budget:
            print("[", i, ",", j, "]","(",prices[i], "+",prices[j],")")

# Variant 1: The Gift Combos
# The shop owner wants to show Riya all the pairs of items that add up to exactly ₹900, not just the first one.

# Input: [200, 700, 450, 300, 600, 450], budget = 900 → Output: (200,700), (300,600), (450,450)
# Hint: the same pair shouldn’t be printed twice.
a=[200, 700, 450, 300, 600, 450]
b=900

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == b:
            print("(", a[i], ",", a[j], ")")


# Variant 2: The Price Gap
# A shopkeeper wants to put two products side by side where the price difference is exactly ₹500. Find such a pair.

# Input: [150, 650, 300, 800], gap = 500 → Output: (150, 650) or (300, 800)
# Same pattern, but with subtraction.

b=[150, 650, 300, 800]
c=500
for i in range(len(b)):
    for j in range(i+1, len(b)):
        if b[i] - b[j] == c:
            print("(", b[i], ",", b[j], ")")


