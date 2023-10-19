# CSCodes Website Documentation

Welcome to the CSCodes website repository! This web application is designed to showcase and add referral codes for various CS-related services. Below is an in-depth walkthrough to help understand and get started with the project.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Directory Structure](#directory-structure)
- [Setting Up Locally](#setting-up-locally)
- [Contributing](#contributing)
- [License](#license)

## Overview

This web application provides the following main features:
1. Display of referral codes in a carousel format.
2. Ability for users to submit their referral codes.
3. A responsive navigation bar.
4. User feedback through notifications.
5. Links to associated social media and code repositories.

## Technologies Used

- **Flask**: Python micro web framework.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **SQLite**: Lightweight disk-based database.
- **Bootstrap**: Front-end framework for building responsive web UI.
- **FontAwesome**: Icon toolkit based on CSS and LESS.
- **JavaScript**: Scripting language to make web pages interactive.

## Directory Structure

- **Flask App Initialization**: Everything starts with the Flask application initialization and configuration.
- **Database**: Utilizing SQLite for storage, SQLAlchemy helps in querying the data required for the carousel and other components.
- **Routes**:
    - `/`: Renders the homepage and displays all the available referral codes.
    - `/add_referral`: Endpoint to handle the addition of new referral codes.
- **JavaScript**: The `scripts.js` file helps in controlling the behavior of the responsive navigation bar.

## Setting Up Locally

1. **Environment Setup**:
   - Create a Python virtual environment.
   - Activate the environment.
2. **Dependencies Installation**:
   - Install the required packages and libraries using pip.
3. **Database Initialization**:
   - Initialize the SQLite database with the required tables.
4. **Run**:
   - Start the Flask server using the `app.run()` command.

## Contributing

Contributions are always welcome! If you have suggestions, bug reports, or enhancements, feel free to fork the repository and create a pull request.

## License

The CSCodes website is open-sourced software licensed under the MIT License. Please check the LICENSE file in the root directory for more details.

