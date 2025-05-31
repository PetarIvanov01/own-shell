import sys
import os


def exit(*args):
    status = int(args[0])
    os._exit(status)


def echo(*args):
    echo_str = " ".join(args)
    print(echo_str)
    return


def type(*args):
    command = args[0]
    if command in built_in_commands:
        print(f"{command} is a shell builtin")
    return


built_in_commands = {"exit": exit, "echo": echo, "type": type}


def main():

    while True:
        sys.stdout.write("$ ")

        command_input = input()

        command, *args = command_input.split()
        if command not in built_in_commands:
            print(f"{command}: command not found")
            return

        script = built_in_commands[command]

        script(*args)


if __name__ == "__main__":
    main()
