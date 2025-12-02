import requests
import base64

# ==========================================
# TASK 8.1: Basic Fetch (Dog API)
# ==========================================
def fetch_random_dog():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Dog Image: {data['message']}")
    else:
        print("Failed to fetch dog.")

# ==========================================
# TASK 8.2: PokeAPI Wrapper
# ==========================================
def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data['name'],
            "id": data['id'],
            "hp": data['stats'][0]['base_stat'], # HP is usually first
            "type": data['types'][0]['type']['name']
        }
    return None

# ==========================================
# TASK 8.3: Spotify Auth (Conceptual)
# ==========================================
def get_spotify_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    
    # Encode credentials
    creds = f"{client_id}:{client_secret}"
    b64_creds = base64.b64encode(creds.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {b64_creds}"
    }
    data = {
        "grant_type": "client_credentials"
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Auth Failed:", response.text)
        return None

if __name__ == "__main__":
    # fetch_random_dog()
    
    poke_data = get_pokemon_data("pikachu")
    if poke_data:
        print("Pokemon Data:", poke_data)
