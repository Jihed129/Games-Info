import requests as rq

baseURL = "https://api.rawg.io/api/"
APIkey = "38040185dd0a4473988f8265ee72a189"

def get_game_info(gameName: str):
    # search for a game and return the first result
    url = f"{baseURL}games"
    params = {
        "key" :APIkey,
        "search" : gameName,
        "page_size": 1, # gets the first match 
    }
    response = rq.get(url, params=params)

#    Debug: see the exact URL being called
#    print("Requested URL:", response.url)
#    print("Status code:", response.status_code)

#    if response.status_code != 200:
#        print("Error:", response.status_code, response.text)
#        return None
    
    
    data = response.json()

    results = data.get("results", [])
    if not results:
        return None
    return results[0]  # first game


def print_game_info(game: dict):
    """Nicely print information about a game dict from RAWG."""
    name = game.get("name", "Unknown")
    released = game.get("released", "Unknown")
    rating = game.get("rating", "Unknown")

    # Platforms is a list of objects -> extract platform names
    platforms = [
        p["platform"]["name"]
        for p in game.get("platforms", [])
        if "platform" in p and "name" in p["platform"]
    ]
    platforms_str = ", ".join(platforms) if platforms else "Unknown"

    print(f"Name: {name}")
    print(f"Release date: {released}")
    print(f"Rating: {rating}")
    print(f"Platforms: {platforms_str}")


def main():
    game_name = input("Enter game name: ")
    game = get_game_info(game_name)

    if game is None:
        print("No game found with that name.")
        return

    print_game_info(game)


if __name__ == "__main__":
    main()




