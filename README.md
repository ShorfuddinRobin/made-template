# Exercise Badges

![](https://byob.yarr.is/ShorfuddinRobin/made-template/score_ex1) ![](https://byob.yarr.is/ShorfuddinRobin/made-template/score_ex2) ![](https://byob.yarr.is/ShorfuddinRobin/made-template/score_ex3) ![](https://byob.yarr.is/ShorfuddinRobin/made-template/score_ex4) ![](https://byob.yarr.is/ShorfuddinRobin/made-template/score_ex5)

# Climate Change Patterns in Bangladesh: A Correlation Analysis of Temperature and Rainfall Trends

## Project Work
**
## Project Description:
This project aims to explore the relationship between temperature and rainfall patterns in Bangladesh over time to understand the broader implications of climate change. By analyzing long-term weather data, this study seeks correlations between these variables to provide details that can helpful for policy decisions and planning for sustainable development.

## Data Sources:
Bangladesh Weather Dataset from Kaggle, providing comprehensive weather data including temperature.
Historical Rainfall Data in Bangladesh from Kaggle, focused detailed rainfall records.
## Methodology:
Data Fetching and Preparation:  Downloaded datasets from Kaggle and stored in a local SQLite database.
Data Merging: Combined datasets based on 'Year' and 'Month' columns, and handled missing values.
Correlation Analysis: Created scatter plots and calculated the Pearson correlation coefficient to measure the linear relationship between temperature and rainfall.
Linear Regression Analysis: Conducted to determine the influence of temperature changes on rainfall.
## Results:
Scatter Plot: Shows a positive relationship between temperature and rainfall.
Correlation Coefficient: Indicates a weak positive correlation (approximately 0.232) between temperature and rainfall.
Linear Regression: Suggests that for each degree Celsius increase in temperature, rainfall increases by approximately 1.213 mm.
## Conclusions:
Findings: A moderate positive correlation exists between temperature and rainfall, implying that rising temperatures could lead to increased rainfall in Bangladesh.
Implications: These insights are crucial for developing climate change adaptation strategies, highlighting the need to consider temperature's impact on rainfall.
Limitations and Future Work: Accuracy depends on data quality and currently focuses on temperature and rainfall only. Future work should incorporate more variables and advanced models to capture complex climate interactions.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
