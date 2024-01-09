import time


class Menu:
    """A class for displaying a menu for managing TV shows."""

    def __init__(self):
        """Initialize a Menu instance."""
        self.command = None

    def set_command(self, my_command):
        """Set the command for the menu.

        Args:
            my_command (str): The command to set.
        """
        self.command = my_command

    def get_command(self):
        """Get the current command.

        Returns:
            str: The current command.
        """
        return self.command

    def valid_command(self):
        """Check if the command is a valid option for operations.

        Returns:
            bool: True if the command is valid, False otherwise.
        """
        return self.command.isdigit() and 1 <= int(self.command) <= 6

    @staticmethod
    def main_menu():
        """Display the main menu with available commands."""
        print("\033[94m-------------------------------")
        print("|          COMMANDS           |")
        print("|      1 - ADD series         |")
        print("|      2 - DEL series         |")
        print("|      3 - MODIFY score       |")
        print("|      4 - SNOOZE series      |")
        print("|      5 - LIST of series     |")
        print("|          6 - EXIT           |")
        print("-------------------------------\033[92m")
        print()

    @staticmethod
    def invalid():
        """Display an invalid command message and cooldown."""
        print("Invalid! Retry!")
        print()
        time.sleep(2)
