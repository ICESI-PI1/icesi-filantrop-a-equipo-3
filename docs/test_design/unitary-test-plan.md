#Test Plan

**Unitary tests for student**

  preconditions: student must be created

- [x] Student can be created
- [x] Student can be updated
- [x] Student can be deleted
- [x] Student can be listed

*create*


|case|Input|Output|
|---|---|---|
|1|Correct student attributes |create student|
|2|Incorrect student attributes |error|
|3|atributes with an existign code|error|


*update*


|case|Input|Output|
|---|---|---|
|3|Correct student attributes |update student|
|4|Incorrect student attributes |error|


*delete*


|case|Input|Output|
|---|---|---|
|5|Correct student code |delete student|
|6|Incorrect student code |non delete|


*list*


|case|Input|Output|
|---|---|---|
|7|Correct student code |list student|
|8|Incorrect student code |non list|



**Unitary tests for alert**

preconditions: alert must be created

- [x] Alert can be created
- [x] Alert can be listed

*create*
|case|Input|Output|
|---|---|---|
|1|Correct alert attributes |create alert|
|2|Incorrect alert attributes |error|
|3|atributes with an existign code|error|

*list*
|case|Input|Output|
|---|---|---|
|4|Correct alert code |list alert|
|5|Incorrect alert code |non list|



**Unitary tests for Donor**

preconditions: donor must be created

- [x] Donor can be created
- [x] Donor can be updated
- [x] Donor can be deleted

*create*
|case|Input|Output|
|---|---|---|
|1|Correct donor attributes |create donor|
|2|Incorrect donor attributes |error|
|3|atributes with an existign code|error|

*update*
|case|Input|Output|
|---|---|---|
|4|Correct donor attributes |update donor|
|5|Incorrect donor attributes |error|

*delete*
|case|Input|Output|
|---|---|---|
|6|Correct donor code |delete donor|
|7|Incorrect donor code |non delete|


**Unitary tests for ExtraAcademic**

preconditions: extraAcademic must be created

- [x] ExtraAcademic can be created
- [ ] ExtraAcademic can be updated
- [ ] ExtraAcademic can be deleted
- [ ] ExtraAcademic can be listed

*create*
|case|Input|Output|
|---|---|---|
|1|Correct extraAcademic attributes |create extraAcademic|
|2|Incorrect extraAcademic attributes |error|
|3|atributes with an existign code|error|

*update*
|case|Input|Output|
|---|---|---|
|4|Correct extraAcademic attributes |update extraAcademic|
|5|Incorrect extraAcademic attributes |error|

*delete*
|case|Input|Output|
|---|---|---|
|6|Correct extraAcademic code |delete extraAcademic|
|7|Incorrect extraAcademic code |non delete|

*list*
|case|Input|Output|
|---|---|---|
|8|Correct extraAcademic code |list extraAcademic|
|9|Incorrect extraAcademic code |non list|


**Unitary tests for AcademicBalance**

preconditions: academicBalance must be created

- [x] AcademicBalance can be created
- [ ] AcademicBalance can be updated
- [ ] AcademicBalance can be deleted
- [ ] AcademicBalance can be listed

*create*
|case|Input|Output|
|---|---|---|
|1|Correct academicBalance attributes |create academicBalance|
|2|Incorrect academicBalance attributes |error|
|3|atributes with an existign code|error|

*update*
|case|Input|Output|
|---|---|---|
|4|Correct academicBalance attributes |update academicBalance|
|5|Incorrect academicBalance attributes |error|

*delete*
|case|Input|Output|
|---|---|---|
|6|Correct academicBalance code |delete academicBalance|
|7|Incorrect academicBalance code |non delete|

*list*
|case|Input|Output|
|---|---|---|
|8|Correct academicBalance code |list academicBalance|
|9|Incorrect academicBalance code |non list|

**Unitary tests for CreaQuery**

preconditions: creaQuery must be created

- [x] CreaQuery can be created
- [ ] CreaQuery can be updated
- [ ] CreaQuery can be deleted
- [ ] CreaQuery can be listed

*create*
|case|Input|Output|
|---|---|---|
|1|Correct creaQuery attributes |create creaQuery|
|2|Incorrect creaQuery attributes |error|
|3|atributes with an existign code|error|

*update*
|case|Input|Output|
|---|---|---|
|4|Correct creaQuery attributes |update creaQuery|
|5|Incorrect creaQuery attributes |error|

*delete*
|case|Input|Output|
|---|---|---|
|6|Correct creaQuery code |delete creaQuery|
|7|Incorrect creaQuery code |non delete|

*list*
|case|Input|Output|
|---|---|---|
|8|Correct creaQuery code |list creaQuery|
|9|Incorrect creaQuery code |non list|

**Unitary tests for PhilanthropyMember**

preconditions: philanthropyMember must be created

- [x] PhilanthropyMember can be created
- [ ] PhilanthropyMember can be updated
- [ ] PhilanthropyMember can be deleted
- [ ] PhilanthropyMember can be listed

*create*
|case|Input|Output|
|---|---|---|
|1|Correct philanthropyMember attributes |create philanthropyMember|
|2|Incorrect philanthropyMember attributes |error|
|3|atributes with an existign code|error|

*update*
|case|Input|Output|
|---|---|---|
|4|Correct philanthropyMember attributes |update philanthropyMember|
|5|Incorrect philanthropyMember attributes |error|

*delete*
|case|Input|Output|
|---|---|---|
|6|Correct philanthropyMember code |delete philanthropyMember|
|7|Incorrect philanthropyMember code |non delete|

*list*
|case|Input|Output|
|---|---|---|
|8|Correct philanthropyMember code |list philanthropyMember|
|9|Incorrect philanthropyMember code |non list|

**Unitary tests for Report**

preconditions: report must be created

- [x] Report can be created
- [ ] Report can be updated
- [ ] Report can be deleted
- [ ] Report can be listed

*create*
|case|Input|Output|
|---|---|---|
|1|Correct report attributes |create report|
|2|Incorrect report attributes |error|
|3|atributes with an existign code|error|

*update*
|case|Input|Output|
|---|---|---|
|4|Correct report attributes |update report|
|5|Incorrect report attributes |error|

*delete*
|case|Input|Output|
|---|---|---|
|6|Correct report code |delete report|
|7|Incorrect report code |non delete|

*list*
|case|Input|Output|
|---|---|---|
|8|Correct report code |list report|
|9|Incorrect report code |non list|

**Unitary tests for Collaborator**

preconditions: collaborator must be created

- [x] Collaborator can be created
- [ ] Collaborator can be updated
- [ ] Collaborator can be deleted
- [ ] Collaborator can be listed
  
*create*
|case|Input|Output|
|---|---|---|
|1|Correct collaborator attributes |create collaborator|
|2|Incorrect collaborator attributes |error|
|3|atributes with an existign code|error|

*update*
|case|Input|Output|
|---|---|---|
|4|Correct collaborator attributes |update collaborator|
|5|Incorrect collaborator attributes |error|

*delete*
|case|Input|Output|
|---|---|---|
|6|Correct collaborator code |delete collaborator|
|7|Incorrect collaborator code |non delete|

*list*
|case|Input|Output|
|---|---|---|
|8|Correct collaborator code |list collaborator|
|9|Incorrect collaborator code |non list|




