---
toc: true
layout: post
description: A check to see if my program meets the Collegeboard criteria.
categories: [Markdown, Trimester 2, Assignments, Collegeboard]
title: CPT Writeup
comments: true
---

## 3a. Provide a written response that does all three of the following: 

> i. Describes the overall purpose of the program:

The overall purpose of the program is to allow students to enter their classes into the input fields, including class period, class number, class name, and start and end times. This information is then formatted into a table and map, allowing the students to have an organized schedule list with classroom locations.

> ii. Describes what functionality of the program is demonstrated in the video

In the video, the input and display of data is demonstrated. This is shown by typing information and selecting information from the input fields and then displaying it on the table and map. Once the page is reloaded, the data stays there because it is stored in an api.

> iii. Describes the input and output of the program demonstrated in the video

In the video, the period number, class name, class number, and start and end times of the class are inputted by the user. When the Add button is pressed, the data is displayed on the generated table and map, as well as stored in the API database. The clear button, which is an input from the user, clears all the data from the API and the populated table.

## 3b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program

> i. The first program code segment must show how data have been stored in the list.

![]({{site.baseurl}}/images/cpt1.png "A data table is being formatted into a .db file, which can be accessed with an extension, SQLite.")
![]({{site.baseurl}}/images/cpt2.png "This is the setters and getters which are used to set the data into place for each running instance of the API.")
![]({{site.baseurl}}/images/cpt3.png "This is the SQLite table created with the data from the API.")

> ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose

![]({{site.baseurl}}/images/cpt4.png "In this code section, the data is called from the API list created and sent to the frontend, when requested.")

> iii. Identifies the name of the list being used in this response

The list being used here is schedule.db, which is formatted into a table and is used to store and post data onto the frontend of the website. This way the data is stored is in something called a database, which is defined in the schedule python class. Inside, the data points are defined, including class period, class name, class number, and start and end times.

> iv. Describes what the data contained in the list represent in your program

The data is stored in the database file as strings. These strings are inputted by the user and posted through networking with JSON into the API, which formats it into the database. These data points represent the qualities of the class that they choose to add to their schedule. Without the storage of the data into the API, the data would have no meaning as it would be deleted upon reload of the webpage.

> v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list

Without a list, the program would not be able to run at all. The list is critical to storing the data the user inputs and without the list, the data would be lost from the user every time the page is reloaded. The program could be entirely written with the use of localstorage, which would store the data locally on the computer with cookies, however, moving to a different computer or deleting your browsing history would entirely delete the data you have previously entered.

## 3c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure.

> i. The first program code segment must be a student-developed procedure that:
> - Defines the procedure’s name and return type (if necessary)
> - Contains and uses one or more parameters that have an effect on the functionality of the procedure
> - Implements an algorithm that includes sequencing, selection, and iteration 

![]({{site.baseurl}}/images/cpt5.png " ")

> ii. The second program code segment must show where your student-developed procedure is being called in your program.

![]({{site.baseurl}}/images/cpt6.png " ")

![]({{site.baseurl}}/images/cpt7.png " ")

> iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program

The function ```ScheduleListAPI()``` contains many subsections. This procedure allows the callback of all data, as well as the deletion of all data through the functions ```get()``` and ```delete()```. It allows all of the data to be recalled whenever the webpage is reloaded, allowing access to anyone from anywhere, and it also allows the data to be entirely redone if one isn't happy with it's contents.

> iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.

- When the user enters their data, the data is sent to the API through the ```addLocal()``` function. This pulls the parameters containing the information the user inputted from the input fields and sends it to the API in a JSON list known as ```data```. This is done through a POST request from the frontend to the API.
- Once the API receives the JSON data, it parses through the it, assigning it to each of the variables used to store the data in the database list. If the API detects a problem with the data being inputted, it sends an error message with the server error at hand.
- Once the data storage has been successful, the data can be called back with a fetch from the frontend, through the ```getList()``` function. When this is called, the ```get()``` function is called, parsing through the entire database by id and sending all of the information to the frontend for organization and use.
- If a user chooses to delete the data they have, the ```remove()``` function is called, sending a DELETE request to the API, causing all of the data in the list to be deleted, only if there are no errors in the data.

## 3d. Provide a written response that does all three of the following:

> i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute

- The ```ScheduleListAPI()``` function is called a first time when the user initially loads the page, requesting all of the stored data in the API be brought out in a readable format through the ```get()``` function into HTML formatting.
- The function is called a second time when the user decides to delete the data, causing the displayed data to entirely disappear through the ```delete()``` function.

> ii. Describes what condition(s) is being tested by each call to the procedure:

Each time the procedure is called, the API tests for errors in the data that may prevent the frontend code from running properly.
- The first call checks through all of the data in the API list, making sure that the data is correctly formatted. If it is, the data is sent to the frontend to be displayed.
- The second call checks whether there are any server errors involving the formatting of the data and if there are none, all of the data is deleted.

> iii. Identifies the result of each call

- The first call results in the pulling of all the stored data out of the API and into the display of it onto the frontend.
- The second call results in the deletion of all stored data in the API and the disappearance of it in the frontend.