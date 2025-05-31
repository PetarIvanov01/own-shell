import sys


def exit(*args):
    status = int(args[0])
    sys.exit(status)


def echo(*args):
    echo_str = " ".join(args)
    print(echo_str)


def type(*args):
    command = args[0]
    if command in built_in_commands:
        print(f"{command} is a shell builtin")
    else:
        print(f"{command}: not found")


def command_not_found(command):
    print(f"{command}: command not found")
    return


built_in_commands = {"exit": exit, "echo": echo, "type": type}


def main():

    while True:
        sys.stdout.write("$ ")

        command_input = input()

        command, *args = command_input.split()
        if command not in built_in_commands:
            command_not_found(command)

        else:
            script = built_in_commands[command]
            script(*args)


if __name__ == "__main__":
    main()
