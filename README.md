# Academic-Portal
A Python-based Academic Dashboard designed using Tkinter.<br>
<br>
<h2>Project description:</h2>
This project is about creating a functional academic portal, that allows users to:<br>
<ul>
<li>Sign In to their accounts</li>
<li>Sign Up and create a new account</li>
<li>View their user profile with their academic information</li>
<li>Edit the information in their profile</li>
<li>Submit a deregistration request to delete their account</li>
</ul>

<h2>Features:</h2>
<ul>
<li>For the back-end part, the python programming language has been used.
The pandas library has been used for proper management and structured 
storage of data. Three separate csv files are used, one for each type of user, 
namely teacher, UG student and PG student. A list of data frames named as 
‘dataBase’ is used to access the csv files. </li>
<li>Object Oriented Programming (OOP) features like inheritance, data-encapsulation, etc. have been exploited to improve the readability, understandability and functionality of the program.</li>
<li>A ‘temp.txt’ file is used as temporary storage required for the transfer of data 
from one .py file to another.</li>
<li>For the front-end and GUI part, the Tkinter library along with PIL (Python Image 
Library) were used. The GUI includes progress-bar based loading screen, 
dynamic menu, etc.</li>
<li>The ‘main.py’ file contains the front-end code for the loading screen of the 
program, created using progress bar from tkinter.ttk, and directs the program to 
the ‘LoginAndRegistrationPage.py’ file.</li>
<li>The ‘LoginAndRegistrationPage.py’ file includes the required code for the log-in 
and sign-up pages, which on proper authentication of the user directs to the 
‘Dashboard.py’ file.</li>
<li>The ‘Dashboard.py’ file contains the user dashboard code which provides 
options to update/edit the user’s profile, deregister from the portal, log-out, etc.</li>
<li>The ‘Dashboard.py’ file contains the required classes, which follow the following 
inheritance hierarchy relations:
  ![image](https://github.com/IshaanJain107/Academic-Portal/assets/118128699/ab88e6bc-8ed0-4092-9305-2f02888eddae)

</li>
</ul>
<br>

