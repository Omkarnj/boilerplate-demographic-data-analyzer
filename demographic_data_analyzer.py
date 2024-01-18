import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts())
    

    # What is the average age of men?
    age_men = df[df['sex'] == 'Male']['age']

    average_age_men = round(age_men.mean(),1)
    
    

    # What is the percentage of people who have a Bachelor's degree?
    bach_count = (df[df['education'] == "Bachelors"]['education']).count()

    percentage_bachelors = round(((bach_count / df['education'].count()) * 100) ,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K? 
  
    
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    adv_edu = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(adv_edu)]
    lower_education = df[~df['education'].isin(adv_edu)]

    # percentage with salary >50K
    highed_rich_count = (higher_education[higher_education['salary'] == '>50K']['salary']).count()
    lowed_rich_count = (lower_education[lower_education['salary'] == '>50K']['salary']).count()
    higher_education_rich = round(((highed_rich_count / len(higher_education)) *100),1)
    lower_education_rich = round(((lowed_rich_count / len(lower_education)) *100),1)
    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week,
    # and have a salary of >50K?
    #lets find the number of people who work the min hours per week
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
  #now we find the number of people who work the min hours per week and have a salary >50K
    rich_min_workers = len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])
  #finally the percentage
    rich_percentage = ( rich_min_workers / num_min_workers )* 100

    # What country has the highest percentage of people that earn >50K?
    total_count = df['native-country'].value_counts()
    # print(total_count)
    total_rich_count = df[df['salary'] == ">50K"]['native-country'].value_counts()
    # print(total_rich_count)
    highest_earning_country = (total_rich_count / total_count).idxmax()
    highest_earning_country_percentage = round(((total_rich_count / total_count).max() * 100),1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_ind = df[df['native-country'] == "India"][['native-country','salary','occupation']]
    # df_ind

    salsort_ind = df_ind[df_ind['salary'] == ">50K"][['native-country', 'occupation', 'salary']]
  
    top_IN_occupation = salsort_ind['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
