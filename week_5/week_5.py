import json

# with open('Documents/workspace/Pratt664/week_5/Artworks.json') as json_file:
   # nation_json = json.load(json_file)
   # for nation in nation_json:
    #    print(nation['Nationality'])

res = {}

with open('Documents/workspace/Pratt664/week_5/Artworks.json') as json_file:
    nation_file = json.load(json_file)
    for artist_nation in nation_file:
       nationality = nation_file.get('Nationality'['Unknown'])
       
       
       if artist_nation['Nationality'] is None:
        res.append(artist_nation)
        print(artist_nation)

with open('res.json', 'w') as outfile:
    json.dump(res, outfile)
    








   