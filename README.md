# EduTime
Educational Data Mining focusing on time aspect

## Project proposal

### Core idea of the project
Predict probability of a student doing the next exercise based on past exercise behavior. This will allow changing exercise difficulty per student to reduce dropout rate.

### Research questions
What are principal components in e-learning system’s student progress data and good ML model to predict probability of student continuing the course?

### Data
Data is from an online programming course. In addition to user id, gender (M/F), year of birth, and whether the user had previous programming experience (true/false), the data contains the following features:
- WORKED_ON_{EXERCISE}, whether student worked on the exercise (Y/N)
- SUBMITTED_{EXERCISE}, whether student submitted the exercise (Y/N)
- SECONDS_SPENT_ON_{EXERCISE}, number of seconds spent on the exercise
- PERCENTAGE_COMPILES_{EXERCISE}, percentage of states that the student was in that
compiled
- DIFFICULTY_{EXERCISE}, difficulty of that assignment as indicated by the student
- EDUCA TIONAL_V ALUE_{EXERCISE}, educational value of that assignment as indicated
by the student (each student responded to the question "How Educational Was This Assignment" on a scale from 1 to 5 -- this was not used in the original study, but may be interesting for you :));
- NUM_OF_STATES_{EXERCISE}, number of different source code states that the student visited (can be thought of as "steps taken")
- SECONDS_IN_COMPILING_STATE_{EXERCISE}, how many seconds did the student spend in a state that did compile
- SECONDS_IN_NON_COMPILING_STATE_{EXERCISE}, how many seconds did the student spend in a state that did not compile
- LINES_OF_CODE_{EXERCISE}, how many lines of code did the students last solution have
- FLOW_CONTROL_ELEMENT_COUNT_{EXERCISE}, amount of flow control elements (if, while, for, ...) in the solution how many lines of code did the student's last solution have

Data is freely available at https://www.cs.helsinki.fi/group/rage/data/2014-sigite-difficulty-indicators/

### Research methods
Test four different ML models on the data and compare their performance on probability prediction. Test also what are the principal components for the predictions.
Models to be used are:
1. Logistic Regression
2. Naïve Bayes
3. Support Vector Classification
4. Random Forest

### Expected results
Student’s probability to continue to the next assignment can be modeled with significant accuracy in some cases. This will enable to give a student, close to dropping out, easier assignments on the fly to keep them on the course.
