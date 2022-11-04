select Concat(GivenNames, " ", Surname) As nameses, 
		max(TIMESTAMPDIFF(YEAR, DateOfBirth, CURDATE())) as Age, Gender
from student
where Gender = 'female';

CREATE TABLE Student(
StudentID integer,
GivenNames varchar(150) NOT NULL,
Surname varchar(150) NOT NULL,
PreferredName varchar(60) NOT NULL,
DateOfBirth date NOT NULL,
title Enum('Mr', 'Mrs', 'Ms', 'Other'),
gender Enum('Male', 'Female', 'other'),
StudentEmail varchar(100) NOT NULL,
PersonalEmail varchar(100) NOT NULL,
AddressLine1 varchar(150) NOT NULL,
AddressLine2 varchar(150),
Suburb varchar(100) NOT NULL,
Postcode varchar(50) NOT NULL,
Phone varchar(50) NOT NULL,
EmergencyContactID integer NOT NULL,
HomeAddressID integer NOT NULL,
BankDetailsID integer,
CONSTRAINT PkID PRIMARY KEY(StudentID),
Constraint fk_EmergencyContact Foreign key(EmergencyContactID) references EmergencyContact(EmergencyContactID),
Constraint fk_HomeAddress Foreign key(HomeAddressID) references HomeAddress(HomeAddressID),
Constraint fk_BankDetails Foreign key(BankDetailsID) references BankDetails(BankDetailsID));



INSERT INTO Student
VALUES (10570365, 'Raneli', 'Kothalawala', 
'Raneli', '1998-09-22','Ms', 'Female', 'raneli@our.ecu.edu.au', 
'raneli@gmail.com', '122', 'Thomas Avenue', 'Yokine', '6066', '0460852592', 502, 122, 202);
