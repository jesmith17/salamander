import os
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Example of accessing an environment variable
    example_var = os.getenv("EXAMPLE_VAR", "Default Value if not set")
    print(f"EXAMPLE_VAR is set to: {example_var}")

if __name__ == "__main__":
    main()
