import time


class Menu:
    def __init__(self):
        self.command = None

    def set_command(self, my_command):
        self.command = my_command

    def get_command(self):
        return self.command

    def valid_command(self):
        return self.command.isdigit() and 1 <= int(self.command) <= 6

    @staticmethod
    def main_menu():
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
        print("Invalid! Retry!")
        print()
        time.sleep(2)
