import requests
import os

# Replace these with your actual credentials
HCP_CLIENT_ID = os.environ.get('HCP_CLIENT_ID')
HCP_CLIENT_SECRET = os.environ.get('HCP_CLIENT_SECRET')
TOKEN_FILE = 'hcp_token.txt'

def get_hcp_token(client_id, client_secret):
    url = "https://auth.idp.hashicorp.com/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "audience": "https://api.hashicorp.cloud"
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        token = response.json().get("access_token")
        print("✅ HCP Token retrieved successfully:")
        print(token)
        with open(TOKEN_FILE, 'w') as f:
            f.write(token)
        print(f"🔐 Token saved to '{TOKEN_FILE}'")
        return token
    else:
        print("❌ Failed to retrieve token:")
        print(response.status_code, response.text)
        return None

# Run the function
get_hcp_token(HCP_CLIENT_ID, HCP_CLIENT_SECRET)
