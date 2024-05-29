# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
# 🚨 Remember to remove the print statement above when you submit.

names = names_string.split(", ")

import random
num_names = len(names)
random_num = random.randint(0, num_names - 1)
print(f"{names[random_num]} is going to buy the meal today!")