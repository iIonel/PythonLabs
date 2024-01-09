import connection as con
import menu as m
from commands import add_series, del_series, modify_score, snooze_series, list_of, exit_program


def execute():
    connection = con.connect_db()

    if connection:
        menu = m.Menu()
        while True:
            menu.main_menu()
            menu.set_command(input("Enter command: "))

            if menu.valid_command():
                if int(menu.get_command()) == 1:
                    add_series()
                elif int(menu.get_command()) == 2:
                    del_series()
                elif int(menu.get_command()) == 3:
                    modify_score()
                elif int(menu.get_command()) == 4:
                    snooze_series()
                elif int(menu.get_command()) == 5:
                    list_of()
                else:
                    exit_program()
            else:
                menu.invalid()


if __name__ == '__main__':
    execute()
