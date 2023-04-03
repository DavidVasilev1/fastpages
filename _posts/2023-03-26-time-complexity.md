---
toc: true
layout: post
description: Some notes on time and space complexity with test correction.
categories: [Markdown, Trimester 3, Assignments, Collegeboard]
title: Time Complexity and Practice Test
comments: true
---

### Time and Space Complexity

![]({{site.baseurl}}/images/tc-1.png " ")

- The answer here is number 3 because the first loop is O(n) and the second loop is O(m). They are independent of each other and are run separately, so the time is O(n+m) and the time is O(1).

![]({{site.baseurl}}/images/tc-2.png " ")

- The answer here is number 4 because the function involving j runs inside the function i, meaning that the time complexity is O(n*n). This is because both functions involve n.

![]({{site.baseurl}}/images/tc-3.png " ")

- The answer here is number 2 because j keeps doubling until it is less than or equal to n. A number can be doubled multiple times until it is less than n, which would be log(n).

![]({{site.baseurl}}/images/tc-4.png " ")

- The answer here is number 2 because this means that X will always be the better algorithm than the Y algorithm. This is because in asymptotic analysis, the growth of the algorithm in terms of the input size. This means that X will always take less time to finish for larger values.

![]({{site.baseurl}}/images/tc-5.png " ")

- The answer here is number 4 because ‘(N/2^x )< 1 OR  2^x>N’ where x=O(log N).

![]({{site.baseurl}}/images/tc-6.png " ")

- The answer here is 3 because both space and time are useful to find the efficiency of a program.

![]({{site.baseurl}}/images/tc-7.png " ")

- The answer here is 2 because the more operations performed by an algorithm, the more complex it is, compared to the input size.

![]({{site.baseurl}}/images/tc-8.png " ")

- The answer here is 3. This program is k^(n-1) and when the log is taken, it becomes log(k)n,

![]({{site.baseurl}}/images/tc-9.png " ")

- The answer here is 3 because the first loop is run for n times and the second one is run for n-1 times. This means that the overall complexity is n(n-1).

![]({{site.baseurl}}/images/tc-10.png " ")

- The answer here is 2 because algorithm A is constant while algorithm B is exponential. This means that as the input size increases, the time it takes for a program to run also increases, but for A, the time stays constant.

### CB Quiz

![]({{site.baseurl}}/images/quiz2.png " ")

- Although I did get a perfect score, I feel like I should still review long problems that involve a lot of reading, such as problems 19. I should also review some binary questions.

![]({{site.baseurl}}/images/19.1.png " ")
![]({{site.baseurl}}/images/19.2.png " ")

![]({{site.baseurl}}/images/24.png " ")