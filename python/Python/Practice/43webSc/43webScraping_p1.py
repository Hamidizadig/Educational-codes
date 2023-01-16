import re                  # https://regex101.com
conf="""
Conference1
Topic: Object Oriented Programming
Date: 09/20/2022
Location: USA
Web: conf.usa/09/2022
Cost: $1200
Conference2
Topic:    Python3
Date: 01/31/2022
Location: France
Web: conf.france/01/2022
Cost: $600
Conference3
Topic: Data Science
Date: 07/09/2022
Location: UK
Web: conf.org
Topic: Object Oriented Programming2
Date: 09/21/2022
Cost: $900
Conference4
Topic: Web Development
Date: 08/29/2022
Location: Canada
Web: conf.ca
Cost: $1100
Conference5
Topic: Python for Beginners
Date: 05/09/2022
Location: Turkey
Web: conf.com/03/2022
Cost: $900000
"""
# topic_list=re.findall(r"Topic:\s*(.+)",conf)
# print(topic_list)

# date_list=re.findall(r"Date:\s*(\d\d/\d\d/\d{4})",conf)
# print(date_list)

# date_month_list=re.findall(r"Date:\s*(\d\d/)\d\d/\d{4}",conf)
# print(date_month_list)

# year_list=re.findall(r"Date:\s*\d\d/\d\d/(\d{4})",conf)
# print(year_list)

# topic_list=re.findall(r"Web:\s*conf\.\w+/(\d\d/2022)",conf)
# print(topic_list)

# web_list=re.findall(r"Topic:\s*(.+)\sDate:\s*09/\d\d/\d{4}",conf)
# print(web_list)

newCost=re.sub(r"Cost:\s*\$\d{2,4}\s","Cost: $555\n",conf)
print(newCost)
