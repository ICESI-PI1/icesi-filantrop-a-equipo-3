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



