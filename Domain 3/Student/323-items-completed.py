item_list = [["Rock", "Pogo Stick"], ["Wand", "Pogo Stick"], ["Wand", "Rock", "Pogo Stick"]]

for i in range(len(item_list)):
    for item in item_list[i]:
        print(f"You can get a {item} at level {i + 1}.")