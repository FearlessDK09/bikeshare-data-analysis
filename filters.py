def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input("Would you like to see the data for Chicago, New York City, or Washington? ").lower()
    month = input("Which month (all, January, ... June)? ").lower()
    day = input("Which day? (all, Monday, Tuesday, ... Sunday) ").lower()
    print('-' * 40)
    return city, month, day
