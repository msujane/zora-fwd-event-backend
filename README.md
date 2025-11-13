Backend: FastAPI (Python) for registration, quiz logic, scoring, and leaderboard.


Requirements
**you have to install **
**Python 3.8+
(Optional) SQLite DB**

1)Create Zora folder in which clone the repo by running this command in terminal
git clone https://github.com/msujane/zora-fwd-event-backend.git

2)write the following command to activate the environment

cd zora/backend
python -m venv venv
source venv/bin/activate        
pip install -r requirements.txt 

3)Run the following command for installing the libraries

pip install fastapi uvicorn sqlalchemy pydantic

4)to start the backend server run the final command 

uvicorn main:app --reload
