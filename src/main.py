import sys
from config import Config
from command import Command
from device import Device
from arg import Arg, HELP_VALUE, CLEAR_DEVICE_VALUE, UPLOAD_FILES_VALUE, MONITOR_DEVICE_VALUE


def help():
    pass


def all(config: Config):
    clear_device(config)
    upload_files(config)
    monitor_device(config)


def clear_device(config: Config):
    Device.clear_device(config.options_upload, config.tools)


def upload_files(config: Config):
    commands = Command.create_command(
        config.ignore, config.options_upload, config.tools)

    print("===== Execute commands =====")
    for command in commands.commands:
        Command.execute(command)


def monitor_device(config: Config):
    Command.execute_serial_command(config.options_serial, config.tools)


try:
    arg = Arg(sys.argv[1:])

    if arg.arg & HELP_VALUE:
        print('''Execute

Nenhum argumento = Clear, Upload e Monitor
-h = Ajuda, mostra essa mensagem
-c = Para Clear
-u = Para Upload
-m = para Monitor

Não combine flags se o fizer separe por argumento''')
        pass

    else:
        config = Config.get_config_info()

        Command.execute_reset_device(config.options_serial, config.tools)

        if arg.arg == 0:
            all(config)

        if arg.arg & CLEAR_DEVICE_VALUE:
            clear_device(config)

        if arg.arg & UPLOAD_FILES_VALUE:
            upload_files(config)

        if arg.arg & MONITOR_DEVICE_VALUE:
            monitor_device(config)

except Exception as err:
    print(err)
