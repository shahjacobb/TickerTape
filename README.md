# TickerTape

**TickerTape** is a straightforward and user-friendly web application for personal stock portfolio management. It uses Flask and SQLite for backend operations, and Chart.js for visualizing stock market data provided by Alpha Vantage.

## Tech Stack
### Frontend
- **HTML & CSS** - markup and  styling
- **JavaScript & Chart.js** - Dynamic frontend elements and data visualization.
### Backend
- **Flask** - for web api and server logic
- **Flask-Login** - authentication and session management
- **Werkzeug** - password hashing 
- **SQLite** - small but reliable datastore
### Config
- **python-dotenv** - for loading API key from `os.environ` variable

## Build Instructions For Testing
1. **Clone the Repo:**
   - Clone the TickerTape code with `git clone https://github.com/shahjacobb/TickerTape`.

2. **Virtual Environment:**
   It's best to use a venv since the backend is basically entirely Python. Create and activate a virtual environment by running
     - `python -m venv venv`
     - Windows: `venv\Scripts\activate` (or if you're running **git bash** like me, `source venv/Scripts/Activate`)
     - Unix/Mac: `source venv/bin/activate`

3. **Install Dependencies:**
   - `pip install -r requirements.txt`

4. **Configure Environment Variables:**
We'll need this to secretly store our session secret key and also the API key.
   - Create a `.env` file in the root directory.
   - Include `SECRET_KEY`, `SQLALCHEMY_DATABASE_URI`, and `ALPHA_API_KEY` (for Alpha Vantage).

5. **Initialize the Database:**
   - Run in a Python shell:
     ```python
     from app import db
     db.create_all()
     ```

6. **Run the Application:**
   - `python app.py`

7. **Access the Application:**
   - Open `http://127.0.0.1:5000/` in a browser.

## Additional Notes
- The `ALPHA_API_KEY` is for accessing stock data from [Alpha Vantage](https://www.alphavantage.co/).
- For a more secure production environment, consider secret key managers like [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) or [Vault by HashiCorp](https://www.vaultproject.io/) instead of python-dotenv for portability/scale.

