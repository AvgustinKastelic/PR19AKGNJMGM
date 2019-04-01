import urllib.request, json

# funkcija ustvari json datoteko s podanim imenom iz podanega url-ja
def get_data(url, name):
    data = json.loads(urllib.request.urlopen(url).read().decode())
    file = open(name, "w")
    json.dump(data, file)
    file.close()