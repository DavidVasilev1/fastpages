---
toc: false
layout: post
description: I random word generator I made.
categories: [Markdown, Javascript, Trimester 1, Tri 1 Assignments]
title: Personal Javascript
comments: true
---

## Personal Javascript Program

- This program generates random words at the click of a button. The list that it chooses words from has about 20 words.

<br>
<style>
  .container {
    text-align: center;
  }
</style>  
<div class="container">
  <style>
    button {
      padding: center;
      border-color: white;
      padding: 15px 32px;
      text-align: center;
      font-size: 16px;
    } 
    h3 {
      text-align: center;
    }
  </style>

  <button name="button" onclick="randomWord()">Click to Generate Word</button>
    <br>
  <h3 id="Word Generator" href="#">The Word Will Appear Here</h3>
</div>
<script>
  const wordList = [
    "reform",
    "dark",
    "satisfaction",
    "spend",
    "distortion",
    "application",
    "mouth",
    "useful",
    "flock",
    "restless",
    "perfume",
    "charity",
    "force",
    "relation",
    "straighten",
    "eat",
    "artificial",
    "sleeve",
    "river",
    "century"
  ];
  function randomWord() { 
    var index=Math.floor(Math.random() *wordList.length) 
    document.getElementById("Word Generator").innerHTML = wordList[index]
  }
</script>
