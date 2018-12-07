import csv
import re
import datetime


def valid_date_search():
    """
    This function checks if the date provided by the user for searching is a
    valid date by checking it against the dd/mm/yyyy format from the datetime
    library and keeps on running until a valid date is input. It displays
    the search results after being given a valid date.
    """
    while True:
            user_date = input('Please enter a date in the DD/MM/YYYY format: ')
            try:
                datetime.datetime.strptime(user_date, "%d/%m/%Y")
                search_by_date(user_date)
                break
            except ValueError:
                print('You have entered an invalid date. Please try again.')


def valid_date_add():
    """
    This function is a bit different from valid_date_search since it is
    returning the date input by the user after checking if it is valid.
    """
    while True:
            user_date = input('Please enter a date in the DD/MM/YYYY format: ')
            try:
                datetime.datetime.strptime(user_date, "%d/%m/%Y")
                return user_date
            except ValueError:
                print('You have entered an invalid date. Please try again.')


def add_entry(new_entry, task_title, time_spent, notes):
    """
    This function takes the variables from the user and appends them to the
    csv file. If no file exists then it is created. Entries are stored as
    DictWriter objects so that it is easy to search them.
    """
    with open("log.csv", "a", newline='') as csvfile:
        fieldnames = ['Date', 'Task Name', 'Time Spent', 'Notes']
        log_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        log_writer.writerow({
            'Date': '{}'.format(new_entry),
            'Task Name': '{}'.format(task_title),
            'Time Spent': '{}'.format(time_spent),
            'Notes': '{}'.format(notes)
        })


def search_by_date(user_date):
    """
    Searches the csv file for a given valid date by the user.
    """
    try:
        with open("log.csv", newline='') as csvfile:
            fieldnames = ['Date', 'Task Name', 'Time Spent', 'Notes']
            log_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(log_reader)

            found = False
            for row in rows:
                if row['Date'] == user_date:
                    found = True
                    print('Date:', row['Date'])
                    print('Title:', row['Task Name'])
                    print('Time Spent:', row['Time Spent'])
                    print('Notes:', row['Notes'])
                    print('')
            if found:
                input('Search results displayed. Press enter to return to '
                      'the search'
                      'menu')
            if not found:
                print('Entry does not exist')
    except FileNotFoundError:
        print('No entries have been recorded yet.')
        input('Press enter to return to the search menu')


def search_by_time_spent(user_time):
    """
    Searches the csv file for entries matching the elapsed time given by user.
    """
    try:
        with open("log.csv", newline='') as csvfile:
            fieldnames = ['Date', 'Task Name', 'Time Spent', 'Notes']
            log_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(log_reader)

            found = False
            for row in rows:
                if row['Time Spent'] == str(user_time):
                    found = True
                    print('Date:', row['Date'])
                    print('Title:', row['Task Name'])
                    print('Time Spent:', row['Time Spent'])
                    print('Notes:', row['Notes'])
                    print('')

            if found:
                input('Search results displayed. Press enter to return to '
                      'the search'
                      'menu')

            if not found:
                print('Entry does not exist')
    except FileNotFoundError:
        print('No entries have been recorded yet')
        input('Press enter to return to the search menu')


def search_by_exact_search(user_string):
    """
    Searches the notes and task name columns against the given user_string.
    """
    try:

        with open("log.csv", newline='') as csvfile:
            fieldnames = ['Date', 'Task Name', 'Time Spent', 'Notes']
            log_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(log_reader)

            found = False
            for row in rows:
                if row['Task Name'] == user_string or row['Notes'] ==  \
                        user_string:
                    found = True
                    print('Date:', row['Date'])
                    print('Title:', row['Task Name'])
                    print('Time Spent:', row['Time Spent'])
                    print('Notes:', row['Notes'])
                    print('')
            if found:
                input('Search results displayed. Press enter to return to '
                      'the search'
                      'menu')
            if not found:
                print('Entry does not exist')
    except FileNotFoundError:
        print('No entries have been recorded yet.')
        input('Press enter to return to the search menu')


def search_by_pattern(user_pattern):
    """
    Searches the csv file for a given regex pattern.
    """
    try:
        with open("log.csv", newline='') as csvfile:
            fieldnames = ['Date', 'Task Name', 'Time Spent', 'Notes']
            log_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(log_reader)

            found = False
            for row in rows:
                if user_pattern.search(str(row)):
                    found = True
                    print('Date:', row['Date'])
                    print('Title:', row['Task Name'])
                    print('Time Spent:', row['Time Spent'])
                    print('Notes:', row['Notes'])
                    print('')
            if found:
                input('Search results displayed. Press enter to return to '
                      'the search menu')
            if not found:
                print('Entry does not exist')
    except FileNotFoundError:
        print('No entries have been recorded yet')
        input('Search results displayed. Press enter to return to the main'
              'menu')


def search():
    """
    This menu is displayed when the user wants to search for an existing
    record.
    """
    while True:
        search_input = input('Do you want to search by:\n'
                             'a) Exact Date\n'
                             'b) Time Spent\n'
                             'c) Exact Search\n'
                             'd) Pattern\n'
                             'e) Return to main menu\n')

        if search_input.upper() == 'A':
            valid_date_search()

        if search_input.upper() == 'B':
            while True:
                try:
                    user_time = int(input('Please enter an integer: '))
                    break
                except ValueError:
                    print('Please enter a valid integer')

            search_by_time_spent(user_time)

        if search_input.upper() == 'C':
            user_string = input('Please enter a string to search: ')
            search_by_exact_search(user_string)

        if search_input.upper() == 'D':
            pattern_input = input('Please enter a regex pattern to search: ')
            user_pattern = (re.compile(r'''
                %s
             ''' % pattern_input, re.X | re.M))

            search_by_pattern(user_pattern)

        if search_input.upper() == 'E':
            break


def main_menu():
    """
    This menu is displayed when the program is run. It has options to add
    records, search for existing records and quit the program.
    """
    while True:
        user_input = input('WORK LOG\n'
                           'What would you like to do?\n'
                           'a) Add new entry\n'
                           'b) Search in existing entries\n'
                           'c) Quit program\n')

        if user_input.upper() == 'A':
            new_entry = valid_date_add()
            task_title = input('Title of the task: ')

            while True:
                try:
                    time_spent = int(input('Time spent (rounded in '
                                           'minutes): '))
                    break
                except ValueError:
                    print('Please enter a valid integer')

            notes = input('Notes (Optional, you can leave this empty): ')

            add_entry(new_entry, task_title, time_spent, notes)

            input('The entry has been added. Press enter to return to the '
                  'menu')

        if user_input.upper() == 'B':
            search()
            continue

        if user_input.upper() == 'C':
            break


main_menu()
