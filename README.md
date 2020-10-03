# Requirement for this project for setup:<br/>

-> Create a vitual environment.<br/>
== virtualenv -p python3.6 venv<br/>
-> Activate your virtual environment using this command<br/>
== source venv/bin/activate<br/>
-> Install required python libraries by using pip installer.<br/>
== pip install -r requirements.txt<br/>
-> Migrate database.<br/>
== python manage.py migrate<br/>
-> Finally, run your django runserver.<br/>
== python manage.py runserver<br/>

# Two API's work around to this Project.

# (POST) First Api Gateway where we can pass valid request and in response valid reponse.

like:- 

    Request =  {
        "amount": "100",
        “currency”: "USD",
        "type": "creditcard",
        "card": {
            "number": "4111111111111111",
            "expirationMonth": "2",
            "expirationYear": "2020",
            "cvv": "111"
            }
        }

    Response = {
        "amount": "100",
        “currency”: “USD”,
        “type”: “creditcard”
        "card": {
            "number": "4111111111111111"
        }
        “status”: “success”,
        “authorization_code”: “SDSD23232333”
        “time”: “2020-05-16 07:00:00”
    }

    Error Respinse = {
        "amount": "100",
        "currency": "100",
        "type": "100",
        "card": {
            "number": "100"
        },
        "status": "error",
        "error": "'expirationYear'was not present in the response",
        "authorization_code": "Jaytlpzepdcw"
        "time": "2020-10-02 19:00:16.744329",
    }


# (GET) Second Api All Transactions History response (Success + Error).

like:-

    Response = [
        [
            1,
            {
                "card": {
                    "number": "100"
                },
                "time": "2020-10-02 19:00:16.413080",
                "type": "100",
                "error": "'expirationYear'was not present in the response",
                "amount": "100",
                "status": "error",
                "currency": "100",
                "authorization_code": "Nkxw0lunfkq5"
            }
        ],
        [
            2,
            {
                "card": {
                    "number": "100"
                },
                "time": "2020-10-02 19:00:16.744329",
                "type": "100",
                "error": "'expirationYear'was not present in the response",
                "amount": "100",
                "status": "error",
                "currency": "100",
                "authorization_code": "Jaytlpzepdcw"
            }
        ],
        [
            3,
            {
                "card": {
                    "number": "100"
                },
                "time": "2020-10-02 19:01:51.073078",
                "type": "100",
                "amount": "100",
                "status": "success",
                "currency": "100",
                "authorization_code": "E3boeq1gheut"
            }
        ] ............................................
    ]
