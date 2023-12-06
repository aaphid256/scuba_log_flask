# SCUBA Log
> This SCUBA Log project for cs50 is a Flask website that allows users to keep track of SCUBA related activity. Users are able to log into the website and log individual dives as well as their equipment and travel experience. This final project was an opportunity to develop my own software using the skills I learned in cs50.
[Video Introduction](https://www.youtube.com/watch?v=FoU-_yPjXz8)


## Requirements  (Prerequisites)
Tools and packages required to successfully install this project.
* Visual Studio Code (VSCode): [Install] (https://code.visualstudio.com/download)
* Python 3.3 and up [Install](https://www.python.org/downloads/) - Make sure to check the option to add Python to your system's PATH during installation.

## VSCode Extensions:
* [Python Extension for VSCode] - Install the "Python" extension by Microsoft from the VSCode Extensions marketplace. This extension provides Python language support and debugging capabilities.
* [HTML/CSS Support] - If you're working with HTML, you may want to install an extension like "HTML CSS Support" for better HTML and CSS language support.


## Installation
Log into [cs50.dev](cs50.dev), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:
`$`

Next download the project.zip file from the [Gradescope page](https://www.gradescope.com/courses/564772) and add it to your codespace.

Then execute

`unzip project.zip`

to create a folder called `project`. You no longer need the ZIP file, so you can execute

`rm project.zip`

and respond with "y" followed by Enter at the prompt to remove the ZIP file you downloaded.

Now type

`cd project`

followed by Enter to move yourself into (i.e., open) that directory. Your prompt should now resemble the below.

`project/ $`

Execute `ls` by itself, and you should see a few files and folders:

`app.py helpers.py project.db readme.md requirements.tex static/ templates/`

If you run into any trouble, follow these same steps again and see if you can determine where you went wrong!

## Running

Start Flask's built-in web server (within `project/`):

`$ flask run`

Visit the URL outputted by `flask` to see the distribution code in action and use the website!

## Screenshots
Screenshots of the website that show the history in the log, the new dive form to add a log, the gear log, and the destination log.

![SCUBA Log](https://drive.google.com/file/d/12I5W0WQs053lfoGZLOrNGByFsPiciUsB/view?usp=sharing)


![Dive Form](https://drive.google.com/file/d/1amRknwHFyhr-HqHnb8c-ZJPMwPMvdDXa/view?usp=sharing)


![Gear Log](https://drive.google.com/file/d/1Mz0dXYygSp_7pvUz6VrJ_PaV1Pzpidwm/view?usp=sharing)


![Destinations Log](https://drive.google.com/file/d/1XhVYgD_L3xScT9wFN5XoT4YTzckBlT7r/view?usp=sharing)


## Usage example
### Dive Log
#### Log a New Dive

1. Navigate to the "Dive Log" section.
2. Fill in the dive details, such as dive number, date, location, etc.
3. Click "Add Log" to submit the entry.

#### View Dive History

1. Visit the "History" page to see a table of your dive logs.
2. Explore various dive details such as date, location, dive time, and more.

### Gear Log

#### Log New Gear

1. Access the "Gear Log" section.
2. Provide information about the type, brand, date purchased, etc.
3. Click "Submit" to add the gear to your log.

#### View Gear Inventory

1. Navigate to the "Gear Log" page to see a list of your gear items.
2. Check details like brand, condition, and last service date.

### Travel Log

#### Record Travel Destinations

1. Visit the "Travel" section.
2. Enter the destination, date, and any notes.
3. Click "Add" to include the travel entry.

#### Explore Travel History

1. Go to the "Travel" page to see a record of your travel destinations and notes.


## Tech Stack / Built With
1. [Python 3](https://www.python.org/download/releases/3.0/) - One of the programming languages used.

2. [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) - The markup language used to display info in the web browser.

3. [Visual Studio Code](https://code.visualstudio.com/) - The source-code editor that was used.


## Authors
Tony Warfield - tony.warfield86@gmail.com

I'm a student at Harvard Extension School concentrating in Computer Science. I'm planning on graduating Summer of 2025.

You can find me here:
[Github](https://github.com/aaphid256) and
[LinkedIn](https://www.linkedin.com/in/tonywarfieldta/)

## Credits
The [Final Project](https://cs50.harvard.edu/extension/2023/fall/project/) from CS50 class is what this project was created for. This link has all the expectations for the project.

Here's a list of other related projects, sites, and tutorials which helped me in creating this project:

- [Make a README](https://medium.com/@sagarganiga468/how-to-create-a-stunning-readme-md-edf1c74b6a46) - How to make a great README file.
- [Python](https://www.python.org) - For all my Python needs.
- [W3Schools](https://www.w3schools.com/) - For almost everything! I tend to google things every 2 minutes and they seem to answer the majority of my questions.
- [Stack Overflow](https://stackoverflow.com/) - For everything I can't find on W3Schools.
- [CS50 Finance](https://cs50.harvard.edu/extension/2023/fall/psets/9/finance/) - I used the skeleton of the Finance app that we built earlier in the term to build my final project. Please notice that the login/out and register are all taken directly from this source and was not written by me. I have also credited this in the footer of my site.
