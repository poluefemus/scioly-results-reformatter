import pandas as pd

data_df = pd.read_csv("data.csv")
roster_df = pd.read_csv("roster.csv")

results = data_df.loc[(data_df["school"] == "Duluth High School")]

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

export_df.to_csv("final_schedule.csv", index=False)


