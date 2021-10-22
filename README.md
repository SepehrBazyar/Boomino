# Boomino
Boomino Technical Task with FastAPI Framework

## Tools:
1. Back-End: Python, FastAPI, SlowApi(Rate Limiting)
2. DataBase: MongoDB(Motor Driver), Redis

## How to Run?
1. Clone the Project
* `git clone https://github.com/SepehrBazyar/Boomino.git`
2. Create a Virtual Environment("venv" is a Selective Name).
* `virtualenv venv`
3. Activate the Interpreter of the Virtual Environment
* Windows: `venv\Script\active`
* Linux: `source venv/bin/active`
4. Install the Requirements
* `pip install -r requirements.txt`
5. Create `.env` File in Core Directory Based on `env_template` File
6. Run the MongoDB & Redis-Server
7. Write the Following Command to Run the Server
* `python main.py`

## API Routes(Get Method Requests):
* `/sum/`: Takes `a` & `b` Integer Variables in Query String & Return Sum of them.
* `/total/` & `/history/`: Authentication with Username & Password if not Valid Forbidden 403 Status Code.
