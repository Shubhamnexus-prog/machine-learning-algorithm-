CREATE  TABLE student
(
  s_no INT PRIMARY KEY,
  s_name VARCHAR(20),
  S1 INT,
  S2 INT, 
  S3 INT
 )

 -- INSERT  VALUES--

 INSERT INTO student VALUES
 ('A',80,90,70),
 ('B',30,60,50),
 ('C',60,20,30),
 ('D',10,20,30)

 SELECT *FROM student

 -- list of the student who are pased

 SELECT*FROM student WHERE S1>=35 AND S2>=35 AND S3>=35

 SELECT *FROM student

 --list of student who are failed

 SELECT* FROM student WHERE S1<35 AND S2<35 AND S3<35

 --list of student who are failed 1 subject


SELECT *
FROM student
WHERE (S1 < 35 AND S2 >= 35 AND S3 >= 35)
   OR (S1 >= 35 AND S2 < 35 AND S3 >= 35)
   OR (S1 >= 35 AND S2 >= 35 AND S3 < 35);

 --list of student who are failed 2 subject--


 
SELECT *
FROM student
WHERE (S1 < 35 AND S2 < 35 AND S3 >= 35)
   OR (S1 < 35 AND S2 >= 35 AND S3 < 35)
   OR (S1 >= 35 AND S2 < 35 AND S3 < 35);


 --list of  the student who failed all 3 subject--
 
SELECT *
FROM student
WHERE S1 < 35
  AND S2 < 35
  AND S3 < 35;
