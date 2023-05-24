import os

def read_env_var(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        print(f"Error: The environment variable '{var_name}' is not set.")
        exit(1)

def main():
    var_name = "MY_VAR"
    print(read_env_var(var_name))

if __name__ == "__main__":
    main()
