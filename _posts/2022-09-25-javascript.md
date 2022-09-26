---
title: Javascript Usage
toc: false
categories: [Jupyter, Trimester 1, Tri 1 Assignments]
comments: true
layout: post
description: Showing the use of javascript with a submenu.
---

# Javascript Usage

{% include navbar-javascript.html %}

## Submenu:

I created a template with a table in _includes, which I imported into this page. In the table I have links to the things I did.

![]({{site.baseurl}}/images/template.png)

This is the line of code that imports the table:

![]({{site.baseurl}}/images/imbed.png)

## Personal Javascript

I created a list of words with a `const` and then I created a function that uses math to pick a word from that list and display it as a piece of text with `document.getElementById`.

Here is my code:

![]({{site.baseurl}}/images/javascriptcode.png)

## Javascript Table

I attempted to create a Javascript table, however when I tried to create one, it gave me errors in the Jupyter Notebook. Because of this I switched to coding in a markdown post and using Google Inspect to debug my code. I was able to get a list in the console, but it refused to print because of errors that said `Uncaught TypeError: Cannot read properties of undefined (reading 'forEach')`.

Here is my code:

![]({{site.baseurl}}/images/personaljscode.png)

Here is the output I managed to get:

![]({{site.baseurl}}/images/output.png)