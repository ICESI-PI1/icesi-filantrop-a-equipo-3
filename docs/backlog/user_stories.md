# USER STORIES

Sprint on Jira: [https://integrativeproject1.atlassian.net/jira/software/projects/MSDE/boards/3](https://integrativeproject1.atlassian.net/jira/software/projects/MSDE/boards/3)

**User Story 1 - Student Registration:**
Estimation:  8

https://github.com/ICESI-PI1/icesi-filantrop-a-equipo-3/blob/main/img/1.png

As a member of the philanthropy office, I want to be able to enter the information of new students joining the institution, including their full name, date of birth, ID card, email address, mobile number, ICFES score, and assign them to an existing donor.

**User Story 2 - Creation of Tracking for Consultations in CREA:**
Estimation:  13

https://github.com/ICESI-PI1/icesi-filantrop-a-equipo-3/blob/main/img/2.png

As a user of the philanthropy office, I need to generate reports that contain the consultation history made by a student in the CREA department. These reports should include information such as date, time, reason, and result of each consultation.

**User Story 3 - Updating Student Data:**
Estimation:  5

https://github.com/ICESI-PI1/icesi-filantrop-a-equipo-3/blob/main/img/3.png

As a member of the philanthropy office, I need the ability to request and update the information of students registered in the system at any time, to keep it synchronized with the data recorded at the university.

**User Story 4 - Generation of Alerts for Cancellations:**
Estimation:  8

https://github.com/ICESI-PI1/icesi-filantrop-a-equipo-3/blob/main/img/4.png

As a member of the philanthropy office, I need to receive an alert if a student cancels subjects or makes withdrawals. This will help me stay updated on changes in the students' academic situation and take action if necessary.

**User Story 5 - Donor Registration:**
Estimation: 8

https://github.com/ICESI-PI1/icesi-filantrop-a-equipo-3/blob/main/img/5.png

As an administrator of the system, I want to be able to register the information of new donors, including their full name, contact information, history of previous donations, and donation preferences, to maintain an updated record of available donors.

**User Story 6 - Generation of Financial Reports:**
Estimation: 21

https://github.com/ICESI-PI1/icesi-filantrop-a-equipo-3/blob/main/img/6.png

As a user of the philanthropy office, I need the ability to generate financial reports that show the current status of scholarship funds and donations received. These reports should be used for decision-making and financial planning.

**User Story 7 - Management of Attached Documents:**
Estimation: 8

https://github.com/ICESI-PI1/icesi-filantrop-a-equipo-3/blob/main/img/7.png

As a member of the philanthropy office, I want to be able to attach relevant documents to student and donor records, such as donation receipts, thank you letters, or additional reports, to keep a complete and organized record of the information.

**User Story 8 - Notification to Philanthropy:**
Estimation: 5

https://github.com/ICESI-PI1/icesi-filantrop-a-equipo-3/blob/main/img/8.png

As a member of the Welfare office, I want to be able to send notification alerts to the Philanthropy offices to inform them about student updates to make relevant decisions.

**Estimation**

**Prioritization**

In this case, we will choose to prioritize tasks based on the skills of the work team. Therefore, we have determined a score from 1 to 5, where 1 would be the task with fewer assigned resources and workers, and 5 would be the task with more assigned resources and workers.

User Story 3: We consider it requires a level 5 prioritization.

User Story 4: We consider it requires a level 4 prioritization.

User Story 6: We consider it requires a level 4 prioritization.

User Story 1: We consider it requires a level 3 prioritization.

User Story 2: We consider it requires a level 2 prioritization.

User Story 5: We consider it requires a level 2 prioritization.

User Story 8: We consider it requires a level 2 prioritization.

User Story 7: We consider it requires a level 1 prioritization.

**Gherkin Scenarios**

**User Story 1 - Student Registration:**

Scenario 1:
Given I am a member of the philanthropy office, authenticated and on the student registration window.
When I enter the complete information of a new student
And assign to an existing donor
Then the system successfully registers the student

Scenario 2:
Given I am a member of the philanthropy office, authenticated and on the student registration window.
When I try to register a student without providing all required information
Then the system displays an error indicating the missing fields

**User Story 2 - Creation of Tracking for Consultations in CREA:**

Scenario 1:
Given I am a user of the philanthropy office, authenticated and on the consultation tracking creation window.
When I select a student and request their CREA consultation history
Then the system generates a report with the date, time, reason, and result of each consultation

Scenario 2:
Given I am a user of the philanthropy office, authenticated and on the consultation tracking creation window.
When I select a student who has not had consultations in CREA
Then the system displays a message indicating the student has no registered consultations

**User Story 3 - Updating Student Data**

Scenario 1:
Given I am a member of the philanthropy office, authenticated and on the student window.
When I select a student and update their information
Then the system successfully saves the changes

Scenario 2:
Given I am a member of the philanthropy office, authenticated and on the student window.
When I try to update student information with invalid data
Then the system displays an error indicating the problem

**User Story 4 - Generation of Alerts for Cancellations**

Scenario 1:
Given I am a member of the philanthropy office, authenticated and on the student window.
When a student cancels subjects or makes withdrawals
Then I receive an alert indicating the change in the student's academic situation

Scenario 2:
Given I am a member of the philanthropy office, authenticated and on the student window.
And I have not set up alerts in the system
When a student cancels subjects or makes withdrawals
Then I do not receive any alert about the change

**User Story 5 - Donor Registration**

Scenario 1:
Given I am a member of the philanthropy office with permissions, authenticated and on the donor registration window.
When I enter the complete information of a new donor
Then the system successfully registers the donor

Scenario 2:
Given I am a member of the philanthropy office with permissions, authenticated and on the donor registration window.
When I try to register a donor without providing all required information
Then the system displays an error indicating the missing fields

**User Story 6 - Generation of Financial Reports**

Scenario 1:
Given I am a user of the philanthropy office, authenticated and on the financial reports window.
When I request a financial report on scholarship funds and donations
Then the system provides me with a detailed report for decision-making and financial planning

**User Story 7 - Management of Attached Documents**

Scenario 1:
Given I am a member of the philanthropy office and authenticated.
When I select a record and attach a relevant document
Then the system saves the attached document to the selected record

Scenario 2:
Given I am a member of the philanthropy office and authenticated.
When I try to attach an unsupported or invalid format file
Then the system displays an error indicating the issue with the selected file

**User Story 8 - Notification to Philanthropy**

Scenario 1:
Given I am a member of the Welfare office, authenticated and on the student window.
When I send a notification alert to the Philanthropy offices
Then the Philanthropy office receives the notification and can act according to the update

Scenario 2:
Given that I am a member of the Welfare Office, I am authenticated and in the student window,
When I try to send a notification but a system error occurs,
Then I receive an error message and the notification is not sent.