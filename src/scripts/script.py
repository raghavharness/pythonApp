import subprocess

def main():
    try:
        subprocess.run(["./scripts/my_script.sh"], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to run the script.")
        exit(1)

if __name__ == "__main__":
    main()
