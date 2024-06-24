from src.filters import get_filters
from src.data_loader import load_data
from src.statistics import time_stats, station_stats, trip_duration_stats, user_stats
from src.utils import display_raw_data

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            view_raw_data = input('\nWould you like to view first five rows of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
