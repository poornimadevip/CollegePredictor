# College Predictor

College Predictor is a web application that helps users find suitable colleges or institutes based on their rank and other criteria. The application uses a Flask backend and reads data from an Excel file to filter and display results.

## Features

- Filter institutes based on rank, academic programs, gender, quota, year, and round.
- Display results in a user-friendly table format.
- Download filtered results as an Excel file.

## Prerequisites

- Python 3.x installed on your system.
- Required Python libraries: `Flask`, `pandas`, `openpyxl`.

## Installation

1. Clone this repository or download the source code.
2. Navigate to the project directory:
   ```
   cd CollegePredictor
   ```
3. Install the required Python libraries
``` pip install -r requirements.txt```

## Usage
1. Place the Excel file containing the institute data (e.g., RankList.xlsx) in the project directory. Ensure the file has the necessary columns like Opening Rank, Closing Rank, Gender, Academic Program Name, etc.
2. Run the Flask application
``` python app.py```
3. Open your browser and navigate to http://127.0.0.1:5000.
4. Enter your rank and other criteria to find matching institutes.
5. View the results or download them as an Excel file.

## File Structure
## File Structure
[app.py](app.py): The main Flask application.
[templates/index.html](templates/index.html): The HTML template for the web interface.
[static/style.css](static/style.css): The CSS file for styling the application.
[RankList.xlsx](RankList.xlsx): The Excel file containing institute data (to be provided by the user).
[requirements.txt](requirements.txt): The list of required Python libraries.

## Notes
Ensure the Excel file ([RankList.xlsx](RankList.xlsx)) has the correct column names and data format.
The application is designed for local use. For deployment, additional configurations may be required.


## License
This project is licensed under the MIT License. 