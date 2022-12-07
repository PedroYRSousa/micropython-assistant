CLEAR_DEVICE_TEXT = '-c'
CLEAR_DEVICE_VALUE = 0b0001
UPLOAD_FILES_TEXT = '-u'
UPLOAD_FILES_VALUE = 0b0010
MONITOR_DEVICE_TEXT = '-m'
MONITOR_DEVICE_VALUE = 0b0100
HELP_TEXT = '-h'
HELP_VALUE = 0b1000

class Arg():
    def __init__(self, argv: list[str]) -> None:
        self.arg = 0b0000

        if (len(argv) == 0):
            return

        for arg in argv:
            if (arg == HELP_TEXT):
                self.arg = HELP_VALUE
                return
            
            if (arg == CLEAR_DEVICE_TEXT):
                self.arg += CLEAR_DEVICE_VALUE
            if (arg == UPLOAD_FILES_TEXT):
                self.arg += UPLOAD_FILES_VALUE
            if (arg == MONITOR_DEVICE_TEXT):
                self.arg += MONITOR_DEVICE_VALUE