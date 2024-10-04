import sys
import jwt
import json

def main():
    if len(sys.argv) < 2:
        print("Usage: python read_jwt.py <token>")
        return    

    token = sys.argv[1]
    
    try:
        decoded_token = jwt.decode(token, options={"verify_signature": False}, algorithms=["HS256"])
        print(json.dumps(decoded_token, indent=4))

    except jwt.InvalidTokenError:
        print("Invalid token")

if __name__ == "__main__":
    main()

