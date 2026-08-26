# 🏆 Science Olympiad Competition Results Parser
This Python script reformats data from [Duosmium](https://www.duosmium.org/results/), so teams can better analyze the performance of members without needing to constantly reference what events each member is participating in.

## ⚡ Features
- Import Duosmium results and your roster from Google Sheets directly via their urls
  - Local csv files work as well
- Distinguish between multiple teams automatically
- After importing the parsed results into Google Sheets or Excel, you can sort by name, team, or event.

## 🚀 Installation
```bash
git clone [https://github.com/your-username/scioly-parser.git](https://github.com/your-username/scioly-parser.git)
cd scioly-parser
pip install pandas requests
```

## Usage 
```bash
python main.py <SchoolNameCamelCase> [duosmium_source] [roster_source]
```

## Example (you can download the files in the examples folder to test)
```bash
python meets/d/1lqtl2DCOtr-68Ue3hICBALAMMCKYZuaqTsK-GH_4om8/edit?gid=0#gid=0
```
Roster: <img width="607" height="695" alt="image" src="https://github.com/user-attachments/assets/3feea86d-e42e-40c0-999e-cf550830bf8c" />
Official Results: <img width="1162" height="916" alt="image" src="https://github.com/user-attachments/assets/a58de601-b0d8-41df-9d30-951ab4f3e486" />
Parsed Results: <img width="474" height="710" alt="image" src="https://github.com/user-attachments/assets/6404e1da-81e1-4d2d-9919-c8a32a03f21e" />
