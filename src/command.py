import os
import subprocess
from path import Path, FILE, DIR
from config import Ignore, Options, Tools


class Command():
    def __init__(self) -> None:
        self.paths: list[Path] = []
        self.commands: list[str] = []

    def _get_paths(self, ignore: Ignore, path=None):
        files = os.listdir(path)

        if len(files) == 0:
            self.paths.remove(self.paths[len(self.paths) - 1])

            return

        for file in files:
            location = f"{'' if path is None else path + '/'}{file}"

            if (os.path.isfile(location)):
                extension = file.split('.')
                extension = '.' + extension[len(extension) - 1]

                if (extension in ignore.extensions):
                    print(f"Skip \t{file}")
                    continue

                self.paths.append(Path(FILE, location))

            elif os.path.isdir(location):
                if (file in ignore.directories):
                    print(f"Skip \t{file}")
                    continue

                self.paths.append(Path(DIR, location))
                Command._get_paths(self, ignore, location)

    def _get_commands(self, options: Options, tools: Tools):
        file_prefix = f"{tools.ampy} --port {options.port} --baud {options.baud} put "
        dir_prefix = f"{tools.ampy} --port {options.port} --baud {options.baud} mkdir "

        for path in self.paths:
            if (path.type is FILE):
                self.commands.append(file_prefix + path.path)
            elif (path.type is DIR):
                self.commands.append(dir_prefix + path.path)

    def execute(command, stdout=subprocess.PIPE):
        print(f"Exec \t{command}")

        process = subprocess.Popen(command.split(), stdout=stdout)
        output, error = process.communicate()

        if error is not None:
            raise Exception(error)

        return output

    def execute_reset_device(options: Options, tools: Tools):
        print("===== Execute reset device =====")
        command = f"{tools.ampy} --port {options.port} --baud {options.baud} reset --safe"
        Command.execute(command)

    def execute_serial_command(options: Options, tools: Tools):
        print("===== Execute serial command =====")
        command = f"{tools.rshell} --port {options.port} --baud {options.baud} repl"
        subprocess.run(command.split())

    def create_command(ignore: Ignore, options: Options, tools: Tools):
        print("===== Create command =====")

        command = Command()
        command._get_paths(ignore)
        command._get_commands(options, tools)

        return command
