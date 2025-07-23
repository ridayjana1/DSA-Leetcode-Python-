value = "leeetcode"
new_word = ""
count = 1

for i in range(len(value)):
    if i > 0 and value[i] == value[i - 1]:
        count += 1
        print("What does this do: " ,value[i-1])
    else:
        count = 1

    if count < 3:
        new_word += value[i]

print(new_word)  # ➜ "leetcode"
