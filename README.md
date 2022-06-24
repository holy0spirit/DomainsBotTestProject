# Backend Python Developer for Distributed Company 
###### NEW
## DomainsBot.com

 This is a test project requirement for [DomainsBot Job Application](https://www.python.org/jobs/6640/)

To test the project:

download [Source Code](https://github.com/holy0spirit/DomainsBotTestProject.git)

install virtual environment: ```pip install virtualenv```

create virtual environment: ```virtualenv myenv```

activate virtual environment: ```virtualenv/scripts/activate```

install requirements.txt File: ```pip install -r requirements.txt in your shell.```

download [Postman](https://www.postman.com/)

launch your app: ```flask run```

> copy endpoints to postman for testing

 [ ] / - default endpoint

returns
```
{
    "data": "end-point successful",
    "status": "200"
}
```

[ ] /palindrome - Task 1 [Write a function that tells you whether a word is a palindrome. A palindrome is a word or a phrase that is the same whether you read it backwards or forwards, for example the word ‘refer’. On the other hand, ‘refers’ is not a palindrome.]

returns:
```
{
    "message": "False, it is not a Palindrome Text",
    "original-text": "refers",
    "palindrome-text": "srefer",
    "status": "200"
}
```
or
```
{
    "message": "True, it is a Palindrome Text",
    "original-text": "refer",
    "palindrome-text": "refer",
    "status": "200"
}
```

[ ] /lenghty - Task 2 [Write a function which, given a string, finds the length of the longest sub-string without repeating characters.]

returns:

```
{
    "character": "refs",
    "lenght": 4,
    "status": "200",
    "sub-string": "refers"
}
```

All Methods are POST if not you recieve this error:
```
{
    "message": "Method Not Allowed",
    "status": "405"
}
```
Any other error cases will return:
```
{
    "status" : "503", 
    "message" : "App Crash"
}
```
