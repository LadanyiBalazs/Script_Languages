#!/usr/bin/env python3

import locale

# Setting the locale to US English
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

lang_info = [("Ashton Cox", "Junior Technical Author", "San Francisco", 66, "2009-01-12", 86000),
            ("Michael Silva", "Marketing Designer", "London", 66, "2012-11-27", 198500),
            ("Jackson Bradshaw", "Director", "New York", 65, "2008-09-26", 645750),
            ("Paul Byrd", "Chief Financial Officer (CFO)", "New York", 64, "2010-06-09",725000),
            ("Olivia Liang", "Support Engineer", "Singapore", 64, "2011-02-03", 234500),
            ("Serge Baldwin", "Data Coordinator", "Singapore", 64, "2012-04-09", 138575),
            ("Garrett Winters", "Accountant", "Tokyo", 63, "2011-07-25", 170750),
            ("Zenaida Frank", "Software Engineer", "New York", 63, "2010-01-04", 125250),
            ("Vivian Harrell", "Financial Controller", "San Francisco", 62, "2009-02-14", 452500),
            ("Tiger Nixon", "System Architect", "Edinburgh", 61, "2011-04-25", 320800)]


def main():
    print("{0:<20} {1:<30} {2:^16} {3:^5} {4:^10} {5:>10}".format("Name", "Position", "Office", "Age", "Start Date", "Salary"))
    print("-"*96)
    for element in lang_info:
        print("{0:<20} {1:<30} {2:<16} {3:^5} {4:^10} {5:>10n}".format(element[0], element[1], element[2], element[3], element[4], element[5]))
    return
    
if __name__ == "__main__":
    main()