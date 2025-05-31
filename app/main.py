import sys
import os
import shutil
import subprocess

path = os.environ["PATH"]


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
    elif path := shutil.which(command):
        print(f"{command} is {path}")
    else:
        print(f"{command}: not found")


def command_not_found(command):
    print(f"{command}: command not found")
    return


def findExe(exe):
    paths = path.split(":")

    for pathDir in paths:
        try:
            for filename in os.listdir(pathDir):
                if filename == exe:
                    filePath = os.path.join(pathDir, filename)
                    if os.path.isfile(filePath) and os.access(filePath, os.X_OK):
                        return filePath
        except:
            pass


built_in_commands = {"exit": exit, "echo": echo, "type": type}


def main():
    while True:
        sys.stdout.write("$ ")
        command_input = input()
        command, *args = command_input.split()
        if command not in built_in_commands:
            if path := findExe(command):
                subprocess.run([command] + args)
            else:
                command_not_found(command)
        else:
            if len(args) != 0:
                script = built_in_commands[command]
                script(*args)


if __name__ == "__main__":
    main()
