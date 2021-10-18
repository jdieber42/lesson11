import json

"""
{
    "people":[
        {
            "name": "Tina",
            "age": 23,
            "gender": "female"
        },

        {
            "name": "Jakob",
            "age": 35,
            "gender": "male"
        },

        {
            "name": "Barbara",
            "age": 44,
            "gender": "female"
        }
    ]
}
"""

person = {"name": "Tina", "age": 23, "gender": "female"}
person1 = {"name": "Jakob", "age": 35, "gender": "male"}
person2 = {"name": "Barbara", "age": 44, "gender": "female"}


list = [person, person1, person2]
dict = {"people": list}

print(list)

with open("people.json", "w") as people_file:
    people_file.write(json.dumps(dict))