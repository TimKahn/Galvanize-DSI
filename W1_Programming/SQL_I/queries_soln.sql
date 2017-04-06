/*
Implementing queries from
Introduction to SQL for Data Scientists
*/

-- Uncomment the query you'd like to run

/*
SELECT
    s.id AS id,
    s.name AS name
FROM
    student AS s
WHERE
    s.id = 1;
;
*/

/*
SELECT
    s.id AS id,
    s.name AS name,
    t.gpa AS gpa
FROM
    student AS s
JOIN
    term_gpa AS t
ON
    s.id = t.id
WHERE
    s.id = 1
    AND
    t.term = 2012;
*/

/*
Question 1: Write a query that will find and display Edith Warton's and Henry 
James's gpas for 2011 and 2012.
*/

/*
SELECT
    s.name AS name,
    t.term AS term,
    t.gpa AS gpa
FROM
    student AS s
JOIN
    term_gpa AS t
ON
    s.id = t.id
WHERE
    s.name IN ('Edith Warton', 'Henry James')
    AND
    t.term = 2011 
    OR 
    t.term = 2012;
*/

/* Question 2: Write a query that will find Edith Warton's and Henry James's 
highest gpas rounded to two decimal places.  Order them by whoever has the highest gpa.
*/

/*
SELECT
    s.name AS name,
    ROUND(MAX(t.gpa),2) AS max_gpa
FROM
    student AS s
JOIN
    term_gpa AS t
ON
    s.id = t.id
WHERE
    s.name IN ('Edith Warton', 'Henry James')
GROUP BY s.name
ORDER BY max_gpa DESC;
*/


/* Practice with Left Joins
In one table list all the students, the term they were enrolled, their gpa for that
term, and the degree they received (if they received one).
*/

/*
SELECT
    s.name AS name,
    t.term AS term,
    t.gpa AS gpa,
    d.degree as degree
FROM
    student AS s
JOIN
    term_gpa AS t
ON
    s.id = t.id
LEFT JOIN
    degrees AS d
ON
   d.id = s.id
   AND
   d.term = t.term;
*/

/* Use of Grouping
Let's find the students who have graduated.
*/

/*
SELECT
    s.name AS name
FROM
    student AS s
JOIN
    degrees as d
ON
    s.id = d.id
GROUP BY s.name;
*/

/*
Question 3:  Let's find the students who haven't graduated and their average 
gpa, rounded to two decimal places. You may want to use a subquery.
*/

SELECT s.name AS name, 
       ROUND(avg(t.gpa),2) AS avg_gpa
FROM 
    student AS s
JOIN
    term_gpa AS t
ON
    s.id = t.id
GROUP BY s.name
HAVING s.name NOT IN (SELECT
                        s.name AS name
                     FROM
                        student AS s
                     JOIN
                        degrees as d
                     ON
                        s.id = d.id
                     GROUP BY s.name);

