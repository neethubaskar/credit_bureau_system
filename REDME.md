# Credit Bureau Update System

This project is a Credit Bureau Update System built using Django and PostgreSQL. The system calculates a user's credit score based on answers to predefined questions. The answers are stored in a database and dynamically displayed using a popup interface. The application is containerized using Docker for easy deployment.

## Features

- **Dynamic Question Popup**: Displays a series of questions to the user in a popup interface.
- **Credit Scoring Algorithm**: Calculates a user's credit score based on their responses to the questions.
- **User Responses Tracking**: Stores and tracks user responses in a PostgreSQL database.
- **Admin Interface**: Allows easy management of questions, answers, and user responses via Django's admin panel.
- **Dockerized Application**: The entire application is containerized for easy setup and deployment.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**
- **Docker and Docker Compose** (for containerization and easy deployment)
- **PostgreSQL** (Database service is provided through Docker)

## Installation

### Step 1: Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/credit-bureau-system.git
cd credit-bureau-system
