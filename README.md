<h1>Rudgeys Recruitment</h1>
<hr>
<p>
    Rudgeys Recruitment is a recruitment website for the Warrington area. The app is targeted for job seekers and for people looking to hire in the Warrington area, the app has a job board that advertises different types of jobs.
    In order to view the website please click on the link below......... <h1>(LINK PROJECT)</h1>
</p>

<h2>Table of Contents</h2>


<h2>Design</h2>
<p>
    The site has simple and clean colours, I use colours that wouldn’t be off putting for the user when reading the jobs or filling out the forms.
</p>
<h3>Colours</h3>
<p>These are the colours I used for the background</p>
![f5f5f5]{readme/F5F5F5.png}
<h3>Images</h3>
<p>I only used one image and that was for my logo that was created by using Shopify Logo Maker</p>
<p>The Poppins font is the main font of the website. Sans Serif is the backup font, in case for any reason the main font isn't being imported into the site correctly. These fonts were imported via Google Fonts.</p>
<h3>Wireframes</h3>
<ul>
    <li>
        Index.html
        <!--Add a phone wireframe-->
    </li>
    <li>
        Jobs.html
        <!--Add a phone wireframe-->
    </li>
    <li>
        Applying.html
    </li>
    <li>
        Advertising.html
    </li>
    <li>
        Hiring.html
    </li>
    <li>
        Contact.html
    </li>
    <li>
        SignUp.html
    </li>
    <li>
        Login.html
    </li>
    <li>
        Profile.html
    </li>
    <li>
        Forgotten Password.html
    </li>
</ul>
<h2>Agile</h2>
<p>
    I used the github projects to manage the app whilst using the Agile Method.
    I created 10 user stories with acceptable acceptance criteria to make it clear when the User Story has been completed. The acceptance criteria are further broken down into tasks in order to complete the user story.
    You can click <a href="https://github.com/users/JoshRudge22/projects/5/views/1">here</a> to view them.
</p>
<h2>Data Model</h2>
<ul>
    <li>ContactUsForm: Represents a form for users to contact the website. It includes fields for name, email, phone number, message, and preferred contact time.</li>
    <li>Hiring: Represents a hiring process or job application form. It includes fields for company name, email, phone number, job description, and documentation.</li>
    <li>Job: Represents a job listing or job posting. It includes fields for job title, job benefits, address, job details, job requirements, interview deadline, availability times, hire status, and notes.</li>
    <li>AvailableTime: Represents available times for job interviews. It includes fields for different time slots.</li>
    <li>Profile: Represents user profiles. It includes fields for user information such as email, phone number, CV (resume), address, post code, and notice times.</li>
    <li>NoticeTimes: Represents notice times for job applications. It includes fields for different notice periods.</li>
    <li>JobApplication: Represents job applications submitted by users. It includes a foreign key to the User model and possibly a reference to the Job model</li>
</ul>
<h2>Testing</h2>
<h2>User Authentication</h2>
<ul>
    <li>Django's LoginRequired is used to make sure that the user cannot apply for any jobs unless they have created an account.</li>
</ul>
<h2>Forms</h2>
<p>If the form is empty or incorrect the form will not be submitted. If an text box hasn't been filled but the user clicks submit the form doesn't get sent and the user is informed where the error is.</p>
<h2>Database</h2>
<p>The database url and secret key are stored in the env.py file to prevent unwanted connections to the database</p>
<h2>Error Pages</h2>
<p>Custom Error Pages were created to give the user more information on the error, in the middle of the page the user will see the home button and navbar to get them off the page</p>
<ul>
    <li>400.html
    </li>
    <li>403.html
    </li>
    <li>404.html
    </li>
    <li>500.html
    </li>
