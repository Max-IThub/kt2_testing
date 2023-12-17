import json

def read_superhero_data(file_path):
    with open(file_path, 'r') as file:
        superhero_data = json.load(file)
    return superhero_data

def add_superheroes(superhero_data, new_superheroes):
    superhero_data['members'].extend(new_superheroes)

def sort_superheroes_by_age(superhero_data):
    superhero_data['members'] = sorted(superhero_data['members'], key=lambda x: x['age'])

def save_superhero_data(file_path, superhero_data):
    with open(file_path, 'w') as file:
        json.dump(superhero_data, file, indent=2)

def main():
    superhero_file_path = '../data/SuperHero.json'
    superhero_data = read_superhero_data(superhero_file_path)

    # Add new superheroes
    new_superheroes = [
        {
            "name": "New Hero 1",
            "age": 30,
            "secretIdentity": "Unknown",
            "powers": ["Super Strength", "Flight"]
        },
        {
            "name": "New Hero 2",
            "age": 25,
            "secretIdentity": "Mystery",
            "powers": ["Telekinesis", "Invisibility"]
        }
    ]

    add_superheroes(superhero_data, new_superheroes)

    # Sort superheroes by age
    sort_superheroes_by_age(superhero_data)

    # Save the updated superhero data to a new file
    new_superhero_file_path = '../data/superhero_new.json'
    save_superhero_data(new_superhero_file_path, superhero_data)

if __name__ == "__main__":
    main()
