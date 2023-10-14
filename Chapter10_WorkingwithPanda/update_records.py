import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_world_records_in_swimming"

tables = pd.read_html(URL)

RECORDS = (0, 2, 4, 5)
COURSES = ("LC Men", "LC Women", "SC Men", "SC Women")

records = {}

records = {}
for table, course in zip(RECORDS, COURSES):
    df = tables[table][["Event", "Time"]]
    df = df = df[~df["Event"].str.contains("relay")]
    df = df.set_index("Event")
    records[course] = df.to_dict()["Time"]
