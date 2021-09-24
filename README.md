# Tiger card
Driver code: [driver_code.py](driver_code.py)

## Usage
    python3 driver_code.py [options]
    Options:
      -h, --help                    Show his help message and exit
      -f INPUT_FILE                 CSV file containing the journey details

#### Example
    python3 driver_code.py -f <input file>
    
To change the journey details, add/modify the input.csv file or create a new csv file with the following fields:

    1. Date(dd-mm-yy)
    2. Time(hh:mm)
    3. Starting zone for the journey
    4. Ending zone for the journey

## Test cases
[TestTigerCard.py](TestTigerCard.py)

