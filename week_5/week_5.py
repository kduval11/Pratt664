import os
import json

with open("Artworks.json", "r") as artworksfile:
    data = json.load(artworksfile)

nationalityfiles = {}

for nation in data:
    nationality_list = nation.get("Nationality", ["Unknown"])
    if nationality_list:  
        nationality = nationality_list[0]  
    else:
        nationality = "Unknown"  
    if nationality not in nationalityfiles:
        nationalityfiles[nationality] = []
    nationalityfiles[nationality].append(nation)

output_folder = "res"


for nationality, entries in nationalityfiles.items():
    filename = os.path.join(output_folder, f"{nationality}.json")
    with open(filename, "w") as file:
        json.dump(entries, file, indent=2)

print(f"Split into separate JSON files based on the 'Nationality' key and saved in the '{output_folder}' folder.")

