
# MoneyTree Spending Tracker
MoneyTree is a website where users can create an account and then record their expenditures. From this, MoneyTree will store this information in a database and generate charts from the data for the user to get insights from. This information can be used to identify to the user any areas which they are spending too much on and should cut back, or gaining an undertsanding as to where their money goes over the months. They could also use this information for seeing seasonal changes in their spending and being able to effectively budget for this.

The live site can be found at https://moneytree-spending-tracker-da63cdf02d44.herokuapp.com/

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

## Acknowledgements
All code which has been adapted from online sources has been commented with a link to the original source in each file.
- Using Javascript to retrive data from a url and use in a chart: https://testdriven.io/blog/django-charts/
- Replacing the save() method when not using a ModelForm: https://stackoverflow.com/questions/16443029/cant-save-a-form-in-django-object-has-no-attribute-save
- Generating dates in psql: https://stackoverflow.com/questions/58769145/postgresql-with-recursive
- Setting up the django project and installing needed packages was done by following the 'I think therefore I Blog' walkthrough project from Code Institute.

## Planning
Before development, planning of the look of the application and the structure of its database was done to streamline development.

### Front End Plan
Below is a simple wireframe which was created as a concept for the look of the main page the user would use: The dashboard.

![wireframe](https://github.com/12kharris/spending-tracker/blob/50f67b6f41e99c567d8435cd7807ef7ae9e17108/README-Images/wireframe.png?raw=true)

### Database
Below is an entity relationship diagram for how the database structure would look.

![ERD](https://github.com/12kharris/spending-tracker/blob/0d8ad3401e0003ee0786c04de8c6d12e1b3239a8/README-Images/ERD.png?raw=true)

### User Stories
Below is a link to the Trello board which was used to list all development tasks which were identified for this project.

https://trello.com/invite/b/lvzdh0BT/ATTI89fdb6d4cc73046678d01061a96ba7c0896AC760/moneytree-kanban-board

Trello offers more functionality than GitHub projects but the tasks were copied over to GitHub projects in case the reader does not wish to create a Trello account. The GitHub project board can be found here: https://github.com/users/12kharris/projects/2/views/1

## Models
Three models are used in the backend. These are the Category model, the Transaction model and the Transactions_by_Day model. The category model is responsible for the categories which a transaction can have. The Transaction model is the model which conatins all information about a transaction (or expenditure). It contains the amount, category (foreign key to Category model), a reference and the date of the transaction. Finally, the Transactions_by_Day model is an unmanaged model. It is a view which aggregates the different category's expenditures for every day of the year. This is the primary model which is used for the charts on the dashboard.


## Features
This section outlines the various features of the MoneyTree application. 

### Home Page
The home page contains content for users who do not have an account. All features of the application can only be used if a user has an account. The page uses images to show the various features of the app with a short explanation of the feature. The features detailed include: the monthly spending chart, the spending category Pie chart, the daily spending stacked bar chart and the adding, updating and deleting of expenditures.

![home 1](https://github.com/12kharris/spending-tracker/blob/50f67b6f41e99c567d8435cd7807ef7ae9e17108/README-Images/home%201.png?raw=true)

![home 2](https://github.com/12kharris/spending-tracker/blob/50f67b6f41e99c567d8435cd7807ef7ae9e17108/README-Images/home%202.png?raw=true)

### Account Registration
MoneyTree requires the creation of an account to access the platform's features. For the CodeInstitute examiner, login credentials for a demo user will be provided. The handling of accounts is done through the Django Allauth package. 

![sign up](https://github.com/12kharris/spending-tracker/blob/256a6701ea2c0d198b196c963752557c5fa344d9/README-Images/register.png?raw=true)

![sign in](https://github.com/12kharris/spending-tracker/blob/7b32e836e33316b211adacd1ac4a09bd552537a8/README-Images/sign%20in.png?raw=true)

![sign out](https://github.com/12kharris/spending-tracker/blob/7b32e836e33316b211adacd1ac4a09bd552537a8/README-Images/sign%20out.png?raw=true)

#### Security
The backend logic checks the login state of all requests which connect to the database. If a user is not logged in and tries to navigate to any of the URLs which query the database, they are returned to the home page before any other logic is carried out.


### Dashboards
All dashboards can be accessed using the 'Dashboard' navigation link once a user is logged in. At the top of the dashboard, a user can choose a yearly dashboard by selecting the 'All' option from the month dropdown or a specific month to access the monthly dashboards. Months and years in the future are not available from the dropdown list and the selection of available months is determined by looking at the current date and the year that was selected. If a user attempts to navigate to a future month by specifying the year and month in the url, they will be redirected to the current month's dashboard.

The dashboard navigation link automatically navigates to the current month's dashboard when clicked by looking at the current date.

#### Year Dashboard
The yearly dashboard provides insights to a user's spending over an entire year. It features a line chart with the total expenditure for each month during the year, up to the present month. 

![line chart](https://github.com/12kharris/spending-tracker/blob/9534814b15b82f949504200cbc8fbbf82debaf5a/README-Images/line%20chart.png?raw=true)

At the top of the page is a ribbon showing the year and the total expenditure for that year so far.

![ribbon](https://github.com/12kharris/spending-tracker/blob/ba246c61b377a7f01a271d5a1d886e30d6edf78c/README-Images/ribbon.png?raw=true)

Next to the line chart is a pie chart which shows the distribution of spending across the categories over the year.

![year pie](https://github.com/12kharris/spending-tracker/blob/c0d5378202b205fb92540550f3ccbf4032a1eefa/README-Images/yearly%20pie.png?raw=true)

All charts are generated from a database view of the epxenditures. The SQL for the view can be found in the 0003 migrations file for the 'tracker' app. As such, the charts will automatically update when more data is added.


### Month Dashboard
The monthly dashboard shows the breakdown of spending for a given month. This is also where the managing of expenditure entries is done. 

#### Daily Spending Stacked Bar Chart
The monthly dashboard page features a stacked bar chart which shows the total expenditure for each day of the month and what categories made up that day of spending. When hovered over, each category in a bar will show its expenditure amount.

![stacked bar](https://github.com/12kharris/spending-tracker/blob/c0d5378202b205fb92540550f3ccbf4032a1eefa/README-Images/daily-chart.png?raw=true)

#### Monthly Pie Chart
Similar to the yearly dashboard, the monthly dashboard features a pie chart with the distribution of spending over the month across the different spending catgeories.

![month pie](https://github.com/12kharris/spending-tracker/blob/1d6a2d597942079fa5d97266715fda04d48c970f/README-Images/month-pie.png?raw=true)

#### Add Expenditures
The page features a simple form for a user to add an expenditure to. The 'amount' field supports up to 2 decimal places and there is logic which handles entires which do not fit this requirement. The 'reference' category is a text field where the user can enter anything they wish to identify what the expenditure was. The 'category' field is a dropdown list for every category that is defined. There is also a date picker for the date of the expenditure. For a better user experience, the user can enter any date of expenditure between 1st Jan 2023 and now rather than only allowing for entering data for the current month. Finally there is a button to add the expenditure and a button to cancel which clears the form.

![add form](https://github.com/12kharris/spending-tracker/blob/3f120376857d89f35086c214613211592035b964/README-Images/add.png?raw=true)

When submitted, the page will refresh and a message will show at the top of the page detailing whether the expenditure was successfully added or not. As the charts are based on a database view, they will update to show the new expedniture (if it was added in the selected month).

![add message](https://github.com/12kharris/spending-tracker/blob/4170087f69dfbacfe94f32d38f501e7477419a3e/README-Images/add%20message.png?raw=true)

#### View Expenditures
Below the add form is a button to show all expenditures for that month. This is a collapsable table. In the table the amount, reference, category and date are shown. The categories are colour coded to match the charts. There is also buttons to edit and delete any expenditure.

![table](https://github.com/12kharris/spending-tracker/blob/4170087f69dfbacfe94f32d38f501e7477419a3e/README-Images/transaction%20table.png?raw=true)

#### Edit Expenditures
When a user clicks to edit a given transaction, the add form is populated with the data for that expenditure. The page will automatically focus on this form if it is off the screen. The 'add' button is changed to an 'update' button and 'cancel' will reset the form back to the 'add' form state. 

![edit form](https://github.com/12kharris/spending-tracker/blob/3f120376857d89f35086c214613211592035b964/README-Images/update.png?raw=true)

When a user submits an edit, the page will refresh and a message will be show at the top of the page showing whether the edit was successful. The charts will also show the newly edited data.

#### Delete Expenditures
When a user chooses to delete an expenditure, a modal will appear with a confirmation message asking if they are sure they want to delete the expenditure. If the choose to do so, the expenditure will be permenantly deleted and the page refreshed. A message will appear detailing if the expenditure was successfully deleted.

![modal](https://github.com/12kharris/spending-tracker/blob/57a0bd857e616babcce8dd46996d0ed4e4dff1bb/README-Images/modal.png?raw=true)

## Testing
### Python Manual Testing
The following tests were done maually to ensure the backend of the application is functioning as expected:
#### Attempted access to a dashboard when not logged in
This test involved a non-logged in user entering a URL for a dashboard page. The result was the user being redirected back to the home page which is a PASS.
#### Attempted access to raw data when not logged in
This test involved a non-logged in user attempting to see JSON data used to populate the charts of the dashboard by manually entering the URL. The result was the user being redirected back to the home page which is a PASS.
#### Attempted navigation to a dashboard in the future
This test involved a user attempting to navigate to a monthly and yearly dashboard which is in the future by manually entering a url containing a future date. The result of this test was the user being redirected to the current month/year's dashboard which is a PASS.

### Python Automated Testing
The automated tests that were run are contained in the tests.py file. The tests are as follows:
#### Added transaction displays on monthly dashboard page
A test transaction was created and a test conducted to see if it appeard on the monthly dashboard page. The result was a pass.
#### Test form POST data can successfully create a new transaction
POST data which is created from submitting the 'add transaction' form was made and used in the get_month_dashboard view function. The POST data successfully created a new transaction and the success message was saved which is a PASS.
#### Test an attempt to add a transaction with a blank date
POST data which is created from submitting the 'add transaction' form was made and used in the get_month_dashboard view function. This POST data had an empty date. The result from this test was the page still returning but the error message being present in the response.content which is a PASS.

### Javascript Manual Testing
The Javascript interactivity of the website was tested manually
#### Dashboard month restrictions
The dashboard month form should not allow for furutre months to be selected. To test this, the year of the form was changed and the month options in the month input were inspected. For 2024 (as of July 2024), the month options were 'All', 1, 2, 3, 4, 5, 6 and 7 which is as expected. For 2023, months 'All' and 1-12 were present which is expected as this is in the past. The page was refreshed for a 2023 month and the months were still ass expected which is a PASS.
#### Dashboard chart updates
The dashboard charts should update to show the current data in the database. To test this, a new transaction was added with the 'add transaction' form on a day with no data. The page automatically refreshes and the new transaction can be seen in the dashboard charts. This is a PASS.
#### Dashboard messages should automatically disappear
When a message appears at the top of the dashboard, it should automatically clear after 10 seconds. To test this, a transaction was updated which creates a message at the top of the dashboard page. After 10 seconds, the message disappeares which is a PASS.
#### Edit button should add the transaction content to the form
When the 'edit' button is pressed, the content of the transaction form should be populated with the content of the existing transaction. To test this, a transaction from every category was updated. Each time the edit button was clicked, the add form was siccessfully updated with the content from the transaction which is a PASS.
#### Dashboard page should focus on 'add' form when 'edit' is pressed
When a user has scrolled and the 'add' form is off the page and 'edit' is pressed, the page should scroll to the 'add' form for a good user experience. To test this, the page was scrolled so the form was off the page and 'edit' was pressed. The result of this test was a PASS as the page automatically scrolled to the 'add' form.
#### Cancel button should clear the 'add' form
When a user clicks the 'cancel' button, the add form should be reset back to clear and if applicable, the 'update' button should return to an 'add' button. To test this, the form was filled out and the cancel button pressed. In this case the test PASSed as the form was reset. Additionally, an 'edit' button was pressed which filled in the form and changed the 'add' button to an 'update' button. The cancel button was then clicked and the form was reset and the 'update' button was changed back to an 'add' button. The form was then filled out and the 'add' button pressed and the transaction was successfully added which is a PASS.

### Responsive Testing
The various pages were viewed using the chrome dev tools for various sized devices. Below are the monthly dasboard pages for large, medium and small screens respectively.
![large](https://github.com/12kharris/spending-tracker/blob/86ee5d6e087b83a9a2616233ad7057e01138315d/README-Images/lg.png?raw=true)
![medium](https://github.com/12kharris/spending-tracker/blob/86ee5d6e087b83a9a2616233ad7057e01138315d/README-Images/md.png?raw=true)
![small](https://github.com/12kharris/spending-tracker/blob/86ee5d6e087b83a9a2616233ad7057e01138315d/README-Images/sm.png?raw=true)

## Deployment
 
The package whitenoise was used to handle static files in deployment. The website was deployed using Heroku. The deployment steps are as follows
- Run python3 manage.py collectstatic to collect all static files and store them in the staticfiles directory for whitenoise
install gunicorn
- Add a procfile with a command of web: gunicorn moneytree.wsgi in it.
- Set Debug to False
- Git commit and push
- On Heroku, include the following config vars: DATABASE_URL and SECRET_KEY with their respective values.
- Deploy the branch

## Code Validation
### HTML
Using W3C, all pages had no errors from my custome HTML. The only errors are from HTML loaded with the font-awesome scripts at the bottom of the page.

![HTML valid](https://github.com/12kharris/spending-tracker/blob/57a0bd857e616babcce8dd46996d0ed4e4dff1bb/README-Images/HTML%20validation.png?raw=true)
The above error is from a font awesome script

### CSS
The CSS code passed the W3C validator with no errors

![CSS](https://github.com/12kharris/spending-tracker/blob/1214f256926ac517fba5a90b85029af673d6ba5b/README-Images/CSS.png?raw=true)

### Javascript
Using JSHint, the only errors were the use of the 'Chart' type. This is handled by the ChartJS CDN so can be ignored. The only other messages were warnings from using const, let and arrow functions (e.g. "'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).")

![JS hint](https://github.com/12kharris/spending-tracker/blob/8e493b0398ae98f886329a126d357e6bc90aea01/README-Images/JS%20hint.png?raw=true)
The above is an example of the JS hint output. All of the js files shared these warnings.

### Python

All python files I have modified and their PEP8 validation results are shown below
#### charts.py
![charts pep8](https://github.com/12kharris/spending-tracker/blob/8e493b0398ae98f886329a126d357e6bc90aea01/README-Images/charts%20pep8.png?raw=true)

#### forms.py
![forms pep8](https://github.com/12kharris/spending-tracker/blob/8e493b0398ae98f886329a126d357e6bc90aea01/README-Images/forms%20pep8.png?raw=true)

#### models.py
![models pep8](https://github.com/12kharris/spending-tracker/blob/8e493b0398ae98f886329a126d357e6bc90aea01/README-Images/models%20pep8.png?raw=true)

#### urls.py
![urls pep8](https://github.com/12kharris/spending-tracker/blob/8e493b0398ae98f886329a126d357e6bc90aea01/README-Images/urls%20pep8.png?raw=true)

#### views.py
The only errors for views.py were for import statements. No matter which order I wrote the import statements, these errors would persist.
![views pep8](https://github.com/12kharris/spending-tracker/blob/8e493b0398ae98f886329a126d357e6bc90aea01/README-Images/views%20pep8.png?raw=true)


## Known Issues
The only known issue is when a transcation is added/edited/modified, the monthly total at the top of the page will not update. However, when the page is refreshed, the values updates to reflect the previous change. I'm not sure why this might be. 


## Problems encountered
- There was an issue with setting up the db view for daily spending. The view required a change so the migration was rolled back. However, when running the migration again, django did not run the migration to recreate the view as it thought it was already implemented. Checking the migrations table in the db it believed the migration had been run but the view did not exist. After deleting the migration from the db table and re-running the migrations it errored saying that the object it was trying to create (the view) already existed, despite it not existing on the db. To resolve this, I abandoned that model and made a new view with the same logic but a different name.
- The next view issue encountered was where using django's ORM to query the model which the view was the db_table for never returned any objects. There was data in the view in the db but for whatever reason, no data was ever returned. As a result, I created a second model not attached to any db table where I could run raw SQL statements and this returned the data in the view.
- I originally intended for the 'Add expenditure' form to be a collapsable like the expenditure table. However, I encountered a limitation of using a button to do this. The intention was to expand the form when the 'edit' button was clicked. In Javascript I would call the collapse.show() method which should only show the collapsable and not collapse it if it is already showing. However this was not occurring. When debugging, the event listener on the 'edit' button did not look at the current state of the page and so always thought the form was collapsed and would call the show() method which closed the form (I am unsure why show() would ever close a collapsable). To avoid this, the collapsable was abandoned for the form.
- A few days before due date, the postgres server which hosts the database for this project was not allowing any new connections. This lead to a delay in development of the project. In the future, hosting my own postgres server would allow more control over issues that arise.
- I could not apply the migrations which creates the daily_transactions view for unit testing as it is a raw psql statement but the test sqlLite db does not use psql. As such, in the test environment the 0003 migration is not run.

## Future Features
Below are features which I would like to add to the application in the future.
- Add multiple expenditures at a time - This is the main feature I would like to add. It would be a better user experience if more than one expenditure could be added at once by having an 'add another' button which duplicates the form, enabling multiple expenditures to be added at once.
- User cutomsiable categories - Another feature would be to give users the default categories and then allow them to change the category names and colours if they choose.
- Direction of transaction - The db model is called 'transaction' rather than 'expenditure' to allow for a field on the model 'Direction' to eventually be added. This could dictate inflows as well as outflows so the app could also offer revenue streams as well as expedniture tracking. This could be one step to becoming a financial hub as opposed to just a spending tracker to a user.
- Automatic category assignment - It would be nice to store some strings for each user and category for the references. If a user inputs a refernce, the app could recognise this input and automatically assign a category to it.
- Upload of csv input - Banks allow statements to be downloaded in a csv format. If a user could upload this and the 'add' forms automatically generated with automatic category assignment, this could save lots of time inputting data manually.
- Use of bank APIs - Some banks offer APIs which a user with an account for that bank can use to see their transaction history. If multiple banks offer this, then a feature far down the road could utilise these for a user to automatically sync their data as opposed to relying on manual user input.