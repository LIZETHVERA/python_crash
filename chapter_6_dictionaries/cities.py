cities= {
    "san diego" : { 
        "country" : "USA",
        "population": "1.307 million",
        "fact": "The top employer in the city is the United States Navy",
        },
    "atlanta" : {
        "country" : "England",
        "population" :"8.8 million",
        "fact": "Over 300 languages are spoken in London",
        },
    "amsterdam" : {
        "country" : "Holland",
        "population" :"1.1 million",
        "fact": "Amsterdam has 165 canals.",
        },
    }
for city, cities_info in cities.items():
    print ("\nCity: " + city.title())
    country = cities_info ["country"]
    population = cities_info ["population"]
    fact = cities_info ["fact"]

    print ("\tcountry: " + country + "\n\tpopulation: " + population + "\n\tfact: " + fact)
    
