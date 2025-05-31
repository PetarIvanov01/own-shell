import sys


def main():

    # Wait for user input
    while True:
        sys.stdout.write("$ ")

        command = input()

        if command.startswith("exit") and command.endswith("0"):
            sys.exit(0)

        if command.startswith("echo"):
            output = command.split(" ", 1)
            if len(output) > 1:
                print(output)
            else:
                print("")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
