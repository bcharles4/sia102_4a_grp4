# SIA 102 - System Integration Project

This project focuses on integrating various healthcare-related systems to manage patient records, discharge processes, and real-time updates on hospital room status. The system is designed to provide hospital staff with an efficient way to track, manage, and analyze data related to patient discharges, deaths, and room availability.

There are two versions of the system in this repository:
- **Codespace Version**: The unedited, default code intended for local development and testing within GitHub Codespaces. This version may require specific configurations for hosting.
- **Hosted Version**: The version optimized and slightly edited for live hosting. It has been deployed on **PythonAnywhere** for production use.

**Live Deployment URL**: [jmt.pythonanywhere.com](http://jmt.pythonanywhere.com)

## Features

### 1. **Data Analysis Charts**
   - **Illnesses Per Month**: Visual representation of the number of illnesses reported each month.
   - **Types of Illnesses**: A breakdown of the most common illnesses reported during each month.
   - **Deaths Per Month**: A graph showing the number of patient deaths recorded each month.
   - **Causes of Death**: A chart that details the diseases or conditions that caused patient deaths.

### 2. **Current Patients Admitted**
   - A real-time webpage that lists all patients currently admitted to the hospital, including their admission details and status.

### 3. **Room Availability Status**
   - A dedicated webpage showing the status of hospital rooms, indicating whether rooms are currently available or occupied.

### 4. **Discharged Patient Records**
   - A webpage containing records of all patients who have been discharged from the hospital, including discharge dates and reasons.

### 5. **Deceased Patient Discharge Records**
   - A webpage showing records of patients who were discharged due to death, including the cause of death and discharge dates.

### 6. **Patient Discharge Notifications**
   - A notification system that displays a list of patients waiting to be discharged. Hospital staff can manage discharge actions directly from this page, with options to:
     - Discharge a patient.
     - Discharge a deceased patient.

## Installation Instructions

### Codespace Version
1. Open the repository in GitHub Codespaces.
2. Follow the setup instructions provided in the `codespace_setup.md` (if applicable) to configure the environment.
3. Run the application using the provided `docker-compose` or `npm` commands (depending on the environment setup).
4. Make sure all dependencies are installed and configurations are correctly set up for local testing.

### Hosted Version (PythonAnywhere)
1. Clone or download the repository.
2. Navigate to the `hosted_version/` directory.
3. Ensure that all configurations are suitable for deployment on PythonAnywhere (e.g., database settings, allowed hosts, etc.).
4. Deploy the system on **PythonAnywhere** following these steps:
   - Create an account on [PythonAnywhere](https://www.pythonanywhere.com/).
   - Set up a new web app in your PythonAnywhere dashboard.
   - Choose the **Django** option and follow the steps for setting up your Django project.
   - Upload your project files to PythonAnywhere and configure the environment (e.g., virtualenv, database, static files).
5. Once the setup is complete, the system will be live at [jmt.pythonanywhere.com](http://jmt.pythonanywhere.com).

## Notes
- The **Codespace Version** may not work directly on PythonAnywhere due to different environment configurations (e.g., database, server settings).
- The **Hosted Version** is specifically optimized for live hosting on PythonAnywhere. Please ensure you have correctly configured the project for production use (settings for allowed hosts, database, static files, etc.).
- You can find further deployment instructions in the [PythonAnywhere documentation](https://help.pythonanywhere.com/).

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- Thanks to all contributors and collaborators who helped in developing and testing the system.
