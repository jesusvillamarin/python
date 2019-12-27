<!--- 
    BEGIN...
    THIS WILL NEED TO EXECUTE CALCULATOR.PY
 -->
### Create a virtual enviroment to python
> py -3 -m venv .venv
    OR
> python3 -m venv venv


Install matplotlib on python
> python -m pip install matplotlib
<!-- ...END -->

Data types on python
* int
* float
* str
* bool
* complex
* dictionary
* tuple


### Define functions on python

    def name_function:
        algorith to execute...

    def name_function(var1, var2, var3):
        print(var1,var2,var3)
    
    def name_function(var1, *, var2, var3):
        <!-- IS OBLIGATORY CALL THE FUNCTION AND PASS THE ARGS WITH NAME AFTER THE ASTERISK -->
        <!-- THE ARGS BEFORE THE ASTERISK SHOULD BE PASS WITH NAME OR BY POSITION -->

### Call the function

 > name_function ---- THE FIRST FUNCTION WITHOUT PARAMETERS
 > name_function(var1 = 10, 30, var3 = 20) --- CALL FUNCTION AND PASSING ARGS WITH NAME AND POSITION
 > name_function(10, var2 = "Obligatory args with name", var3 = "the same that var2")
