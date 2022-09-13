### Install:

Run `pip install` to install all the dependencies in `requirements.txt` 

### Run the local Flask project:
`flask run`

### Heroku Deployment:
The json data output of the project can be viewed here: 
`https://octopus-backend-test.herokuapp.com/api`

### Notes:

I spent slighlty more than the alloted 4 hours as I ran into an unexpected issue with deploying to Heroku as they have discontinued support for Python version 3.9.6. (Usually this deployment process is very smooth). But, I was able to find a way around this issue in the end. 

By the end of the test time period I was able to get all the Premier League results for the 2020/21 season from the API and transform these results in a new trimmed down JSON data model. The results were then passed into a Flask view with a URL or endpoint which can be run locally or via the Heroku link above. 

I was also able to extract the NBA 2020/21 regular season results from the API provided in the same JSON model format. However I ran out of time to combine the two data sets and add the pagination feature. I have left the print statement for the NBA results in the code to demonstrate how this data is being passed into the Flask view.


