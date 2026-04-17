import json

try:
    with open("config.json", "r") as file:
        config = json.load(file)
    print("System Ready.")

except FileNotFoundError:
    print("config.json not found. Creating default config file.")

    default_config = {
        "theme": "light",
        "volume": 50,
        "language": "en"
    }

    with open("config.json", "w") as file:
        json.dump(default_config, file, indent=4)

    print("Default config file created.") 