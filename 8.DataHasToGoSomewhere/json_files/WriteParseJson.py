menu = {
    "breakfast": {
        "hours": "7-11",
        "items": {
            "breakfast burritos": "$6.00",
            "pancakes": "$4.00"
        }
    },
    "lunch": {
        "hours": "11-3",
        "items": {
            "hamburger": "$5.00"
        }
    },
    "dinner": {
        "hours": "3-10",
        "items": {
            "spaghetti": "$8.00"
        }
    }
}

import json
menu_json = json.dumps(menu)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)

# Working with datetimes...
import datetime
now_str = str(datetime.datetime.now())
json.dumps(now_str)
from time import mktime
int(mktime(datetime.datetime.now().timetuple()))