import subprocess
command = ""
while command != "exit":
    try:
        command = input("Enter a command to run: ")
        if command == "exit":
            break
        result = subprocess.run(
            command, capture_output=True, text=True, check=True)
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        print(e.stderr)
    except Exception as e:
        print(f"An unexpected error occured: {str(e)}")
