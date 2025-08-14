import requests, sys

API_KEY = "YOUR_VT_API_KEY"
VT_URL = "https://www.virustotal.com/api/v3/files/"

def vt_lookup(file_hash):
    headers = {"x-apikey": API_KEY}
    r = requests.get(VT_URL + file_hash, headers=headers)
    if r.status_code == 200:
        data = r.json()
        print(data)
    else:
        print(f"Error: {r.status_code} - {r.text}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file_hash>")
        sys.exit(1)
    vt_lookup(sys.argv[1])
