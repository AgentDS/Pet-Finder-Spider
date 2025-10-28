BASIC_URL = "https://www.petfinder.com/search/cats-for-adoption/us/{location}/?age%5B0%5D={age}&breed%5B0%5D={breed}&distance={distance}"

def kitten_query_url(breed='Siamese', age='Baby', location='mi/ann-arbor', distance=100):
    assert age in ['Baby', 'Young', 'Adult', 'Senior'], "Only support age in ['Baby', 'Young', 'Adult', 'Senior']"
    assert breed in ['Abyssinian', 'Siamese'], "Currently only support 'breed' for 'Abyssinian', or 'Siamese'"

    if isinstance(distance, int):
        assert distance > 0
        distance = int(distance // 10 * 10)
        distance_msg = f"({distance} km around)"
    elif isinstance(distance, str):
        assert distance=='Anywhere'
        distance_msg = '(Anywhere around)'
    else:
        raise ValueError(f"'distance' can either be integer or 'Anywhere'")
    
    msg = f"Breed={breed} \t Age={age} \t Location={location} {distance_msg}"

    print(f"Query requirement: {msg}")
    query_url = BASIC_URL.format(breed=breed, age=age, location=location,  distance=distance)
    print(f"Query URL: {query_url}")
    return query_url