# EduTime
Educational Data Mining focusing on time aspect

## Project report
Final report available [here](./reports/Edutime_final_report.pdf).

## Project proposal

### Core idea of the project
We wanted to see if the time consumption is related to difficulty and educational value given by the student. 

### Research questions
When doing work on problems in programming and in general, it is said that it is better to take short breaks once in a while. We wanted to know if there could be found a relationship between solving a problem and time. We also were interested in if educational value, difficulty value and time consumption are related to each other.

### Data
Data is from an online programming course. In addition to user id, gender (M/F), year of birth, and whether the user had previous programming experience (true/false), the data contains the following features:
- WORKED_ON_{EXERCISE}, whether student worked on the exercise (Y/N)
- SUBMITTED_{EXERCISE}, whether student submitted the exercise (Y/N)
- SECONDS_SPENT_ON_{EXERCISE}, number of seconds spent on the exercise
- PERCENTAGE_COMPILES_{EXERCISE}, percentage of states that the student was in that
compiled
- DIFFICULTY_{EXERCISE}, difficulty of that assignment as indicated by the student
- EDUCATIONAL_VALUE_{EXERCISE}, educational value of that assignment as indicated
by the student (each student responded to the question "How Educational Was This Assignment" on a scale from 1 to 5 -- this was not used in the original study, but may be interesting for you :));
- NUM_OF_STATES_{EXERCISE}, number of different source code states that the student visited (can be thought of as "steps taken")
- SECONDS_IN_COMPILING_STATE_{EXERCISE}, how many seconds did the student spend in a state that did compile
- SECONDS_IN_NON_COMPILING_STATE_{EXERCISE}, how many seconds did the student spend in a state that did not compile
- LINES_OF_CODE_{EXERCISE}, how many lines of code did the students last solution have
- FLOW_CONTROL_ELEMENT_COUNT_{EXERCISE}, amount of flow control elements (if, while, for, ...) in the solution how many lines of code did the student's last solution have

Data is freely available at https://www.cs.helsinki.fi/group/rage/data/2014-sigite-difficulty-indicators/

### Expected results
Student’s time consumption per exercise should look like Poisson distribution or some other distribution. We also predict that there will be a certain time window in which most students make exercise. 
