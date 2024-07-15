
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
This section outlines the various features of the MoneyTree application. **If using the demo user, data has been entered from mid 2023 to May 2024**

### Home Page
The home page contains content for users who do not have an account. All features of the application can only be used if a user has an account. The page uses images to show the various features of the app with a short explanation of the feature. The features detailed include: the monthly spending chart, the spending category Pie chart, the daily spending stacked bar chart and the adding, updating and deleting of expenditures.

### Account Registration
MoneyTree requires the creation of an account to access the platform's features. For the CodeInstitute examiner, login credentials for a demo user will be provided. The handling of accounts is done through the Django Allauth package. 

#### Security
The backend logic checks the login state of all requests which connect to the database. If a user is not logged in and tries to navigate to any of the URLs which query the database, they are returned to the home page before any other logic is carried out.


### Dashboards
All dashboards can be accessed using the 'Dashboard' navigation link once a user is logged in. At the top of the dashboard, a user can choose a yearly dashboard by selecting the 'All' option from the month dropdown or a specific month to access the monthly dashboards. Months and years in the future are not available from the dropdown list and the selection of available months is determined by looking at the current date and the year that was selected. If a user attempts to navigate to a future month by specifying the year and month in the url, they will be redirected to the current month's dashboard.

The dashboard navigation link automatically navigates to the current month's dashboard when clicked by looking at the current date.

#### Year Dashboard
The yearly dashboard provides insights to a user's spending over an entire year. It features a line chart with the total expenditure for each month during the year, up to the present month. 

CHART IMAGE

At the top of the page is a ribbon showing the year and the total expenditure for that year so far.

Next to the line chart is a pie chart which shows the distribution of spending across the categories over the year.

PIE CHART

All charts are generated from a database view of the epxenditures. The SQL for the view can be found in the 0003 migrations file for the 'tracker' app. As such, the charts will automatically update when more data is added.


### Month Dashboard
The monthly dashboard shows the breakdown of spending for a given month. This is also where the managing of expenditure entries is done. 

#### Daily Spending Stacked Bar Chart
The monthly dashboard page features a stacked bar chart which shows the total expenditure for each day of the month and what categories made up that day of spending. When hovered over, each category in a bar will show its expenditure amount.

STACKED BAR

#### Monthly Pie Chart
Similar to the yearly dashboard, the monthly dashboard features a pie chart with the distribution of spending over the month across the different spending catgeories.

PIE CHART

#### Add Expenditures
The page features a simple form for a user to add an expenditure to. The 'amount' field supports up to 2 decimal places and there is logic which handles entires which do not fit this requirement. The 'reference' category is a text field where the user can enter anything they wish to identify what the expenditure was. The 'category' field is a dropdown list for every category that is defined. There is also a date picker for the date of the expenditure. For a better user experience, the user can enter any date of expenditure between 1st Jan 2023 and now rather than only allowing for entering data for the current month. Finally there is a button to add the expenditure and a button to cancel which clears the form.

ADD FORM

When submitted, the page will refresh and a message will show at the top of the page detailing whether the expenditure was successfully added or not. As the charts are based on a database view, they will update to show the new expedniture (if it was added in the selected month).

MESSAGE

#### View Expenditures
Below the add form is a button to show all expenditures for that month. This is a collapsable table. In the table the amount, reference, category and date are shown. The categories are colour coded to match the charts. There is also buttons to edit and delete any expenditure.

TABLE

#### Edit Expenditures
When a user clicks to edit a given transaction, the add form is populated with the data for that expenditure. The page will automatically focus on this form if it is off the screen. The 'add' button is changed to an 'update' button and 'cancel' will reset the form back to the 'add' form state. 

EDIT FORM

When a user submits an edit, the page will refresh and a message will be show at the top of the page showing whether the edit was successful. The charts will also show the newly edited data.

