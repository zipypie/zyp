Tools and application i've used in this project
Visual Studio Codesoftware application
MYSQL Workbench software application

PROGRAMMING LANGUAGE
python 
structured query language/SQL
git


INSTALL TO USE MY PROJECT
install python 
install flask
install erd editor extension on the vscode
install git 
install postman
install xampp


#Their USES
Python: Python is a programming language that is widely used for web development, data analysis, artificial intelligence, and more. It's known for its simplicity and readability.

Flask: Flask is a web framework for Python that makes it easy to build web applications. It provides tools and libraries to handle routing, request handling, and rendering templates, making web development more efficient.

ERD Editor Extension (Visual Studio Code): This extension allows you to create Entity-Relationship Diagrams (ERDs) within Visual Studio Code. ERDs are visual representations of database tables and their relationships, helping you design and understand the structure of a database.

Git: Git is a version control system that helps you manage and track changes to your code. It allows multiple developers to work on a project simultaneously, keeps track of different versions, and enables collaboration and code sharing.

Postman: Postman is an API development and testing tool. It simplifies the process of working with APIs by providing a user-friendly interface to send requests, view responses, and test API functionality. It's commonly used by developers to interact with and debug APIs.

XAMPP: XAMPP is a software package that includes a web server (Apache), a database server (MySQL), and a scripting language (PHP). It provides a local development environment for building and testing web applications before deploying them to a production server.







#TO INSTALL FLASK

Make sure you have Python installed on your system. You can check by opening a terminal or command prompt and running the following command:


python --version
If Python is not installed, you can download it from the official Python website (https://www.python.org) and follow the installation instructions for your operating system.

Once Python is installed, open a terminal or command prompt.

Create a new directory (optional) for your Flask project. You can skip this step if you want to install Flask globally.


mkdir myflaskproject
cd myflaskproject

It is recommended to create and activate a virtual environment to keep your project dependencies isolated. Run the following commands to create and activate a virtual environment (optional step):

For Windows:
python -m venv venv
venv\Scripts\activate
For macOS/Linux:

python3 -m venv venv
source venv/bin/activate

Now, with the virtual environment activated (if you chose to use one), run the following command to install Flask:


pip install flask
This command will install Flask and its dependencies.

Once the installation is complete, you can start building Flask applications.



#TO INSTALL FLASK-MYSQLDB
Install MySQL Server:

Download and install MySQL Server from the official website: https://dev.mysql.com/downloads/mysql/
Follow the installation instructions for your operating system.
Install the Flask-MySQLdb package:

Open a command prompt or terminal.
Run the following command to install Flask-MySQLdb:
pip install flask-mysqldb
Set up the MySQL connection in Flask:

Open your Flask application code.

Import the necessary modules:

python
from flask import Flask
from flask_mysqldb import MySQL





#TO INSTALL NeoVim
Open PowerShell or Command Prompt as an administrator.

If you don't have Chocolatey installed, run the following command to install Chocolatey:

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))


After Chocolatey is installed, run the following command to install Neovim:


choco install neovim

Chocolatey will download and install Neovim along with its dependencies. Follow the prompts during the installation process.

Once the installation is complete, you can launch Neovim by opening a new PowerShell or Command Prompt window and typing nvim.





#TO INSTALL XAMPP
this provides a local server environment for web development

Visit the Apache Friends website at https://www.apachefriends.org/index.html.

On the Apache Friends website, locate the XAMPP section and click on the "Download" button.

You'll be directed to the download page. Select the appropriate version of XAMPP for your operating system (Windows, macOS, or Linux) and click on the download link.

Once the download is complete, locate the downloaded file and run the installer.

On the Windows platform, the installer will guide you through the installation process. Follow the on-screen instructions, and you can choose the components you want to install (e.g., Apache, MySQL, PHP, etc.). By default, all components are selected, but you can customize the installation according to your requirements.

Select the installation directory where you want to install XAMPP. The default directory is usually suitable, but you can choose a different location if desired.

Continue with the installation process, and once it completes, you'll have XAMPP installed on your system.

To start XAMPP, run the XAMPP Control Panel (which is usually installed along with XAMPP). You can find it in the installation directory or through the Start menu (on Windows).

In the XAMPP Control Panel, you'll see various modules such as Apache, MySQL, PHP, etc. Click on the "Start" button next to the modules you want to activate. By default, Apache and MySQL are started.

Once the modules are running, you can access the XAMPP server by opening a web browser and navigating to http://localhost or http://127.0.0.1.


but there are some needed to change on the file of the mysql where you need to delete some files inorder for us to use the xampp file











#TO INSTALL CURL
To install curl in PowerShell on Windows, you can follow these steps:

Open PowerShell by typing "PowerShell" in the Windows search bar and selecting the "Windows PowerShell" or "PowerShell" app.

To check if curl is already installed, run the following command:


curl --version
If curl is already installed, you will see the version information. If not, you will see an error indicating that the command is not recognized.

To install curl in PowerShell, you can use the Invoke-WebRequest cmdlet to download the curl executable from the official curl website. Run the following command:


Invoke-WebRequest -Uri https://curl.se/windows/dl-<version>/curl-<version>-win64-mingw.zip -OutFile curl.zip
Replace <version> with the desired version number. For example, to download curl version 7.78.0, the command would be:


Invoke-WebRequest -Uri https://curl.se/windows/dl-7.78.0/curl-7.78.0-win64-mingw.zip -OutFile curl.zip
Once the download is complete, extract the contents of the zip file by running the following command:


Expand-Archive -Path curl.zip -DestinationPath C:\Path\To\Extract
Replace C:\Path\To\Extract with the desired directory where you want to extract curl.

Add the directory containing the curl executable to the system's PATH environment variable. Run the following command:


$env:Path += ";C:\Path\To\Extract"
Replace C:\Path\To\Extract with the actual path where you extracted curl.

Verify the installation by running the following command:


curl --version
You should now see the version information for curl.

That's it! You have installed curl in PowerShell on Windows. You can now use the curl command to make HTTP requests directly from PowerShell.
