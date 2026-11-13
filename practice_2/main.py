def candies_per_bag(candies, bags):
    if bags == 0:
        return "На ноль делить нельзя"
    else:
        return(candies/bags)

print(candies_per_bag(63,7))
print(candies_per_bag(16,4))
print(candies_per_bag(12,0))

assert candies_per_bag(63,7) == 9                                                     
assert candies_per_bag(16,4) == 4
assert candies_per_bag(12,0) == "На ноль делить нельзя"

words = ["мир", "страна", "континент"]
result = sorted(words, key = lambda w:len(w))
print(result)