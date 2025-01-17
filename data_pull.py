import requests
import post_scripts.reddit as rd
from utils.constants import COVID_ENDPT


def rolling_average(n, data): 
    """
    Function to calculate an n day rolling average given a list of covid data pts
    @param n: an int representing the number of points to average into the past
    @param data: a list of dictionaries representing covid data pts
    @return: the n day death, death increase, infected, and infected increase averages
    """

    # 10 day rolling average data
    death_total, inc_death_total, inf_total, inc_inf_total = 0,0,0,0

    # Get the last n days and add to total counters
    for i in range(n): 
        curr = data[i]

        death_total += curr['death']
        inc_death_total += curr['deathIncrease']
        inf_total += curr['positive']
        inc_inf_total += curr['positiveIncrease']

    # Divide total counters by n to get n-day average
    return death_total/n, inc_death_total/n, inf_total/n, inc_inf_total/n


def pull(state): 
    """
    Function to pull data from covidtracking api. 
    @param state: a str representing the abbreviation of the state we want to 
                    pull data from 
    @return: a dict containing the daily, 5 day, and 10 day averages for total 
                deaths, increase in deaths, total infected, and daily infected
    """
    url = COVID_ENDPT + state + '/daily.json'
    r = requests.get(url)

    result = {}
    if r.status_code == 200: 
        data = r.json()
        today = data[0]

        # Daily Data
        result['total_deaths'], result['inc_deaths'], \
            result['infected'], result['inc_infected'] \
                = rolling_average(1, data)

        # 5 day avg
        result['5_day_deaths'], result['5_day_inc_deaths'], \
            result['5_day_infected'], result['5_day_inc_infected'] \
                = rolling_average(5, data)
        # 10 day avg
        result['10_day_deaths'], result['10_day_inc_deaths'], \
            result['10_day_infected'], result['10_day_inc_infected'] \
                = rolling_average(10, data)
        
    return result


if __name__ == '__main__': 
    print(rd.process_comment("!c19data"))
