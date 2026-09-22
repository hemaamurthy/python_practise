#combine separate keys and values into one dictionary, use zip():

keys = ["a", "b", "c"]
values = [1, 2, 3]

d = dict(zip(keys, values))

print(d)