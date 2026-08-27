import pandas as pd
import requests
import re
import sys
import io
import os

def load_csv(source: str):
    if source.startswith("https://"):
        url = source
        # This changes the link of google sheets to allow you to directly download the csv
        if "docs.google.com/spreadsheets" in url:
            gid_match = re.search(r'[#&?]gid=([0-9]+)', url)
            gid = gid_match.group(1) if gid_match else "0"

            base_url = url.split('/edit')[0]
            url = f"{base_url}/export?format=csv&gid={gid}"
        elif "duosmium.org" in url:
             url = url.replace("duosmium.org/results/", "duosmium.org/results/csv/")

        try:
            response = requests.get(url)
            response.raise_for_status() 
        except requests.exceptions.RequestException as err:
            print(f"If you pass in a roster link, make sure that the spreadsheet isn't under a school managed google account and enable anyone with the link to open it.")
            sys.exit(1)
        return pd.read_csv(io.StringIO(response.text))
    else:
        if os.path.exists(source):
            return pd.read_csv(source)
        sys.exit(1)

    
if len(sys.argv) < 2:
    print("Usage: python main.py <SchoolNameCamelCase> [duosmium_csv_url] [roster__csv_link]")
    sys.exit(1)

school = re.sub(r'([A-Z])', r' \1', sys.argv[1]).strip()

duosmium_source = sys.argv[2] if len(sys.argv) > 2 else "data.csv"
roster_source = sys.argv[3] if len(sys.argv) > 3 else "roster.csv"

data_df = load_csv(duosmium_source)
roster_df = load_csv(roster_source)

results = data_df.loc[(data_df["school"] == school)]

# Checks if they typed in the school name right
if results.empty:
    print("Check if you typed in the school name correctly")
    sys.exit(1)

metadata_cols = [
    "number",
    "school",
    "team",
    "exhibition",
    "city",
    "state",
    "track",
    "rank",
    "total",
]

# This is used to get all the event columns (ignores any colums in metadata_cols)
event_cols = [cols for cols in data_df.columns if cols not in metadata_cols]

results_long = results.melt(
    id_vars = "team",
    value_vars = event_cols, 
    var_name = "Events",
    value_name = "Score"
)

roster_results = roster_df.melt(
    id_vars = ["Name", "team"],
    value_vars = [cols for cols in roster_df.columns if cols.startswith("event")],
    value_name = "Events"
).drop(columns=["variable"])

export_df = roster_results.merge(results_long, on=["team", "Events"]).drop_duplicates()
export_df = export_df.rename(columns={"team":"Team"})

export_df.to_csv("parsed_results.csv", index=False)
