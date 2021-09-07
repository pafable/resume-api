import datetime

def employment_date(year: int, month: int) -> str:
    z = datetime.date(year, month, 1)
    z = z.strftime("%B %Y")

    return z

ME = {

    "background": "DevOps/SRE Engineer based in Boston! :D",
    "first_Name": "Philip",
    "last_name": "Afable",
    "help": "Go to /docs"
}

JOBS_DATA = {

    "jobs": [
        {         
            "employer": "Sophos", 
            "title": "Systems Engineer", 
            "location": "Burlington, MA",
            "start_date": employment_date(2019, 4), 
            "end_date": None,
            "intern": False,
            "contractor": False
        },
        {         
            "employer": "PTC", 
            "title": "Cloud Engineer", 
            "location": "Needham, MA",
            "start_date": employment_date(2017, 1), 
            "end_date": employment_date(2019, 4),
            "intern": False,
            "contractor": False
        },
        {         
            "employer": "NWN", 
            "title": "Solutions Engineer", 
            "location": "Waltham, MA",
            "start_date": employment_date(2015, 7), 
            "end_date": employment_date(2016, 12),
            "intern": False,
            "contractor": False
        },
        {        
            "employer": "EMC", 
            "title": "Network Operation Intern", 
            "location": "Southborough, MA",
            "start_date": employment_date(2015, 2), 
            "end_date": employment_date(2015, 6),
            "intern": True,
            "contractor": False
        },  
        {
            "employer": "Suffolk Construction", 
            "title": "Business Systems Intern", 
            "location": "Boston, MA",
            "start_date": employment_date(2014, 9), 
            "end_date": employment_date(2015, 1),
            "intern": True,
            "contractor": False
        }
    ]

}

EDU_DATA = {

    "education": [
        {
            "school": "Western Governor's University",
            "degree": "BS, Information Technology",
        },
        {
            "school": "Bunker Hill Community College",
            "degree": "AS, Computer Information Technology"
        }
    ] 

}