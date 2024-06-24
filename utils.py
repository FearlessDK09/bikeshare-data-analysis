def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five rows of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            break
        next += 5
        print(df.iloc[next:next+5])
