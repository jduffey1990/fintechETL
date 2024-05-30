from decimal import Decimal, getcontext
from datetime import datetime
import os

getcontext().prec = 16


def get_data(filepath):
    """Reads a file and returns its contents as a list of lists, splitting each line by '|'. """
    try:
        with open(filepath, "r") as file:
            return [line.strip().split('|') for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading {filepath}: {e}")
        return []


def write_results_to_file(value, sector_name, filepath="responses.txt"):
    """Writes the given value and sector information to the specified file with a timestamp."""
    now_date = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    if isinstance(value, str):
        message = f"The {sector_name} sector has given us weight of {value} at {now_date}"
    else:
        message = f"The Market Value Calculation has given us total market value of ${value:.2f} at {now_date}"

    with open(filepath, "a") as file:
        file.write(message + "\n")


def market_value(holding_data, security_data):
    """Calculates the total market value and individual sector values from the provided data."""
    total_sum = Decimal("0")
    sectors = {}

    for holding in holding_data:
        for security in security_data:
            if holding[0] == security[0]:
                quantity = Decimal(holding[1])
                price = Decimal(security[4])
                m_value = quantity * price
                total_sum += m_value

                sector_name = security[3]
                if sector_name not in sectors:
                    sectors[sector_name] = m_value
                else:
                    sectors[sector_name] += m_value

    write_results_to_file(total_sum, None, "responses.txt")
    return total_sum, sectors


def sector_weights(sectors, total_sum, filepath):
    """Calculates and logs the weight of each sector as a percentage of the total market value."""
    for sector, value in sectors.items():
        percentage = f"{(value / total_sum) * 100:.2f}%"
        write_results_to_file(percentage, sector, filepath)


def main():
    holding_filepath = 'holdings.txt'
    security_filepath = 'securityData.txt'

    if not os.path.exists(holding_filepath) or not os.path.exists(security_filepath):
        print("Error: One or both data files are missing.")
        return

    holding_data = get_data(holding_filepath)
    security_data = get_data(security_filepath)

    if not holding_data or not security_data:
        print("Error: Data could not be read from one or both files.")
        return

    total_sum, sectors = market_value(holding_data, security_data)
    sector_weights(sectors, total_sum, 'responses.txt')


if __name__ == "__main__":
    main()
