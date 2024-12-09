# SIA 102 - System Integration Project

This project focuses on integrating various healthcare-related systems to manage patient records, discharge processes, and real-time updates on hospital room status. The system is designed to provide hospital staff with an efficient way to track, manage, and analyze data related to patient discharges, deaths, and room availability.

There are two versions of the system in this repository:
- **Codespace Version**: The unedited, default code intended for local development and testing within GitHub Codespaces. This version may require specific configurations for hosting.
- **Hosted Version**: The version optimized and slightly edited for live hosting. It has been deployed on **PythonAnywhere** for production use.

**Live Deployment URL**: [jmt.pythonanywhere.com](http://jmt.pythonanywhere.com)
#For practice use, please use this login credentials:
##Username: 1111
##Password: password123

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
