capitals = ["Moscow", "Washington", "London", "Berlin", "Paris", "Delhi"]
countries = ["Russia", "USA", "UK", "Germany", "France", "India"]
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for capital, country, populat in zip(capitals, countries, population):
    print(f"{capital} is the capital of {country}, population equal {populat} people")