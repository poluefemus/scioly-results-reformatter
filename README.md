# 🏆 Science Olympiad Competition Results Parser
This Python script reformats data from [Duosmium](https://www.duosmium.org/results/), so teams can better analyze the performance of members without needing to constantly reference what events each member is participating in.

## ⚡ Features
- Import Duosmium results and your roster from Google Sheets directly via their urls
  - Local csv files work as well
- Distinguish between multiple teams automatically
- After importing the parsed results into Google Sheets or Excel, you can sort by name, team, or event.

## 🚀 Installation
```bash
git clone [https://github.com/poluefemus/scioly-results-reformatter.git](https://github.com/poluefemus/scioly-results-reformatter.git)
cd scioly-parser
pip install pandas requests
```

## 🛠 Usage 
```bash
python main.py <SchoolNameCamelCase> [duosmium_source] [roster_source]
```
The parameters in brackets are optional. The script will automatically search for a file called data.csv (for the results) and roster.csv (for the roster) if the links for Duosmium and Google Sheets are not provided. 

## 🛠 Example Usage ([test files]([url](https://github.com/poluefemus/scioly-results-reformatter/tree/main/example_files)))
Paste this into the terminal 
```bash
python main.py DuluthHighSchool https://www.duosmium.org/results/2025-10-25_uga_invitational_c/ https://docs.google.com/spreadsheets/d/1lqtl2DCOtr-68Ue3hICBALAMMCKYZuaqTsK-GH_4om8/edit?gid=0#gid=0
```
## 📸 Visuals

#### 1. Roster
Keep your team roster in Google Sheets or a CSV with student event assignments.
Try to keep the columns as Name, team, event1, event2, event3, and event4, so the program doesn't bug out.
<br>
<img src="https://github.com/user-attachments/assets/3feea86d-e42e-40c0-999e-cf550830bf8c" width="500" style="border: 1px solid #d0d7de; border-radius: 6px;" alt="Roster">

---

#### 2. Tournament Results
The script fetches official event rankings directly from Duosmium:
<br>
<img src="https://github.com/user-attachments/assets/a58de601-b0d8-41df-9d30-951ab4f3e486" width="700" style="border: 1px solid #d0d7de; border-radius: 6px;" alt="Official Results">

---

#### 3. Parsed Output Schedule
A new csv file is created with reformatted results that are easier to analyze.
<br>
<img src="https://github.com/user-attachments/assets/6404e1da-81e1-4d2d-9919-c8a32a03f21e" width="400" style="border: 1px solid #d0d7de; border-radius: 6px;" alt="Parsed Schedule">
