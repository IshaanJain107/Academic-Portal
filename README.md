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
  <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/ab88e6bc-8ed0-4092-9305-2f02888eddae"></image>
</li>
<li>
All the functions are performed either via the objects of the class or via the pandas Data-frame.
The code also uses the ‘re’ (Regular Expression) module for checking the validity of the Email-ID as the User-ID.
'os' module is used to redirect from one py file to another.
</li>
</ul>
<br>
<h2>Assumptions</h2>
<ul>
  <li>The user cannot create an account with any of the fields empty. He/she is expected to fill these details duly.</li>
  <li>The user cannot change the User-ID and Password as these are the basic fields used for the authentication of the user.</li>
  <li>Although an option for ‘Forget Password’ has been created on the Log-in page, it is not functioning as we currently do not have any source of sending one-time password (OTP) for verification. So, it is expected of the user to remember his/ her log-in credentials.</li>
  <li>On three or more unsuccessful attempts, the user’s account will be temporarily deactivated. Currently, no provision for reactivation has been created due to lack of verification sources.</li>
</ul>
<h2>GUI</h2>
<ul>
  <li>
    The loading screen.
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/fb8afc94-4cea-436a-9097-b2a98110b21c"></image>
  </li>
  <li>
    After loading to 100%, this screen redirects to the login screen.
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/1cd67031-90d6-4e52-904b-9b91774aa857"></image>
  </li>
  <li>
    On clicking Sign-up button, it switches to Sign-up page
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/abe9d535-eed4-428e-af73-47adc2cada16"></image>
  </li>
  <li>
    Various warning based on incorrect user-id and password while Log-in:
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/c8019fcb-2f9c-4c52-b375-e71b9fb782eb"></image>
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/5a6cf203-9dee-406f-a179-c2877a1b81d6"></image>
<image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/6a6524f5-6ffb-4e39-88d2-d0a743b8f61a"></image>
  </li>
  <li>
    Forget password window
<image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/626e8c46-4086-46c1-bf95-17994d472b8f"></image>
  </li>
  <li>
    Show password functionality:
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/e8f0c6f4-1afa-442d-b6c5-c4e0933da0f8)"></image>
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/7d154c2f-d990-4145-a6da-b45656e7a879"></image>
  </li>
  <li>
    Dynamic Error detection while typing email-id and password on Sign-up Page
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/81db9df2-af73-457f-a1fb-5f98731b5a90"></image>
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/2b7e44a3-0f26-423c-839f-0db299931ad8"></image>
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/66d4dddd-5734-4b76-9a44-46445edfa9eb"></image>
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/dd9051f1-93ff-4feb-ab0e-bfbb907401fa"></image>
  </li>
  <li>
    Dashborad Welcome Page with dynamic side menu which opens on hovering cursor over it
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/f740faee-f322-4704-ab60-aed6ad649632"></image>
  </li>
  <li>
    Profile page with edit option
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/15376c9f-564d-4252-9c7e-8673a3766091"></image>
  </li>
  <li>
    Deregistration page
    <image src="https://github.com/IshaanJain107/Academic-Portal/assets/118128699/df69aa20-1537-4f5b-aac0-9282b85ef7f3"></image>
  </li>
</ul>

