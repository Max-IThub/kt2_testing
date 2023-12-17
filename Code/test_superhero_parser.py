from Code import superhero_parser

def test_sort_superheroes_by_age():
    # Test case with provided data
    test_data = {
        "members": [
            {"name": "Hero1", "age": 30},
            {"name": "Hero2", "age": 25},
            {"name": "Hero3", "age": 35},
        ]
    }

    superhero_parser.sort_superheroes_by_age(test_data)
    assert test_data['members'][0]['age'] == 25
    assert test_data['members'][1]['age'] == 30
    assert test_data['members'][2]['age'] == 35
