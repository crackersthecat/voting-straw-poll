# voting-straw-poll

## Time taken
I spent an extra hour on top of the 4 allocated hours. After 4 hours I had not got the results by constituency view working correctly. I did a git commit at that time so you can see how far I got.

I then spent an extra 30 minutes getting the constituency view working, and another 30 minutes adding basic styling with less. There are git commits for each of these times.

## Notes
I have set this up as a development environment only, so I am using sqlite.

I used django 1.7, python 2.7.9 and the django compressor - requirements are stored in requirements.txt

You need to create a few test constituencies and parties in the admin interface before you can vote.

## To dos
There are a lot more things which I would like to have done. This is the first time that I have written a Django application from scratch, as opposed to edit one that someone else has already set up. As such just getting the basics right took all of my time.

### Write tests
Write some tests to validate the system. For example checking that the total number of yes votes tallies with the totals for the parties

### Refactor repeated code
I'm aware that there is quite a lot of repeated code to get constituencies etc - move some of these into a context processor or look at using methods in models.py

### Create initial data for constituencies
I had planned to use the TheyWorkForYou API to get a list of parliamentary constituencies and use a data migration to populate the constituency table with this information

### Create charts of the data
I would try using a Javascript plugin such as highcharts.js to create pie charts of the results

### Reload the data on the fly
Create a timed ajax request to reload the results data on the fly in the browser - properly 'live'

### Use chosen.js to make selections nicer
Once the real consituency data is in place the drop down will be very long - use the chosen.js plugin to make it easier to use.

### Prevent someone from voting more than once
Set a cookie with Javascript once someone has voted to stop them voting again
