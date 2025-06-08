import json

with (open("city.list.json", "r", encoding="utf-8") as file):
    structure = json.load(file)

    #Определить количество городов в файле
    print("количество городов в файле:", len(structure))

    #Создать словарь, где ключ — это код страны, а значение — количество городов
    dict1 = {}
    for city in structure:
        cod = city["country"]
        dict1[cod] = dict1.get(cod, 0) + 1
    print(dict1)

    #Подсчитать количество городов в северном полушарии и в южном.
    northen = 0
    southern = 0
    for el in structure:
        if el["coord"]["lat"] > 0:
            northen += 1
        if el["coord"]["lat"] < 0:
            southern += 1
    print("В северном полушарии:", northen, "В южном полушарии:", southern)

    #Перевести в CSV файл данные по городам (координаты представить в виде строки значений через запятую).
    import csv

    with open('cities.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["id", "Город", "Страна", "Координаты"])
        for el in structure:
            coordinates = f"{el['coord']['lat']}, {el['coord']['lon']}"
            writer.writerow([
                el["id"],
                el["name"],
                el["country"],
                coordinates
            ])


    #Создать другой JSON файл, в который сохранить только города одной выбранной страны.
        country_file = "DE"
        german_cities = list(filter(lambda city: city["country"] == country_file, structure))
        with open('germany.json', 'w', encoding='utf-8') as json_file:
            json.dump(german_cities, json_file)

    #Для каждой страны создать свой файл JSON с данными городов. Лучше создать отдельную папку в PyCharm, и указать путь к новому файлу с этой папкой
        countries = {}
        for el in structure:
            country_code = el["country"]
            if country_code not in countries:
                countries[country_code] = []
            countries[country_code].append(el)
        for country_code, cities in countries.items():
            file_path = f"countries/{country_code}.json"
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(cities, file)

    #Необходимо сформировать geojson файл с координатами городов для одной страны

    chosen_country = "DE"
    features = []
    cities_number = 0
    for el in structure:
        if el["country"] == chosen_country:
            if cities_number >= 100:
                break
            feature = {
                "type": "Feature",
                "id": el["id"],
                "geometry": {
                    "type": "Point",
                    "coordinates": [el["coord"]["lon"], el["coord"]["lat"]],
                },
                "properties": {
                    "iconCaption": el["name"],
                    "marker-color": "#b51eff",
                }
            }
            features.append(feature)
            cities_number += 1
    geo = {
        "type": "FeatureCollection",
        "features": features
    }

    with open("de_cities.geojson", 'w', encoding='utf-8') as file:
        json.dump(geo, file)