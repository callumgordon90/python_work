cities = {
    "Paris": {
        "country": "France",
        "population_millions": 11,
        "language": "French",
        "continent": "Europe"
    },
    "Tokyo": {
        "country": "Japan",
        "population_millions": 37,
        "language": "Japanese",
        "continent": "Asia"
    },
    "Cairo": {
        "country": "Egypt",
        "population_millions": 20,
        "language": "Arabic",
        "continent": "Africa"
    },
    "New York": {
        "country": "USA",
        "population_millions": 19,
        "language": "English",
        "continent": "North America"
    },
    "Sydney": {
        "country": "Australia",
        "population_millions": 5,
        "language": "English",
        "continent": "Australia"
    }
}

for city, info in cities.items():
    print(city,info['country'])