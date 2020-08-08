# Final Project

*"Foos-ball? Buncha overgrown monsters man-handlin' each other... 'Member when dat man wanted you to play foos-ball, Bobby?" - Mama Boucher*
-The WaterBoy, 1998

## NFL Statistical Analysis & Prediction of Win-Loss Records 

*Project Team: Jeremy Brent, Alim Memon, Brian Remite, Matt Sadowski, Bryan Wilson*

### Programs/Methods Used to ETL Data, Build a Machine Learning Model, & Test and Train Model to Predict a Team's W/L Record based on statistics.
- [x] Extracted data as CSV files *Entire Team*
- [x] Jupyter Notebooks/Pandas to clean data (remove extraneous columns, join or merge files; to produce consistent datasets for each year) *Team*
- [x] Continue wrangling .csv's into a usable dataframe for training and testing *Team*
- [x] Build various machine learning models to find the best one for our purpose *Jeremy* 
- [x] Train model on 2000-2018, test and predict on 2019 season W/L ratio (season win total) *Jeremy, with some help*
- [x] Test Option 1: Created season stat estimation formula for prediction of season W/L ratio based on estimates to emulate final use case *Matt*
- [x] Test Option 2: Use the Adjusted Pythagorean Theorem (source www.footballoutsiders.com)  *Brian*
- [ ] Test model on both versions of 2019 estimated stats *Jeremy, with help*
- [ ] Verify accuracy and viability of model by comparing results of model predictions to actual 2019 W/L ratios, choose the best stat estimation *Team*
- [ ] Use model to predict 2020 season results; assuming a "normal" season (*Full-length, without factoring for Covid-19 variables*) *Team*

### Build Deployment Module & User Interface; Launch on AWS Server
- [x] Build basic webpage with placeholder information (will fill in later once model, prediction, and Tableau Story are finished) *Alim*
- [ ] Build a flask app to enable the python script to run on a cloud-based webpage *Alim*
- [ ] Convert Machine Learning model Jupyter Notebook to a Python file to be able to run the model live *Entire Team*
- [ ] Fill out, format, and design a clean, visually appealing, usable webpage *Bryan, Alim*
 
### Project Presentation
- [ ] Use Tableau to build a story with which to present our results in a visually appealing and informative manner *Brian, Bryan*
- [ ] Rehearse presentation *Team*
- [ ] Present project to the class and submit for grading *Team*
- [ ] Celebratory champagne for winning the Rutgers Data Science Final Project Super Bowl i.e. IT'S GRADUATION TIME BOYS!!! *Team*


### Meeting Notes- Tuesday, August 4th
* Discussed with Gretel to ensure that we are NOT using (example: 2018 win loss ratio in our prediction of 2018 season), but we DO want to use 2017 win loss ratio to predict 2018, and so on.  
* Edit headers for all columns to include OFFENSE/DEFENSE and add a YEAR column as a label, NOT A FEATURE (for our understanding of data)
* Next step is to work on cleaning up and combining csv's into single usable dataframe/csv. 
