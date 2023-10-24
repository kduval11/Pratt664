import csv 

nation_file = {}

with open('Artworks.csv', 'r') as artwork_file:
    processed_csv = csv.DictReader(artwork_file)
    for art in processed_csv:
        artist_nationality = art['Nationality'].split(" ")
        for nationality in artist_nationality:
            if nation_file.get(nationality) is None:
                with open(f"Documents/workspace/Pratt664/week_4/res/{nationality}.csv", "w") as nationality_file:
                    nat_dict_writer = csv.DictWriter(nationality_file, processed_csv.fieldnames)
                    nat_dict_writer.writeheader()
                    nat_dict_writer.writerow(art)
                    nation_file[nationality] = True
            else:
                with open(f"Documents/workspace/Pratt664/week_4/res/{nationality}.csv", "a") as nationality_file:
                    nat_dict_writer = csv.DictWriter(nationality_file, processed_csv.fieldnames)
                    nat_dict_writer.writerow(art)


            nationality_file = open(f"{nationality}.csv", "w")
            nat_dict_writer = csv.DictWriter(nationality_file, processed_csv.fieldnames)

            nation_file[nationality] = {"file": nationality_file, "nat_dict_writer": nat_dict_writer}

