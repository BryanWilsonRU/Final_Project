# Final Project

*"Foos-ball? Buncha overgrown monsters man-handlin' each other... 'Member when dat man wanted you to play foos-ball, Bobby?" - Mama Boucher*
-The WaterBoy, 1998

## NFL Statistical Analysis & Prediction of Win-Loss Records 

* Project Team: Jeremy Brent, Alim Memon, Brian Remite, Matt Sadowski, Bryan Wilson

* Hypothesis: NFL Season Statistics Can Be Used to Predict the Results of the Following Season

* Conclusion:
There is a low degree of confidence that the previous season stats for any team is a significant indicator of future performance. This can be attributed to a wide variety of causes, including, but not limited to: 
- Roster changes due to trades, draft picks, and retirements
- Increases/decreases in team momentum and cohesion among players and the organization
- Injuries
- Weather and/or unforeseeable "acts of God" (earthquakes, hurricanes, etc.)

### Libraries/Software Used:
*Model Build
1. Python        (Jupyter Notebook)
- Pandas         (Data Cleaning/Wrangling)
- Matplotlib     (Model Visualization within Jupyter Notebook)
- SciKit Learn   (Machine Learning Model)
- Seaborn        (Statistical Analysis- Correlation Matrix)

*Website Build
1. HTML 
2. CSS
  - Bootstrap
3. JavaScript


### Programs/Methods Used to ETL Data, Build a Machine Learning Model, & Test and Train Model to Predict a Team's W/L Record based on statistics.
- [x] Extracted data as CSV files
- [x] Jupyter Notebooks/Pandas to clean data (remove extraneous columns, join or merge files; to produce consistent datasets for each year)
- [x] Continue wrangling .csv's into a usable dataframe for training and testing
- [x] Build various machine learning models to find the best one for our purpose
- [x] Train model on 2000-2018, test and predict on 2019 season W/L ratio (season win total)
- [x] Test Option 1: Created season stat estimation formula for prediction of season W/L ratio based on estimates to emulate final use case
- [x] Test Option 2: Use the Adjusted Pythagorean Theorem (source www.footballoutsiders.com)
- [x] Test model on both versions of 2019 estimated stats
- [x] Verify accuracy and viability of model by comparing results of model predictions to actual 2019 W/L ratios, choose the best stat estimation
- [x] Use model to predict 2020 season results; assuming a "normal" season (*Full-length, without factoring for Covid-19 variables*)
- [x] Consider the possible application of a Neural Network
- [ ] Build, train, and test on data to form a conclusion about the usefulness of the neural network.
- [ ] Develop clear conclusion about various model performance, describe on website, and include in presentation

### Build Deployment Module & User Interface; Launch Website Using GitHub Pages
- [x] Build basic webpage with placeholder information (will fill in later once model, prediction, hypothesis, and conclusion are finished)
- [x] Build a flask app to enable the python script to run on a cloud-based webpage
- [ ] Convert Machine Learning model Jupyter Notebook to a Python file to be able to run the model live 
- [ ] Fill out, format, and design a clean, visually appealing, usable website
  - [x] Include a Home page
  - [ ] Include the actual model (Jupyter Notebook containing our ML model, and our Neural Network. Try to fit in 1 clearly documented, concise notebook)
  - [x] Include our Hypothesis, Conclusion, and any/all information about our results and interpretation; based on facts/data rather than opinion.
  - [ ] Design with relevant graphics, visuals, and in a consistent tone & format. 
  - [x] Optional: Include a Contact/About page with information about each group member. 
 
### Project Presentation
- [ ] Tell our story through our website and class presentation.
- [ ] Rehearse presentation.
- [ ] Present project to the class and submit for grading.
- [ ] Celebrate all the hard work we've put in and get ready to party; WE'RE GRADUATING!!!
