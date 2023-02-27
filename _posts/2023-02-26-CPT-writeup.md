---
toc: true
layout: post
description: A check to see if my program meets the Collegeboard criteria.
categories: [Markdown, Trimester 2, Assignments, Collegeboard]
title: CPT Writeup
comments: true
---

## 3a. Provide a written response that does all three of the following: 

### i. Describes the overall purpose of the program:

The overall purpose of the program is to allow students to enter their classes into the input fields, including class period, class number, class name, and start and end times. This information is then formatted into a table and map, allowing the students to have an organized schedule list with classroom locations.

### ii. Describes what functionality of the program is demonstrated in the video

In the video, the input and display of data is demonstrated. This is shown by typing information and selecting information from the input fields and then displaying it on the table and map. Once the page is reloaded, the data stays there because it is stored in an api.

### iii. Describes the input and output of the program demonstrated in the video

In the video, the period number, class name, class number, and start and end times of the class are inputted by the user. When the Add button is pressed, the data is displayed on the generated table and map, as well as stored in the API database. The clear button, which is an input from the user, clears all the data from the API and the populated table.

## 3b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program

### i. The first program code segment must show how data have been stored in the list.

![]({{site.baseurl}}/images/cpt1.png "A data table is being formatted into a .db file, which can be accessed with an extension, SQLite.")
![]({{site.baseurl}}/images/cpt2.png "This is the data table created with data from the frontend, which is converted from a list to a data table.")

### ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose

![]({{site.baseurl}}/images/cpt3.png "In this code section, the data is called form the API and then set as variables for HTML to print on the frontend.")

### iii. Identifies the name of the list being used in this response

The list being used here is 