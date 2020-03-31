import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    list_of_cities = ['chicago', 'new york city', 'washington']
    list_of_months = ['all','january','february','march','april','may','june']
    list_of_dayofweek = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    check_city = None
    check_month = None
    check_dayofweek = None

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Please specify the city that you would like to analyze: Chicago, New York Ciy, or Washington?')

    while check_city not in list_of_cities:
        city = input().lower()
        if city in list_of_cities:
            check_city = city
        else:
            print('Please choose between the following options: Chicago, New York City, or Washington')

    # TO DO: get user input for month (all, january, february, ... , june)
    print('Please specify the month you would like to analyze: all, January, February, March, April, May, or June?')

    while check_month not in list_of_months:
        month = input().lower()
        if month in list_of_months:
            check_month = month
        else:
            print('Plase choose between the following options: all, January, February, March, April, May, or June?')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Please specify the day of the week you would like to analyze: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')

    while check_dayofweek not in list_of_dayofweek:
        day = input().lower()
        if day in list_of_dayofweek:
            check_dayofweek = day
        else:
            print('Plase choose between the following options: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #This reads a csv and creates a new month, day_of_week, and hour columns in df
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #This slices the original df by filtering the month and/or day
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = int(months.index(month)) + 1
        df = df.loc[df['month'] == month]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    count_month = df['month'].value_counts().max()
    print('Most common month: ', common_month, ' / ', count_month)

    # TO DO: display the most common day of week
    common_dayofweek = df['day_of_week'].mode()[0]
    count_dayofweek =  df['day_of_week'].value_counts().max()
    print('Most common day of the week: ', common_dayofweek,' / ', count_dayofweek)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    count_hour = df['hour'].value_counts().max()
    print('Most common start hour: ', common_hour, ' / ', count_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    count_start_station = df['Start Station'].value_counts().max()
    print('Most commonly used start station: ', common_start_station, ' / ', count_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    count_end_station = df['End Station'].value_counts().max()
    print('Most commonly used end station: ', common_end_station, ' / ', count_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End_Station'] = df['Start Station'] + ' / ' + df['End Station']
    common_itinerary = df['Start_End_Station'].mode()[0]
    count_itinerary = df['Start_End_Station'].value_counts().max()
    print('Most frequent itinerary: ', common_itinerary, ' / ', count_itinerary)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum() / 3600
    print('Total travel time (in hours): ', total_travel)
    count_travel = df['Trip Duration'].count()
    print('Total count of trips: ', count_travel)
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean() / 60
    print('Average travel time (in minutes): ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if city in ('chicago','new york city'):

        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print(user_types)

        # TO DO: Display counts of gender
        counts_gender = df['Gender'].value_counts()
        print(counts_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest year of birth: ', df['Birth Year'].min())
        print('Most recent year of birth: ', df['Birth Year'].max())
        print('Most common year of birth: ', df['Birth Year'].mode()[0])


    else:
        user_types = df['User Type'].value_counts()
        print(user_types)
        print('Earliest year of birth: Data not available')
        print('Most recent year of birth: Data not available')
        print('Most common year of birth: Data not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        ind_trip_data = input('\nWould you like to see individual trip data? Enter yes or no.\n')

        if ind_trip_data.lower() in ('yes','y'):
            i = 0
            while ind_trip_data.lower() in ('yes','y'):
                print(df[i:i+5])
                i += 5
                ind_trip_data = input('\nWould you like to see individual trip data? Enter yes or no.\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
