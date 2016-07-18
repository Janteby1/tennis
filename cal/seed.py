import csv 
from cal.models import Tags         

# '''
# to run
# 1) python3 manage.py shell
# 2) from cal.seed import seed
# 3) seed()
# '''

def seed():
    "This seeds the db from a tab seperated file without using csv reader"
    # open text file for reading
    with open("cal/seed.txt", "r") as seed_file:

    # iterate across each line
        for line in seed_file:
            tags = line.split(",")

            for tag in tags:
                print (tag)
                tag = Tags(name=tag)
                tag.save()
            print ("\n All Done")
