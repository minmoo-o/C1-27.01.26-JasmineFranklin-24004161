words = ["comfortable", "round", "support", "machinery"]

combinations = []

for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            combinations.append(words[i] + " " + words[j])

print(combinations)
