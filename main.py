from decimal import Decimal, getcontext
from datetime import datetime

getcontext().prec = 16


def get_data(filepath):
    with open(filepath, "r") as file:
        lines_of_responses = file.readlines()  # tell the program to see the separate lines in input file
    responses_array = []
    for line in lines_of_responses:  # iterate, declare variable response to stand for the line being worked on
        parts = line.strip().split('|')  # break each line up into discreet units using the nicely placed |
        responses_array.append(parts)
    return responses_array  # the file is turned into an array of little arrays, each one with info we need


def write_results_to_file(value, sector_name, filepath="responses.txt"):
    now_date = datetime.now()
    formatted_date = now_date.strftime("%m-%d-%Y %H:%M:%S")  # month-day-year  hour:minute:second
    if isinstance(value, str):  # type of value (literally see function dec above) we enter into the function
        # (i.e., value is a string formatted with %).  f strings let us insert variables into the string.
        message = f"The {sector_name} sector has given us weight of {value} at {formatted_date}"
    else:
        # Assuming monetary when Decimal type input for value, but is the only other input type so else suffices
        message = f"The Market Value Calculation has given us total market value of ${value:.2f} at {formatted_date}"

    with open(filepath, "a") as file:
        file.write(message + "\n")


def market_value(holding_data, security_data):
    total_sum = Decimal("0")
    sectors = {}
    for holding in holding_data:
        for security in security_data:
            if holding[0] == security[0]:  # this match will grow total sum, as well as the associated sector total
                quantity = Decimal(holding[1])
                price = Decimal(security[4])
                m_value = quantity * price
                total_sum += m_value  # easy-peasy, total_sum calculation

                sector_name = security[3]  # Python dictionaries.  Associate the sector with it's own growing value
                if sector_name not in sectors:
                    sectors[sector_name] = m_value
                else:
                    sectors[sector_name] += m_value

    # This write is just for the market value, that's why sector is none.  see sector_weights for calls with sector
    write_results_to_file(total_sum, None, "responses.txt")
    return total_sum, sectors


def sector_weights(sectors, total_sum, filepath):
    for sector, value in sectors.items():
        percentage = f"{(value / total_sum) * 100:.2f}%"  # calculate decimal, times by 100, finish string with %
        write_results_to_file(percentage, sector, filepath)  # percentage is string, write func uses this for logic


holding_data = get_data('holdings.txt')
security_data = get_data('securityData.txt')

# Calculate market values and get the sectors dictionary
total_sum, sectors = market_value(holding_data, security_data)  # again, coding is weird, we returned these values but
# need to save them somewhere

# Calculate and log sector weights
sector_weights(sectors, total_sum, 'responses.txt')

"""Remember, computers are scary efficient but not actually smart.  You need to actually tell them to use the
function that you defined above or nothing happens. You need to save information that you modify or create somehow. 
It just saves that you created some functions and moves on.  Information must be stored and operations must be called 
upon.  This took me a long time to understand."""
