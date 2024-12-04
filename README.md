
# Projet_Maissa_ENIS

A web application designed to provide users with a dynamic diagnosis based on predefined questions and their responses. The app supports statistical analysis and includes geolocation-based doctor recommendations.

## Features
- Admin functionality to upload and update questions and manage diagnosis logic (score intervals and messages).
- Dynamic question and response handling.
- Real-time score calculation and interval-based diagnosis display.
- Geolocation-based doctor search and booking functionality.
- Comprehensive data collection for statistical analysis.

## Technologies
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (mobile responsive)
- **Database**: PostgreSQL
- **Version Control**: Git
- **Deployment**: Docker-ready

## Database Schema
The schema includes tables for Users, Admins, Questions, Diagnosis, Doctors, and Responses. See the class diagram for relationships.

## Class Diagram
Refer to the `class_diagram.uml` file for the structure.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/BohBOhTN/Projet_Maissa_ENIS.git
   cd Projet_Maissa_ENIS
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations to create the database schema:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Contribution
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.
