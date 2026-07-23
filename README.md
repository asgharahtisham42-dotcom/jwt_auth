JWT Auth App (Flask + PostgreSQL)
Sign up, sign in, edit your profile, manage fellows (contacts linked to your account), track security audit logs, and manage roles — powered by Flask, PostgreSQL (Flask-SQLAlchemy), and PyJWT.
1. Prerequisites (PostgreSQL Setup)
Make sure you have PostgreSQL installed and running on localhost:5432.
Create the database Jwt_Login in PostgreSQL:
CREATE DATABASE "Jwt_Login";
2. Project Setup
# Navigate to directory
cd jwt_auth_app

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate        # Linux/macOS: source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables (.env)
Ensure your .env file contains:
generate SECRET_Key from terminal 
SECRET_KEY=your-random-secret-key
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/Jwt_Login

3. Run the Application
py run.py
(All database tables will be automatically created on application startup).

Visit http://localhost:5000 in your browser.

4. Run Automated Unit Tests
Unit tests use pytest with an in-memory SQLite database, running fast and independently without requiring PostgreSQL:

py -m pytest
5. Key API Endpoints
All protected endpoints require the HTTP header: Authorization: Bearer <JWT_TOKEN>

Method	Endpoint	Auth Required	Role Required	Description
POST	/api/v1/auth/signup	No	—	Register new user account
POST	/api/v1/auth/signin	No	—	Authenticate user & receive JWT tokens
POST	/api/v1/auth/refresh	No	—	Refresh access token
GET	/api/v1/profile	Yes	—	Fetch profile information
PUT	/api/v1/profile	Yes	—	Update profile fields
POST	/api/v1/profile/picture	Yes	—	Upload profile avatar
GET	/api/v1/fellows	Yes	—	List fellows (supports q, page, limit, sort, order)
POST	/api/v1/fellows	Yes	—	Create new fellow contact
PUT	/api/v1/fellows/<id>	Yes	—	Update fellow contact
DELETE	/api/v1/fellows/<id>	Yes	—	Delete fellow contact
GET	/api/v1/dashboard/stats	Yes	—	User dashboard metrics
GET	/api/v1/analytics/summary	Yes	—	Contact relationship analytics
PUT	/api/v1/admin/users/<id>/role	Yes	Admin	Update user role (Admin, Manager, User)
GET	/api/v1/admin/audit-logs	Yes	Admin	View system audit logs
