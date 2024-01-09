import math
import sys
from datetime import datetime

from api import check_name_series, get_imdb_link, get_series_aprox_score, get_detail_seasons, get_new_episodes
from database import get_series, delete_series, insert_series, update_score, get_snoozed, update_snooze, get_all_series, \
    get_score, get_episode


def add_series():
    print("\033[94mADD-SERIES COMMAND\033[92m")
    name = input("Enter the name of the series: ")
    while not check_name_series(name):
        print("Series not found!")
        name = input("Try again! Enter the name of the series: ")

    while get_series(name):
        print("Series already in database!")
        name = input("Try again! Enter the name of the series: ")

    imdb = get_imdb_link(name)

    while True:
        try:
            season = input("Enter the last season: ")
            episode = input("Enter the last episode: ")
            #if get_detail_seasons(name, int(season), int(episode)) == False:
                #raise ValueError("Invalid episode or season!")
            break
        except ValueError as er:
            print(f"{er}")

    while True:
        try:
            date = input("Enter the last date (yyyy-mm-dd): ")
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date!")

    while True:
        try:
            score = input("Enter your score: ")
            if not (0 <= float(score) <= 10):
                raise ValueError("Invalid score!")
            break
        except ValueError as er:
            print(f"{er}")

    insert_series(name, imdb, season, episode, date, str(score))


def del_series():
    print("\033[94mDEL-SERIES COMMAND\033[92m")
    name_series = input("Enter the name of the series: ")

    while not get_series(name_series):
        print("Series not found!")
        name_series = input("Try again! Enter the name of the series: ")

    print()
    delete_series(name_series)


def modify_score():
    print("\033[94mMODIFY-SCORE COMMAND\033[92m")
    name = input("Enter the name of the series: ")

    while not get_series(name):
        print("Series not found!")
        name = input("Try again! Enter the name of the series: ")

    current_score = get_score(name)
    print(f"Current score: {current_score[0]}")

    while True:
        try:
            new_score = input("Enter your score: ")
            if not (0 <= float(new_score) <= 10):
                raise ValueError("Invalid score!")
            break
        except ValueError as er:
            print(f"{er}")

    update_score(name, str(new_score))


def snooze_series():
    print("\033[94mSNOOZE/UNSNOOZE-SERIES COMMAND\033[92m")
    name = input("Enter the name of the series: ")

    while not get_series(name):
        print("Series not found!")
        name = input("Try again! Enter the name of the series: ")

    snoozed = get_snoozed(name)
    while True:
        if snoozed[0] == 0:
            is_snoozed = input("Are you sure to snooze? (Y/N): ")
            if is_snoozed in {'Y', 'y'}:
                update_snooze(name, 1)
                return
            elif is_snoozed in {'N', 'n'}:
                return
        else:
            is_snoozed = input("Are you sure to unsnooze? (Y/N): ")
            if is_snoozed in {'Y', 'y'}:
                update_snooze(name, 0)
                return
            elif is_snoozed in {'N', 'n'}:
                return


def list_of():
    print("\033[94mLIST-SERIES COMMAND\033[92m")
    names_series = get_all_series()
    current_year = datetime.now().year
    print()

    if len(names_series) == 0:
        print("\033[96mYou need to add more series to the database or unsnooze another series!\033[92m")
    else:
        names_series = [names[0] for names in names_series]
        for name in names_series:
            season, episode = get_episode(name)[0].split(", ")
            score = get_score(name)
            score = score[0]
            print(f"\033[96mTV SHOW: {name}")
            print("------------------------------------------")
            print(f"\033[92mYOUR STATUS: SEASON {season}, EPISODE {episode}, SCORE {score}")
            print(f"{current_year} TV SHOWS WITH APROX SCORE: ")
            new_series = get_series_aprox_score(float(score))
            filtered_new_series = [s for s in new_series if get_series(s) is False]
            print(filtered_new_series)
            print()
            print("NEWS!!!: ")
            print(get_new_episodes(name, int(episode), int(season)))
            print()
    print()


def exit_program():
    while True:
        is_exit = input("Are you sure about that? (Y/N): ")
        if is_exit in {'Y', 'y'}:
            print("You are welcome!")
            sys.exit()
        elif is_exit in {'N', 'n'}:
            return
