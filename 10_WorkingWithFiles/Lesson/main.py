# ninja_file = open("text.txt", "r")
# contents = ninja_file.read()
# print(contents)
# ninja_file.close()

with open("text.txt", "r") as ninja_file:
    contents = ninja_file.read().splitlines()
    print(contents)

    for line in contents:
        print(line)

with open("ninja2.txt", "w") as ninja_file_2:
    ninja_file_2.write("Hello, new file!")

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score: " + str(best_score))
