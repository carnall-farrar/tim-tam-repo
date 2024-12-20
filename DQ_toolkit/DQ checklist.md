<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="DQ_checks_picture.jpg" alt="Logo" width="300" height="300">
  </a>

  <h3 align="center">Data Quality Checklist</h3>

  <p align="center">
    Find your problems before 10pm the night before the outputs are due.
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#background-reading">Background reading</a>
    </li>
    <li>
      <a href="#reference-information">Reference information</a>
    </li>
    <li>
      <a href="#what-is-a-duplicate">What is a row? What is a duplicate?</a>
    </li>
    <li>
      <a href="#reference-information">Completeness checks</a>
    </li>
    <li>
      <a href="#reference-information">Simple plots</a>
    </li>
    <li>
      <a href="#reference-information">Linking counts</a>
    </li>
    <li>
      <a href="#reference-information">Comparisons to other sources</a>
    </li>
    <li>
      <a href="#reference-information">Accuracy of names</a>
    </li>
    <li>
      <a href="#reference-information">Join duplicate avoidance</a>
    </li>
  </ol>
</details>

## Background reading

Matt

<p align="right">(<a href="#top">back to top</a>)</p>

## Reference information

Danyal

<p align="right">(<a href="#top">back to top</a>)</p>

## What is a row? What is a duplicate?

Maddie

<p align="right">(<a href="#top">back to top</a>)</p>

## Completeness checks

Before we start working with new datasets, it is always a good idea to perform some data quality checks beforehand. Assessing the completeness of dataset fields is important for understanding data quality and its potential impact on your analysis. The `completeness_utils.py` module is designed to perform data quality checks on input tables and provides the following functionalities:

1. Identifies and counts **missing values** for each column in a table.
2. Detects and counts values that are flagged as **invalid** based on pre-defined criteria (e.g., placeholder values like "99" or "unknown").
3. Conducts a **sense check of the values** by looking at the distribution of unique values in each column. 

<p align="right">(<a href="#top">back to top</a>)</p>

## Simple plots

Matt

<p align="right">(<a href="#top">back to top</a>)</p>

## Linking counts

When we have a linked dataset with persistent patient IDs we want to check how many people are linkable between each set of tables. The file check_linking_utils.py contains code to create the following table:

![image info](check_linking.jpg)

Each cell tells you what percentage of IDs in the the on the LHS appear in the table across the top.

<p align="right">(<a href="#top">back to top</a>)</p>

## Comparison to other sources

Bec

<p align="right">(<a href="#top">back to top</a>)</p>

## Accuracy of names

Bec

<p align="right">(<a href="#top">back to top</a>)</p>

## Join duplicate avoidance

Rami

<p align="right">(<a href="#top">back to top</a>)</p>
