import subprocess
from config import Options, Tools
from command import Command

class Device():
    def clear_device(options: Options, tools: Tools):
        print("===== Clear device =====")
        
        rm_command = f"{tools.ampy} --port {options.port} --baud {options.baud} rm "
        ls_command = f"{tools.ampy} --port {options.port} --baud {options.baud} ls"
        
        output = Command.execute(ls_command)
        files =  output.decode().split("\n")

        for file in files:
            if (len(file) > 0):
                command = rm_command + file
                output = Command.execute(command)
