# Design Understanding

## `app.py`

The file is a Flask application for my SCUBA log project. It facilitates user registration, login, and logout, ensuring data security through password hashing. The application includes features for logging dive information, managing gear details, and recording travel destinations. Each route corresponds to a specific functionality, such as displaying a user's dive log summary on the home page `/`, logging a new dive `/dive_log`, and viewing or logging gear information `/gear_log`. The use of custom helper functions, such as `apology` and `login_required`, enhances code readability and maintains a clean structure. Overall, the application employs Flask, SQLite, and CS50 libraries to create a user-friendly SCUBA log platform.

### Credits

`app.py` has code that was taken from the CS50 Finance project and was written by the CS50 team.
- `app.after_request`
- `/register`
- `/login`
- `/logout`

## `design.md`

A design document for the project that discusses how I implemented the project. This is a requirement for the CS50 final project.

## `helpers.py`

This file has the implementation of `apology`. It renders a template, `apology.html` and defines another function, `escape` too replace special characters in apologies.
The file also defines `login_required`.

### Credits

`helpers.py` was taken from the CS50 Finance project. All code written in the file was written by the CS50 team.

## `project.db`

This file is a SQLite database used by the SCUBA log Flask application to store user-related data. It serves as the backend data storage for the project, holding information such as user details, dive logs, gear entries, and travel destinations. The database consists of multiple tables, including `users` for storing user authentication information, `dive_log` to record dive-related data, `gear_log` to manage gear details, and `travel` to store information about travel destinations. The database schema is designed to efficiently store and retrieve data, supporting the functionality of the SCUBA log project.

## `readme.md`

This is a user-friendly, informative document that facilitates a smooth understanding and utilization of the SCUBA log Flask application.

## `requirements.txt`

This file simply prescribes the packages on which this app will depend.

### Credits

`requirements.txt` was taken from the CS50 Finance project. This file was written by the CS50 team.

## `static/`

Inside off this file is the `styles.css` for the app. This `.css` is a vary simple file with minimal design.

## `templates/`

This folder contains multiple files to take input from the user and display information to the user.

### `apology.html`

This is the apology to the user if an error comes up. This will show a turtle with an error message for the user. It took me a long time to understand exactly how the apology was rendered and how the the picture was being fed to the meme generator. After this I was able to figure out how to feed a new image for the message to be rendered on.

#### Credits

Most of this file was written by the CS50 team for the Finance project. Line 8 was the only line that was changed to change the image.

### `dive_log.html`

This file is the HTML template for the Dive Log form page in the SCUBA log Flask application. It extends the "layout.html" template, ensuring a consistent structure across pages. The page features a header "Dive Log," and the main content is a form for users to log details of a new dive. The form includes input fields for Dive Number, Dive Date, Location, Surface Interval, Time In, Dive Time, Max Depth, Average Depth, Gas Used, and Notes. Each input field is appropriately labeled and formatted, utilizing various input types such as number, date, time, and text. Additionally, the form incorporates pattern validation for time-related input fields. The form concludes with a "Submit" button allowing users to add a new dive log entry. This HTML template provides a user-friendly interface for entering dive information in a structured manner.

### `gear_log.html`

This file serves as the HTML template for the Gear Log page in the SCUBA log Flask application. It extends the "layout.html" template for a consistent page structure. The page begins with a heading "Gear Log" and includes a table displaying gear log entries. The table has columns for Type, Brand, Date Purchased, Condition, Last Serviced, and Notes. Using a loop, it dynamically populates the table rows with gear details retrieved from the database.

Unlike the dive log, the gear log puts both the log itself and the input of the log on the same page. I like the ease of access of this, but I don't like how much room the form takes up. In the future, I would maybe use JS to hide the form if the user is not using it.

Below the table, there's a form for adding new gear entries. The form contains input fields for Gear Type, Brand, Date Purchased, Condition, Date Last Serviced, and Notes. Each input field is appropriately labeled and formatted, including date and text input types. Users can enter information about their gear and submit the form to add a new gear log entry.

Overall, this HTML template provides a structured and user-friendly interface for viewing and managing gear log data in the SCUBA log application.

### `index.html`

The file serves as the HTML template for the History page in the SCUBA log Flask application. It extends the "layout.html" template for a consistent page structure. The page begins with a heading displaying the user's name, retrieved from the database.

Below the heading, there's a table for displaying the dive history. The table has columns for Dive Number, Date, Location, Surface Interval, Time In, Dive Time, Max Depth (ft), Average Depth (ft), Gas Used, and Notes. Using a loop, it dynamically populates the table rows with dive log entries retrieved from the database.

Additionally, the table includes a footer row displaying the Total Time in Water, calculated by summing up the dive times from all entries. This provides a summary statistic for the user's overall diving experience. This was the most time consuming part of this project. I spend a long time trying to figure out how to easily add time in HH:MM:SS format.

Overall, this HTML template provides a structured and informative interface for users to view their dive history, including key details and a total time calculation.

### `layout.html`

The 'layout.html' file serves as the base HTML template for all pages in the SCUBA log Flask application, providing a consistent structure and styling. Here's a breakdown of its key components:

1. Head Section: Contains meta tags for character set and viewport, links to Bootstrap CSS stylesheets, a favicon link, a link to a custom stylesheet, and sets the page title based on the content within the "title" block.

2. Body Section:
- Navbar: A responsive Bootstrap navbar with the application brand, a toggle button for small screens, and navigation links. The links dynamically change based on whether a user is logged in or not.
- Flash Messages: Displays alert messages if there are flashed messages, typically used for notifications or success messages.
- Main Content Area: The central part of the page where content specific to each page is injected using the `{% block main %}{% endblock %}` syntax.
- Footer: Contains a small text with a disclaimer stating that the website was created using the CS50 Finance Project as a foundation.

Overall, `layout.html` establishes a clean and responsive layout for the entire application, with consistent navigation, styling, and a flexible structure to accommodate different page content. The use of Bootstrap ensures a visually appealing and user-friendly design.

#### Credit

Most of the `layout.html` page was created by the CS50 team for the Finance project. I have changed it to reflect the needs of the SCUBA Log app. I have also added a footer to provide credit to the CS50 Finance project to anyone that visits the site.

### `login.html`

The form follows a clean and simple design, aligning with the overall layout defined in `layout.html`. Users can enter their credentials and submit the form to log in. The autofocus attribute ensures that the username field is focused when the page loads, providing a smooth user experience. The form action directs the submission to the `/login` route in the Flask application.

#### Credit

The entire `login.html` page was written by the CS50 team for the Finance project.

### `register.html`

Users can enter their desired username, password, and confirm the password before submitting the form for registration. The autofocus attribute ensures that the username field is focused when the page loads, providing a smooth user experience. The form action directs the submission to the `/register` route in the Flask application.

#### Credit

The entire `register.html` page was written by the CS50 team for the Finance project.

### `travel.html`

This file serves as the HTML template for the destination Log page in the SCUBA log Flask application. It extends the "layout.html" template for a consistent page structure. The page begins with a heading "Destinations" and includes a table displaying destination log entries. The table has columns for Name, Date, and Notes. Using a loop, it dynamically populates the table rows with destination details retrieved from the database.

Like the gear log, this page puts both the log itself and the input of the log on the same page.

Below the table, there's a form for adding new destination entries. Each input field is appropriately labeled and formatted, including date and text input types. Users can enter information about their travels and submit the form to add a new log entry.

Overall, this HTML template provides a structured and user-friendly interface for viewing and managing travel data in the SCUBA log application.
