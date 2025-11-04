import re

phone_number_pattern_obj_us = re.compile(r"\d{3}-\d{3}-\d{4}")
phone_number_pattern_obj_BR = re.compile(r"\d{5}-\d{4}")
match_obj_us = phone_number_pattern_obj_us.search("My number is 444-555-8888")
match_obj_BR = phone_number_pattern_obj_BR.search("The phone number of my friend is 98875-5982")

print(match_obj_us.group())
print(match_obj_BR.group())
