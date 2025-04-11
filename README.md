# Bi-Weekly Payment Tally Application

This is a simple web application built with Flask that allows users to enter hours worked for two weeks, calculates total hours and total payment based on an hourly rate, and computes overtime if total hours exceed 80.

## Project Structure

```
bi_weekly_payment_app
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── static
│   └── styles.css
├── app.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd bi_weekly_payment_app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

- Enter the hours worked for Week 1 and Week 2.
- Input the hourly rate.
- Submit the form to see the total hours worked and the total payment, including any overtime calculations.

## Dependencies

- Flask
- Waitress (for serving the application)

## License

This project is licensed under the MIT License.