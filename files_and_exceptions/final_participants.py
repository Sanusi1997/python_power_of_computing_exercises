import csv
world_cup_file = open('world_cup_file.csv', 'r')
world_cup_records = csv.reader(world_cup_file)

final_participants = list()
unique_final_participants = set()

for line in world_cup_records:
    if line[3] == "final".title():
        final_participants.append(line[6])
        unique_final_participants.add(line[6])
        final_participants.append(line[9])
        unique_final_participants.add(line[9])
final_participants.sort()

participants_dict ={country:final_participants.count(country)  for country in final_participants}
print("__" * 50)
print("{:<15s} {:>10s}".format("Countries" ," Number of Finals_Played"))
print("__" * 50)

for  countries, finals_played in participants_dict.items():
    print("{:<15s} {:>10d}".format(countries,finals_played))
    print("__" * 50)

def participants():
    country = input("Please enter  country you want to know their status")
    if country.title() in unique_final_participants:
        print("{} is a finalist with {} appearance(s)".format(country.title(),
                         final_participants.count(country.title())))
    else:
        print(f"{country.title()} is not a world cup finalist")
participants()

world_cup_file.close()