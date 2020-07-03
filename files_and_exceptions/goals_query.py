import csv

world_cup_file = open('world_cup_file.csv', 'r')
world_cup_records = csv.reader(world_cup_file)

goals_in_1930 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1930" in lines]
world_cup_file.seek(0)
goals_in_1934 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1934" in lines]
world_cup_file.seek(0)
goals_in_1938 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1938" in lines]
world_cup_file.seek(0)
goals_in_1942 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1942" in lines]
world_cup_file.seek(0)
goals_in_1946 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1946" in lines]
world_cup_file.seek(0)
goals_in_1950 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1950" in lines]
world_cup_file.seek(0)
goals_in_1954 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1954" in lines]
world_cup_file.seek(0)
goals_in_1958 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1958" in lines]
world_cup_file.seek(0)
goals_in_1962 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1962" in lines]
world_cup_file.seek(0)
goals_in_1966 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1966" in lines]
world_cup_file.seek(0)
goals_in_1970 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1970" in lines]
world_cup_file.seek(0)
goals_in_1974 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1974" in lines]
world_cup_file.seek(0)
goals_in_1978 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1978" in lines]
world_cup_file.seek(0)
goals_in_1982 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1982" in lines]
world_cup_file.seek(0)
goals_in_1986 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1986" in lines]
world_cup_file.seek(0)
goals_in_1990 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1990" in lines]
world_cup_file.seek(0)
goals_in_1994 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1994" in lines]
world_cup_file.seek(0)
goals_in_1998 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "1998" in lines]
world_cup_file.seek(0)
goals_in_2002 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "2002" in lines]
world_cup_file.seek(0)
goals_in_2006 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "2006" in lines]
world_cup_file.seek(0)
goals_in_2010 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "2010" in lines]
world_cup_file.seek(0)
goals_in_2014 = [[int(lines[7]), int(lines[8])] for lines in world_cup_records if "2014" in lines]
world_cup_file.seek(0)

def sum_goal(a, b):
    total = 0
    for groups in a:
        for value in groups:
            total += value
    b.append(total)
    return b


year_set = {years[0] for years in world_cup_records}
year_list = list(year_set)
year_list.sort()
year_list.pop()
goals_list = list()
sum_goal(goals_in_1930,goals_list)
sum_goal(goals_in_1934, goals_list)
sum_goal(goals_in_1938,goals_list)
sum_goal(goals_in_1942, goals_list)
sum_goal(goals_in_1946, goals_list)
sum_goal(goals_in_1950, goals_list)
sum_goal(goals_in_1954, goals_list)
sum_goal(goals_in_1958, goals_list)
sum_goal(goals_in_1962, goals_list)
sum_goal(goals_in_1966, goals_list)
sum_goal(goals_in_1970, goals_list)
sum_goal(goals_in_1974, goals_list)
sum_goal(goals_in_1978, goals_list)
sum_goal(goals_in_1982, goals_list)
sum_goal(goals_in_1986, goals_list)
sum_goal(goals_in_1990, goals_list)
sum_goal(goals_in_1994, goals_list)
sum_goal(goals_in_1998,  goals_list)
sum_goal(goals_in_2002, goals_list)
sum_goal(goals_in_2006,goals_list)
sum_goal(goals_in_2010, goals_list)
sum_goal(goals_in_2014, goals_list)

goals_dict = dict(zip(year_list, goals_list))
for key, values in goals_dict.items():
    print("{:<10s} {:>10d}".format(key, values))

print(f"Total Number of goals scored since 1930 ==> {sum(goals_list)}")
world_cup_file.close()