#### Delete Expenditures
When a user chooses to delete an expenditure, a modal will appear with a confirmation message asking if they are sure they want to delete the expenditure. If the choose to do so, the expenditure will be permenantly deleted and the page refreshed. A message will appear detailing if the expenditure was successfully deleted.

DELETE MODAL

## Testing
### Manual Testing
The following tests were done maually to ensure the application is functioning as expected:
#### Attempted access to a dashboard when not logged in
This test involved a non-logged in user entering a URL for a dashboard page. The result was the user being redirected back to the home page
#### Attempted access to raw data
This test involved a non-logged in user attempting to see JSON data used to populate the charts of the dashboard by manually entering the URL. The result was the user being redirected back to the home page
#### Attempted navigation to a dashboard in the future
This test involved a user attempting to navigate to a monthly and yearly dashboard which is in the future. The result of this test was the user being redirected to the current month/year's dashboard.

### Automated Testing


## Code Validation
### HTML

### CSS
The CSS code passed the W3C validator with no errors

### Javascript
The only errors were the use of the 'Chart' type. This is handled by the ChartJS CDN so can be ignored. The only other messages were warnings from using const, let and arrow functions (e.g. "'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).")

## Problems encountered
- There was an issue with setting up the db view for daily spending. The view required a change so the migration was rolled back. However, when running the migration again, django did not run the migration to recreate the view as it thought it was already implemented. Checking the migrations table in the db it believed the migration had been run but the view did not exist. After deleting the migration from the db table and re-running the migrations it errored saying that the object it was trying to create (the view) already existed, despite it not existing on the db. To resolve this, I abandoned that model and made a new view with the same logic but a different name.
- The next view issue encountered was where using django's ORM to query the model which the view was the db_table for never returned any objects. There was data in the view in the db but for whatever reason, no data was ever returned. As a result, I created a second model not attached to any db table where I could run raw SQL statements and this returned the data in the view.
- I originally intended for the 'Add expenditure' form to be a collapsable like the expenditure table. However, I encountered a limitation of using a button to do this. The intention was to expand the form when the 'edit' button was clicked. In Javascript I would call the collapse.show() method which should only show the collapsable and not collapse it if it is already showing. However this was not occurring. When debugging, the event listener on the 'edit' button did not look at the current state of the page and so always thought the form was collapsed and would call the show() method which closed the form (I am unsure why show() would ever close a collapsable). To avoid this, the collapsable was abandoned for the form.
- A few days before due date, the postgres server which hosts the database for this project was not allowing any new connections. This lead to a delay in development of the project. In the future, hosting my own postgres server would allow more control over issues that arise.
- After the above issue was resolved, I could no longer connect to the database using pgAdmin. The connection would always timeout. As the deadline was approaching, data for the demo user was not entered for all months of the year. Therefore, to see the application with a wide variety of data for the demo user, months between 2023-08 and 2024-05 should be selected.

## Future Features
- Add multiple expenditures at a time - This is the main feature I would like to add. It would be a better user experience if more than one expedniture could be added at once by having an 'add another' button which duplicates the form, enabling multiple expenditures to be added at once.
- User cutomsiable categories - Another feature would be to give users the default categories and then allow them to change the category names and colours if they choose.
- Direction of transaction - The db model is called 'transaction' rather than 'expenditure' to allow for a field on the model 'Direction' to eventually be added. This could dictate inflows as well as outflows so the app could also offer revenue streams as well as expedniture tracking. This could be one step to becoming a financial hub as opposed to just a spending tracker to a user.
- Automatic category assignment - It would be nice to store some strings for each user and category for the references. If a user inputs a refernce, the app could recognise this input and automatically assign a category to it.
- Upload of csv input - Banks allow statements to be downloaded in a csv format. If a user could upload this and the 'add' forms automatically generated with automatic category assignment, this could save lots of time inputting data manually.
- Use of bank APIs - Some banks offer APIs which a user with an account for that bank can use to see their transaction history. If multiple banks offer this, then a feature far down the road could utilise these for a user to automatically sync their data as opposed to relying on manual user input.