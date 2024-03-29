# Darian Yane Portfolio 💼
Through this portfolio you will be able to know my skills and you will get all the necessary information to contact me.

# Table of Contents
- [Darian Yane Portfolio](#darian-yane-portfolio)
- [Table of Contents](#table-of-contents)
- [What is included in this portfolio](#what-is-included-in-this-portfolio)
  - [Reasons for hiring me](#reasons-for-hiring-me)
  - [My projects](#my-projects)
    - [SQL Cleaning Data Project](#SQL-cleaning-data-project)
    - [Nutriplan](#nutriplan)
    - [Grade](#grade)
    - [Fast-Reading](#fast-reading)
    - [Travel Blog](#travel-blog)
  - [About me](#about-me)
  - [Personal Roadmap](#personal-roadmap)
  - [Contact Form](#contact-form)
  - [My networks](#my-networks)
- [FAQ](#faq)
    - [Why are you doing this portfolio?](#why-are-you-doing-this-portfolio?)
    - [Can I optimize a file with Fast-Reading?](#can-i-optimize-a-file-with-fast-reading?)
    - [What kind of files can I optimize with Fast-Reading?](#what-kind-of-files-can-i-optimize-with-fast-reading?)
    - [Does it cost anything?](#does-it-cost-anything?)
    - [Can I register and create a travel blog post?](#can-i-register-and-create-a-travel-blog-post?)
    - [How can I contact you?](#how-can-i-contact-you?)
    - [How is this project done?](#how-is-this-project-done?)
- [Updates](#updates)

# What is included in this portfolio?
I made this portfolio in order to get a job. You can see the deployed version at www.darianyane.com
In this site I explain the reasons for hiring me, show the projects I have created, tell you about my education and work experience, give you links to my social networks, and provide you with a contact form so we can arrange an interview.


## Reasons for hiring me
Here you will find the reasons why you should hire me as soon as possible.


## My projects
In this section you will find the access to the different projects I have worked on. You will find a text modifier to optimize reading and a travel blog (with CRUD, user management, etc.) among other projects.

### SQL Cleaning Data Project
In this project you receive an excel file with information that needs to be cleaned (data with errors, NULL, duplicates, etc).

Through the use of SQL, the data is cleaned so that later it can be processed correctly.

The objective is to take a list of property sales and clean up the information using SQL code.

#### What improvements have been made?
During the optimization process, the following improvements were made:

- Addition of new fields
- Complete missing data (NULL)
- Separation of data in different columns
- Correct data format
- Grouping of categories
- Duplicate removal
- Elimination of unnecessary columns

### Happiness Indicators
The aim of this work is to determine which are the characteristics of people who consider themselves happier and less happy than the average.

#### What was the process performed?
Data preparation
* Download the dataset.
* Analyzed the data to identify the candidate columns to be relevant.
* Performed the necessary transformations/cleaning before importing the data into Tableau.

Data analysis
* Compared the different fields with the corresponding number of happy people. In general I did not take absolute numbers because the sample was not uniform, and I used percentages within each sample category.
* When analyzing each parameter, I determined if there were relevant differences within the groups that deserved to be discussed later.

Presentation of results
* Generated several Dashboards to show which were the characteristics of the happiest and unhappiest people.

<p align="center">
<a><img src="https://github.com/DarianYane/DA-Dev-Portfolio/blob/main/landing/static/assets/img/landing/Dashboard-Happiness1.png" style="width: 740px; height: 1341px;"/></a>
</p>

<p align="center">
<a><img src="https://github.com/DarianYane/DA-Dev-Portfolio/blob/main/landing/static/assets/img/landing/Dashboard-Happiness2.png" style="width: 740px; height: 1688px;"/></a>
</p>

### SQL Cleaning Data Project
In this project you receive an excel file with information that needs to be cleaned (data with errors, NULL, duplicates, etc).

Through the use of SQL, the data is cleaned so that later it can be processed correctly.

### Nutriplan
This application allows you to generate a weekly diet plan with four meals a day, considering the physiological characteristics, objectives, and food preferences of each individual.

The application guides you through a series of steps where you will be asked for information.

In the first instance, the physiological data of the person is requested. Then a range of physical activity is requested to know the level of activity/sedentariness of the person. Finally, it is asked to indicate whether the is to gain muscle mass or to lose weight.

This information is used to calculate the basal metabolic rate and maintenance calories, which are adjusted according to the desired goal to calculate the calories to be consumed daily.

These calories are divided between carbohydrates, proteins and fats to establish a balanced target diet.

In the following steps, the individual is asked to select some of his or her favorite foods to make the diet as attractive and personalized as possible. These foods are considered to be preferentially included in the diet. In case the user does not select any food as a favorite, the application will select foods at random.

Once the favorite foods are selected, the application randomly selects the rest of the foods, and uses NUMPY's SOLVE function to solve a system of equations that satisfies the conditions of the target diet. If for some reason the process returns an error, it reselects another food group until a satisfactory answer is found.

Finally, the weekly diet is presented. If the user is satisfied, he can print the menu. If they are not, they can repeat the process until they find a solution with which they are satisfied.

Nutriplan allows you to generate personalized diets quickly. In addition, its randomized food selection system prevents the person from abandoning the diet because it is monotonous; a new diet can be generated every week!

<p align="center">
<a><img src="https://github.com/DarianYane/DA-Dev-Portfolio/blob/main/landing/static/assets/img/readme/nutrihome.jpg" style="width: 740px; height: 400px;"/></a>
</p>

### Grade
Application to keep track and monitor the corrections that a teacher makes on the delivery of the work of their students.

The teacher can create students, create ratings, and search for students from the main page in order to edit their ratings.

To be able to make modifications and access sensitive information you must be registered on the site.

<p align="center">
<a><img src="https://github.com/DarianYane/DA-Dev-Portfolio/blob/main/landing/static/assets/img/readme/grade-preview.jpg" style="width: 537px; height: 545px;"/></a>
</p>

### Fast-Reading
This application receives a .pdf and places the first two characters of each word in "bold" to make the text easier to read.

Fast-Reading facilitates the reading process by guiding the eyes through text with artficial fixation points. As a result, the reader is only focusing on the highlighted initial letters and lets the brain center complete the word.

Below is a screenshot demonstrating how the aplication works.

<p align="center">
<a><img src="https://github.com/DarianYane/DA-Dev-Portfolio/blob/main/landing/static/assets/img/readme/fastreading-after.jpg" style="width: 400px; height: 400px;"/></a>
</p>


To optimize a file you do not need to download or install anything. You can do it directly from the project page. And if you don't have a .pdf file nearby, I provide one so you can test the project.


### Travel Blog
This travel blog is an improved version of the final work I did for my Python course at Coderhouse. It includes a CRUD for the posts and a user management system.

<p align="center">
<a><img src="https://github.com/DarianYane/DA-Dev-Portfolio/blob/main/landing/static/assets/img/readme/travel-blog-preview.jpg" style="width: 836px; height: 400px;"/></a>
</p>

## About me
In this section you will find a description of my knowledge, experiences and objectives. You can also download my CV.


## Personal Roadmap
Here you will find the goals I have already accomplished, and my future plans as a developer (this section is dynamic and is fed from a database that I modify from the administration panel).


## Contact Form
Do you want to contact me? You can do it from [here](https://www.darianyane.com/#Contact) 


## My networks
These are my social networks, my Linkedin, and the form so you can contact me.
<p align="center">
<a href="https://www.linkedin.com/in/darian-yane/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/128/3536/3536505.png" style="width: 54px; height: 54px;"/></a>
<a href="https://www.youtube.com/c/DarianInvierte" target="_blank"><img src="https://cdn-icons-png.flaticon.com/128/2111/2111748.png" style="width: 54px; height: 54px;"/></a>
<a href="https://twitter.com/DarianInvierte"><img src="https://cdn-icons-png.flaticon.com/128/3670/3670211.png" style="width: 54px; height: 54px;"/></a>
<a href="https://github.com/DarianYane" target="_blank"><img src="https://cdn-icons-png.flaticon.com/128/536/536452.png" style="width: 54px; height: 54px;"/></a>
<a href="https://www.darianyane.com/#Contact" target="_blank"><img src="https://cdn-icons-png.flaticon.com/128/609/609386.png" style="width: 54px; height: 54px;"/></a>
</p>


# FAQ


#### Why are you doing this portfolio?
Because I want to find a job as a Python developer.


#### Can I optimize a file with Fast-Reading?
Yes, you can.


#### What kind of files can I optimize with Fast-Reading?
For now, only pdf files. I hope in the future to expand the functionality for other file types.


#### Does it cost anything?
There is no cost.


#### Can I register and create a travel blog post?
Yes, you can!


#### How can I contact you?
You can do it from [here](https://www.darianyane.com/#Contact) 


#### How is this project done?
This project is made with Python, Django, Bootstrap, and is deployed on Railway.
To make this README I also used https://stackedit.io


# Updates

#### May 2023
* Human Resources API (with massive generation of instances through CSV files)

#### February 2023
* Happiness Indicators
* SQL Cleaning Data Project

#### January 2023
* Nutriplan

#### February 2023
* Code commented
* Buttons for "save and go" to different locations (Grade)
* SQL Cleaning Data Project