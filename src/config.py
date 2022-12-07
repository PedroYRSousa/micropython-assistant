import os
import json

FILE_NAME = ".micropythonrc"

class FileConfigNotFoundException(Exception):
    pass

class MissConfigException(Exception):
    pass

class Options():
    def __init__(self, options, name = 'option') -> None:
        if options is None:
            raise MissConfigException(f"configuração de {name} esta faltando")

        self.port = options.get('port')
        self.baud = options.get('baud')

        if self.port is None:
            raise MissConfigException(f"port de {name} esta faltando.")

        if self.baud is None:
            raise MissConfigException(f"baud de {name} esta faltando.")

class Ignore():
    def __init__(self, ignore) -> None:
        self.extensions = []
        self.directories = []

        if ignore is None:
            return

        self.extensions = ignore.get('extensions')
        self.directories = ignore.get('directories')

        if self.extensions is None:
            self.extensions = []

        if self.directories is None:
            self.directories = []

class Tools():
    def __init__(self, tools) -> None:
        if tools is None:
            raise MissConfigException(f"configuração de tools esta faltando")

        self.ampy = tools.get('ampy')
        self.rshell = tools.get('rshell')

        if self.ampy is None:
            raise MissConfigException(f"ampy esta faltando.")

        if self.rshell is None:
            raise MissConfigException(f"rshell esta faltando.")

class Config():
    def __init__(self, options_upload, options_serial, ignore, tools) -> None:
        self.options_upload = Options(options_upload, 'upload')
        self.options_serial = Options(options_serial, 'serial')
        self.ignore = Ignore(ignore)
        self.tools = Tools(tools)

    def get_config_info():
        print("===== Get config =====")

        config = Config._read_file_config()
        return Config(config.get('upload'), config.get('serial'), config.get('ignore'), config.get('tools'))

    def _exists_file_config():
        files = os.listdir()

        return FILE_NAME in files

    def _read_file_config():
        if not Config._exists_file_config():
            raise FileConfigNotFoundException("Arquivo de configuração não encontrado")

        reader = open(FILE_NAME, mode='r', encoding='utf-8')
        config = json.load(reader)
        reader.close()

        return config
