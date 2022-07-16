# Google-Analytics-URL-Explainer
A Python script that reads the parameters in a GET google-analytics.com/collect call.  

## Input: 
Requests an URL in the terminal, either a file containing a list of URLs, each one delimited by a new line, or a single URL.  

## Output:
Either a `.txt` file containing the explanation or a newly created directory containing a file for every single URL processed if the script was called for a single URL or for a file containing multiples respectively. The file or directory is named at the date and time of when the script was called.  

## Examples:

### Call a single URL in terminal:
Call in terminal:  
![image](https://user-images.githubusercontent.com/62748111/179368862-2dce735f-1333-44d0-a83d-c44afb43c501.png)

Output:  
![image](https://user-images.githubusercontent.com/62748111/179369005-d90e354e-b3ae-4bf8-82f9-10f962011513.png)


### Call Multiple URLs that are in a text file:
Call in terminal:  
![image](https://user-images.githubusercontent.com/62748111/179369048-8bced4b6-cd37-489e-841f-d508c3f1044d.png)

Output:  
![image](https://user-images.githubusercontent.com/62748111/179369057-ab5fe3d9-aa7b-4d18-b8b0-556c5e59e853.png)