</ul>
<h2>Features</h2>
<h3>logo</h3>
<h3>Navbar</h3>
<h3>Footer</h3>
<h2>Index.html</h2>
<p>The index page just goes into detail about who the company is and the services they can provide wheather you are looking for a job or looking to hire someone in the Warrington area.</p>
<h2>Jobs.html</h2>
<p>In my jobs page I have created a job board, this shows 5 jobs per page and if the user sees a job they would like to apply they just need to click on the apply button which will take them to the new page.</p>
<h2>Applying.html</h2>
<p>After the user has clicked on the job they would like to apply for they are taken to this form. If the user has yet to log in they will be redirected to the login page where they will be asked to log in. Onve the user is logged in most of the form is filled, this is because when the user logs in we ask them to update their account with a cv, phone number, email ect. Once they are happy to submit the form the form then gets sent to an email address and the admin panel</p>
<h2>Advertising.html</h2>
<p>We then have our advertising page, this goes into a little bit more detail in how we can advertise roles. There is also an example of how we want the form to be filled out. Orginally I wanted to add a word document for the user to download and fill out but was unable to achive this. When the user clicks the Advertise y role button they will be redirected to another page.</p>
<h2>Hiring.html</h2>
<p>We have a form that the user can fill otu explaining who the company is, their contact details, explation of the job and if they have any attachments they may like to include. Once the user ahs filled this form they click submit where they will be redirected to another page advising the form has been submitted. The form then gets sent to an email and the admin panel.</p>
<h2>Contact.html</h2>
<p>Contact form is created encase the user has any qustion that haven't been answered or they would like more infomation. Once the form has been submmited it is sent to an email address and the admin panel.</p>
<h2>Signup.html</h2>
<p>Form for the user to fill in order to create their account. Once the account has been created they are then redirected to their account.</p>
<h2>Profile.html</h2>
<p>Once the user has signed up or logged in they are redirected to their account page where they can either add or edit theiir details. We take the information from this page and add this to our applying form to stop the user from having to re-enter their details when they apply for more than one job.</p>
<h2>Login.html</h2>
<p>Form for the user to fill in order to log into their account. Once the user has logged in they are then redirected to their account.</p>
<h2>Forgotten.html</h2>
<p></p>
<h2>Deploying to Heroku</h2>
<h3>Create the Heroku App</h3>
<ul>
    <li>Log in to Heroku or create an account.</li>
    <li>On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".</li>
    <li>Enter a unique and meaningful app name.</li>
    <li>Next select your region.</li>
    <li>Click on the Create App button</li>
</ul>
<h3>Create the Heroku App</h3>
<ul>
    <li>In your GitPod workspace, create an env.py file in the main directory.</li>
    <li>Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.</li>
    <li>Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.</li>
    <li>Comment out the default database configuration.</li>
    <li>Save files and make migrations.</li>
    <li>Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.</li>
    <li>Link the file to the templates directory in Heroku.</li>
    <li>Change the templates directory to TEMPLATES_DIR</li>
    <li>Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']</li>
</ul>
<h2>Files</h2>
<ul>
    <li>Create requirements.txt file</li>
    <li>Create three directories in the main directory; media, storage and templates.</li>
    <li>Create a file named "Procfile" in the main directory and add the following: web: gunicorn rr.wsgi</li>
</ul>
<h2>Heroku Config Vars</h2>
<ul>
    <li>DISABLE_COLLECTSTATIC</li>
    <li>DATABASE_URL</li>
    <li>SECRET_KEY</li>
</ul>
<h2>Deploying on Heroku</h2>
<ul>
    <li>Ensure in project settings, DEBUG is False</li>
    <li>Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.</li>
    <li>Scroll to the bottom of the deploy page and  click deploy branch</li>
    <li>Click View to view the deployed site.</li>
</ul>
<h2>Languages Used</h2>
<ul>
    <li>Python</li>
    <li>HTML</li>
    <li>CSS</li>
    <li>Javascript</li>
</ul>
<h2>Frameworks - Libraries - Programs Used</h2>
<ul>
    <li>Django: Main python framework used in the development of this project</li>
    <li>Django-allauth: authentication library used to create the user accounts</li>
    <li>ElephantSQL was used as the database for this project.</li>
    <li>Heroku - was used as the cloud based platform to deploy the site on.</li>
    <li>Lucidspark - Used to create wireframe images</li>
    <li>Used for icons in the footer.</li>
    <li>Google Fonts - Used to import and alter fonts on the page.</li>
    <li>Summernote: A WYSIWYG editor to allow users to edit their job adverts in the admin panel</li>
    <li>Bootstrap: CSS Framework for developing responsiveness and styling</li>
    <li>Hatchful: Used to generate custom logo and the favicon</li>
</ul>
<h2>Credits</h2>
<ul>
    <li>W3Schools</li>
    <li>Stack Overflow</li>
    <li>Bootstrap 4.6 Docs</li>
    <li>Django Docs</li>
    <li>Indeed: Used their job adverts in the Warrington Area</li>
    <li>Code Institute - Blog Walkthrough Project</li>
    <li>Antonio for his help and explaining the issues I didn't understand</li>
</ul>
