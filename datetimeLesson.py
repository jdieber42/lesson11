import datetime
import json

current_time = datetime.datetime.now()

print(type(current_time))
print(current_time)

with open("date.json", "w") as date_file:
    date_file.write(json.dumps(str(current_time)))

