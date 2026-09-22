counts = {'cat': 3, 'dog': 2, 'bird': 1}
best_word = None
best_count = 0 
for word,count in counts.items():
    if count>best_count:
        best_word = word
        best_count = count
print(best_word)