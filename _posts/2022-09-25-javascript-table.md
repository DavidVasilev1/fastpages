---
toc: true
layout: post
description: A table made with Javascript.
categories: [Markdown, Javascript, Trimester 1, Tri 1 Assignments]
title: Javascript Table
comments: true
---

<script>
  function Person(camera, company, year) {
    this.camera = camera;
    this.company = company;
    this.year = year;
  }
  Person.prototype.setRole = function(role) {
    this.role = role;
  }
  Person.prototype.toJSON = function() {
    const obj = {camera: this.camera, company: this.company, year: this.year};
    const json = JSON.stringify(obj);
    return json;
  }
  var cam = [
    new Person("R5", "Canon", 2020),
    new Person("R10", "Canon", 2021),
    new Person("T5i", "Canon", 2020),
    new Person("Alpha 7 III", "Sony", 2018),
    new Person("Alpha 6600", "Sony", 2019),
    new Person("D500", "Nikon", 2016),
  ];
  function Cameras(cam) {
    this.group.forEach(person => this.json.push(person.toJSON()));
  }
  function logItType(output) {
    console.log(output);
  }
  groups = new Cameras(cam);
  logItType(groups.group);
  logItType(groups.group[0].camera);
  logItType(groups.json[0]);
  logItType(JSON.parse(groups.json[0]));
  Cameras.prototype._toHtml = function() {
    var style = (
      "display:inline-block;" +
      "border: 2px solid grey;" +
      "box-shadow: 0.8em 0.4em 0.4em grey;"
    );
    var body = "";
    body += "<tr>";
    body += "<th><mark>" + "Model" + "</mark></th>";
    body += "<th><mark>" + "Company" + "</mark></th>";
    body += "<th><mark>" + "Release Year" + "</mark></th>";
    body += "</tr>";
    for (var row of cam) {
      body += "<tr>";
      body += "<td>" + row.camera + "</td>";
      body += "<td>" + row.company + "</td>";
      body += "<td>" + row.year + "</td>";
      body += "<tr>";
    }
    return (
      "<div style='" + style + "'>" +
        "<table>" +
          body +
        "</table>" +
      "</div>"
    );
};
</script>