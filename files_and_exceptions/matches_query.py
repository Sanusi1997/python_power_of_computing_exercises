import csv
world_cup_file = open('world_cup_file.csv', 'r')
world_cup_records = csv.reader(world_cup_file)

matches_list = [line[0] for line in world_cup_records]
matches_list.remove(matches_list[0])

matches_dict = {years : matches_list.count(years) for years in matches_list}

print("+" * 50)
print("Year  Number of Matches Played")
print("+" * 50)

for Years, Total_matches in matches_dict.items():
    print("{:<10s} {:<10d}".format(Years, Total_matches))
    print("_" * 50)

print("Total Matches Played ==> {:>10d}".format(len(matches_list)))


world_cup_file.close()