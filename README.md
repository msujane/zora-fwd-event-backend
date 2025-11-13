Backend: FastAPI (Python) for registration, quiz logic, scoring, and leaderboard.


**Link for Frontend**
https://github.com/msujane/zora-fwd-event.git

Requirements
**you have to install **
**Python 3.8+
(Optional) SQLite DB**
1. Create Project Folder and Clone Repo
# Create your base folder and move into it
- mkdir zora
- cd zora

# Clone the repository
- git clone https://github.com/msujane/zora-fwd-event-backend.git

- cd zora-fwd-event-backend     # Enter the cloned backend code folder

2. Create and Activate Python Virtual Environment
- python -m venv venv
- source venv/bin/activate         # On Windows, use: venv\Scripts\activate

3. Install All Requirements
If a requirements.txt file is present:

- pip install -r requirements.txt
- pip install fastapi uvicorn sqlalchemy pydantic


4)to start the backend server run the final command 

- uvicorn main:app --reload
