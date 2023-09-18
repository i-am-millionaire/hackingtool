import requests
import itertools

base_url = "https://google.com/"  # Replace with the target domain
characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
max_length = 3  # You can adjust this for desired subdomain length

def generate_subdomains():
    for length in range(1, max_length + 1):
        for combo in itertools.product(characters, repeat=length):
            yield ''.join(combo)

def check_subdomain(subdomain):
    url = f"{base_url}{subdomain}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"https://{subdomain}.google.com")

if __name__ == "__main__":
    for subdomain in generate_subdomains():
        check_subdomain(subdomain)
