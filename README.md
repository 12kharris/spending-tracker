
# MoneyTree Spending Tracker
MoneyTree is a website where users can create an account and then record their expenditures. From this, MoneyTree will store this information in a database and generate charts from the data for the user to get insights from. This information can be used to identify to the user any areas which they are spending too much on and should cut back, or gaining an undertsanding as to where their money goes over the months. They could also use this information for seeing seasonal changes in their spending and being able to effectively budget for this.

Things to include
- mockups and diagrams from planning


## Technologies Used
The following technologies were used and their install commands listed next to them
- Django - For development framework: pip3 install Django~=4.2.1
- Gunicorn - For deployment running:  pip3 install gunicorn~=20.1
- Psycopg2 - For connecting to database: pip3 install dj-database-url~=0.5 psycopg2~=2.9
- Whitenoise - For static file collection in deployment: pip3 install whitenoise~=5.3.0
- Django Allauth - For account registration handling: pip3 install django-allauth~=0.57.0
- Django crispy forms - For simple form rendering whilst developing: pip3 install django-crispy-forms~=2.0 crispy-bootstrap5~=0.7
- Bootstrap 5.0 - For web page styling: CDN used
- ChartJS - For chart rendering: CDN used

## Languages Used
The following programming languages were used for this project
- HTML - For web page content structure
- CSS - For web page content styling
- Javascript - For web page interactivity and chart generation
- Python3 - For simple database querying, view routing and view generation. Python is the language used by the Django framework
- PSQL - For complex querying and database view creation


## Planning
Before development, planning of the look of the application and the structure of its database was done to streamline development.

### Front End Plan
Below is a simple wireframe which was created as a concept for the look of the main page the user would use: The dashboard.

WIREFRAME HERE

### Database
Below is an entity relationship diagram for how the first version of the database structure would look.

DIAGRAM HERE

### User Stories
Below is a link to the Trello board which was used to list all development tasks which were identified for this project.

https://trello.com/invite/b/lvzdh0BT/ATTI89fdb6d4cc73046678d01061a96ba7c0896AC760/moneytree-kanban-board

Trello offers more functionality than GitHub projects but the tasks were copied over to GitHub projects in case the reader does not wish to create a Trello account


## Features
This section outlines the various features of the MoneyTree application

### Home Page
The home page contains content for users who do not have an account. All features of the application can only be used if a user has an account. The page uses images to show the various features of the app with a short explanation of the feature. The features detailed include: the monthly spending chart, the spending category Pie chart, the daily spending stacked bar chart and the adding, updating and deleting of expenditures.

### Account Registration
MoneyTree requires the creation of an account to access the platform's features. For the CodeInstitute examiner, login credentials for a demo user will be provided. The handling of accounts is done through the Django Allauth package. 

#### Security
The backend logic checks the login state of all requests which connect to the database. If a user is not logged in and tries to navigate to any of the URLs which query the database, they are returned to the home page before any other logic is carried out.


### Dashboards
All dashboards can be accessed using the 'Dashboard' navigation link once a user is logged in. At the top of the dashboard, a user can choose a yearly dashboard by selecting the 'All' option from the month dropdown or a specific month to access the monthly dashboards.

The dashboard navigation link automatically navigates to the current month's dashboard when clicked by looking at the current date. 

#### Year Dashboard
The yearly dashboard shows provides insights to a user's spending over an entire year. 


### Month Dashboard
#### Add Expenditures
#### Edit Expenditures
#### Delete Expenditures


## Problems encountered
- There was an issue with setting up the db view for daily spending. The view required a change so the migration was rolled back. However, when running the migration again, django did not run the migration to recreate the view as it thought it was already implemented. Checking the migrations table in the db it believed the migration had been run but the view did not exist. After deleting the migration from the db table and re-running the migrations it errored saying that the object it was trying to create (the view) already existed, despite it not existing on the db. To resolve this, I abandoned that model and made a new view with the same logic but a different name.
- The next view issue encountered was where using django's ORM to query the model which the view was the db_table for never returned any objects. There was data in the view in the db but for whatever reason, no data was ever returned. As a result, I created a second model not attached to any db table where I could run raw SQL statements and this returned the data in the view.
- A few days before due date, the postgres server which hosts the database for this project was not allowing any new connections. This lead to a delay in development of the project. In the future, hosting my own postgres server would allow more control over issues that arise.
