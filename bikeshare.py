import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities=['chicago','new york city','washington']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: inget user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new york city','washington']
    city=' '
    while True:
        city=str(input('\nPlease enter your city, please choose from Chicago, New York city and Washington :').lower())
        if city not in cities:
            print('\nWe are sorry, your chosen city is not available, please choose from Chicago, New York city and Washington')
        else:
            print('You have selected: ', city)
            break
    month=' '
    while True:
        month= str(input('Enter month to filter by months, please choose january to june or choose\nall if you don"t want to filter : ').lower())
        if month not in months:
            print('\nooops! invalid month, please choose january to june or choose\nall if you don"t want to filter')

        else:
            print('You have selected: ', month)

            break
    day=' '
    while True:
        day= str(input('Enter day to filter by days, please choose monday to sunday or choose\nall if you don"t want to filte: ').title())
        if day not in days:
            print('\nooops! invalid day, please choose monday to sunday or choose\nall if you don"t want to filter')
        else:
            print('You have selected: ', day)
            break

    print('-'*40)
    return city, month, day
# load day, month and city from data file
def load_data(city, month, day):

   df=pd.read_csv(CITY_DATA[city])
   df['Start Time'] = pd.to_datetime(df['Start Time'])
   df['month'] =df['Start Time'].dt.month
   df['day_of_week'] = df['Start Time'].dt.weekday_name
   df['hour'] = df['Start Time'].dt.hour
   #filter by day if applicable
   if month.lower() !='all':
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    imonth = months.index(month) + 1
    df = df.loc[df['month'] == imonth]
    #filter by day if applicable
   if day.lower() != 'all':
    days = ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']
    df = df.loc[df['day_of_week'] == day.title()]
   return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

  #Dispaly the most common month"""
    The_most_commmon_month= df['month'].mode()[0]
    print('The most common month is: ' + months[ The_most_commmon_month].title())

    #display the most common day of week
    The_most_commmon_day= df['day_of_week'].mode()[0]
    print('The most common day is: ',  The_most_commmon_day)

    #display the most common start hour
    the_most_common_start_hour= df['hour'].mode()[0]
    print('The most common hour is: '  + str(the_most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most start station: \n {}'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station= df['End Station'].mode()[0]
    print('The most common end station: \n {}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip= df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most common trip is: \n {}'.format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the average and total trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time= df['Trip Duration'].sum().round()
    print('The total travel time is: ',(total_travel_time))

    # display mean travel time
    mean_travel_time= df['Trip Duration'].mean().round()
    print('The mean travel time is:', (mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        user_types =df['User Type'].value_counts()

        print('\nThe count of user types is:\n' + str(user_types))

    else:
         print('User Type does not exist in this dataset')

    # TO DO: Display counts of gender
    for city in cities:
        try:
            gender = df['Gender'].value_counts()
        except KeyError:
            print('Wahington does not have gender column, please select either chicago or new york city')
            break
        else:
            print('\nThe count of user gender is:\n' + str(gender))
            break
    #  Display earliest, most recent, and most common year of birth

    # The earliest year of birth
    for city in cities:
        try:
            earliest_birth_year=df['Birth Year'].min()
        except KeyError:
            print('Wahington does not have birth column, please select either chicago or new york city')
            break
        else:
            print('The earliest birth year is:', int(earliest_birth_year))
            break

    #most recent birth year
    for city in cities:
        try:
            most_recent_birth_year = df['Birth Year'].max()
        except KeyError:
            print('Wahington does not have birth column, please select either chicago or new york city')
            break
        else:
            print('The earliest birth year is:', int(most_recent_birth_year))
            break
    #most common birth year
    for city in cities:
        try:
           most_common_birth_year = df['Birth Year'].mode()[0]
        except KeyError:
            print('Wahington does not have birth column, please select either chicago or new york city')
            break
        else:
            print('The most common birth year is:', int(most_common_birth_year))
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    data = 0
   # TO DO: Display raw data up to 200 columns
    pd.set_option('display.max_columns',200)
    while True:
        raw = input("would you like to see the first 5 raw data? ").lower()
        if raw == 'no':
            break
        # TO DO: appropriately subset/slice your dataframe to display next five rows

        elif raw == 'yes':
               print(df[data : data+5])
               data += 5

        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            continue
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        # TO DO: convert the user input to lower case using lower() function
        restart= " "

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart.lower() not in ['yes', 'no']:
            restart=input('Invalid input, please enter yes or no: ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":

    main()
