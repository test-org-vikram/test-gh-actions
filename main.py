import os

TOKEN = os.environ.get("SONAR_AUTH_TOKEN")

# Print the value or handle if it's not set
if TOKEN:
    print(f"TOKEN: {TOKEN}")
else:
    print("TOKEN not set.")
