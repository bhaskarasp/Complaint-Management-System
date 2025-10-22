# Complaint Management System

A simple complaint management system built using Python, SQLite, and Tkinter. This application allows users to submit complaints and view a list of existing complaints through a graphical user interface.

## Features

- **Submit Complaints**: Users can enter their name, gender, and comments to submit a complaint.
- **View Complaints**: Users can view a list of all submitted complaints in a structured format.
- **SQLite Database**: All complaints are stored in a local SQLite database.

## Requirements

- Python 3
- Tkinter (usually included with Python installations)
- SQLite (included with Python)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bhaskarasp/complaint-management-system.git
   ```

   ```bash
   cd complaint-management-system
   ```

2. **Install any required packages** (if necessary):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## Usage

1. **Submit a Complaint**:
   - Enter your full name in the provided field.
   - Select your gender using the radio buttons.
   - Write your comment in the text area.
   - Click the "Submit Now" button to submit your complaint.

2. **View Complaints**:
   - Click the "List Comp." button to open a new window displaying all submitted complaints.

## Code Structure

- `db.py`: Contains the `DBConnect` class for database operations.
- `listComp.py`: Contains the `ListComp` class for displaying complaints.
- `main.py`: The main application file that sets up the GUI and handles user interactions.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various open-source projects and tutorials on Python and Tkinter.


