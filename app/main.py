import sys
import os
import shutil
import subprocess

PATH = os.environ["PATH"]
HOME = os.environ["HOME"]


def exit(*args):
    status = int(args[0])
    sys.exit(status)


def echo(*args):
    print(args)
    start = args[0]
    end = args[len(args) - 1]
    if start == "'" and end == "'":
        print()
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
    paths = PATH.split(":")

    for pathDir in paths:
        try:
            for filename in os.listdir(pathDir):
                if filename == exe:
                    filePath = os.path.join(pathDir, filename)
                    if os.path.isfile(filePath) and os.access(filePath, os.X_OK):
                        return filePath
        except:
            pass


def pwd():
    print(os.getcwd())


def cd(*args):
    path_to_cd: str = args[0]
    try:
        cur_path = os.getcwd()
        if path_to_cd.startswith("~"):
            os.chdir(HOME)
        elif path_to_cd.startswith("./"):
            next_dirs = path_to_cd.split("./")
            for next in next_dirs:
                cur_path = cur_path + f"/{next}"
            os.chdir(cur_path)
        elif path_to_cd.startswith("../"):
            prev_dirs = path_to_cd.split("/")
            for prev in prev_dirs:
                if prev == "..":
                    index = cur_path.rindex("/")
                    cur_path = cur_path[0:index]
                else:
                    cur_path = cur_path + f"/{prev}"
            os.chdir(cur_path)
        else:
            os.chdir(path_to_cd)
    except:
        print(f"cd: {path_to_cd}: No such file or directory")


built_in_commands = {
    "exit": {"hasArgs": True, "command": exit},
    "echo": {"hasArgs": True, "command": echo},
    "type": {"hasArgs": True, "command": type},
    "pwd": {"hasArgs": False, "command": pwd},
    "cd": {"hasArgs": True, "command": cd},
}


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

            hasArgs, command = built_in_commands[command].values()
            if hasArgs:
                if len(args):
                    command(*args)
                else:
                    print(f"no args provided to {command}")

            else:
                command()


if __name__ == "__main__":
    main()
