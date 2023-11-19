from roku_controller import RokuController


def initialize_aliases():
    ''' Initialize the aliases dictionary '''
    commands = {
        "roku skip": "Select",
        "roku play": "Play",
        "roku pause": "Play"
    }
    return commands


class VoiceController(RokuController):
    def __init__(self):
        super().__init__()
        self.commands = initialize_aliases()

    def execute(self, text):
        ''' Determine whether the text is a valid command and then execute it '''
        # Exit anytime the command is invalid - only need 1 error return
        while True:
            # Text handling
            text = text.lower()
            # Currently, commands are 2 words - so remove anything extra caught
            try:
                text = text.split()[:1]
            except IndexError:
                # command is only one word, not a valid command
                break
            # rejoin the text

            # Determine if its a roku command
            if str(text).startswith("roku"):
                # Determine if its a valid roku command
                if text in self.commands:
                    # Execute the command
                    self.send_command(self.commands[text])
                    # Found a valid command, exit the function
                    return
                else:
                    # Not in the roku command list, invalid
                    break
            else:
                # Not a roku command, invalid
                break
        # No valid command, raise a key error (command not found)
        raise KeyError


def process_commands(text, commands):
    ''' Determine whether the text is a valid command and then execute it '''
    # Exit anytime the command is invalid - only need 1 error return
    while True:
        # Text handling
        text = text.lower()
        # Currently, commands are 2 words - so remove anything extra caught
        try:
            text = text.split()[:1]
        except IndexError:
            # command is only one word, not a valid command
            break
        # rejoin the text

        # Determine if its a roku command
        if text.startswith("roku"):
            # Determine if its a valid roku command
            if text in commands:
                # Execute the command
                commands[text]
                # Found a valid command, exit the function
                return
            else:
                # Not in the roku command list, invalid
                break
        else:
            # Not a roku command, invalid
            break
    raise Exception("Invalid command")
