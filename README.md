# From Heart Rate to Hibernate: Exploring How Physical Activity Shapes Sleep Patterns

From Heart Rate to Hibernate investigates how physical activity influences sleep quality, using real-world data collected from Fitbit wearables. The primary aim of this analysis is to uncover patterns and correlations between daily movement metrics—like step count, active minutes, and heart rate—and key sleep indicators such as total sleep duration, sleep efficiency, and percentage of time in each sleep level.


## Table of Contents

- [From Heart Rate to Hibernate: Exploring How Physical Activity Shapes Sleep Patterns](#from-heart-rate-to-hibernate-exploring-how-physical-activity-shapes-sleep-patterns)
- [Table of Contents](#table-of-contents)
- [Objectives](#objectives)
- [Project Setup](#project-setup)
   - [Virtual Environment Commands](#virtual-environment-commands)
- [Data Source](#data-source)
- [How to run program](#how-to-run-program)
- [Data Dictionary](#data-dictionary)
- [Tech Used](#tech-used)
- [Project Summary](#project-summary)
- [Tableau Public Dashboard](#tableau-public-dashboard)
- [Dedication](#dedication)


## Objectives:

1. Quantify correlations between exercise intensity and sleep quality.

2. Identify trends or thresholds where activity most positively impacts rest.

3. Translate raw metrics into actionable insights for optimizing daily routines.


## Project Setup

In order to run this project:
1. Clone the repository
     - Above the list of files, click <>Code.
     - Copy the URL for the repository.
     - Open Git Bash.
     - Change the current working directory to the location where you want the cloned directory.
     - Type git clone, and then paste the URL you copied earlier.
     - Press Enter to create your local clone.
2. Open the repository in the IDE of your choice.
3. Use the following commands to enter the virtual environment and install the requirements.txt file: 


### Virtual Environment Commands
| Command | Linux/Mac | Windows |
| ------- | --------- | ------- |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` |


## Data Source

All the data files were exported from my Fitbit account. The file types were CSV and JSON. To download you own Fitbit data, use the following steps:
 1. On the [Fitbit settings](https://accounts.fitbit.com/login?targetUrl=https%3A%2F%2Fwww.fitbit.com%2Flogin%2Ftransferpage%3Fredirect%3Dhttps%25253A%25252F%25252Fwww.fitbit.com%25252Fsettings%25252Fprofile%25253Fsjid%25253D2794903053053765236-NA&lcl=en_US) page, click Data Export ​​​​​​​under the Settings menu.
 2. Choose the time period and data you want to include, and the file format.
 3. Click Create Export.
 
#### Once the files have been downloaded from your Fitbit account., navigate to the Takeout folder that was downloaded and move the following files to the corresponding folder in your local repository based on file type:

#### Note: if you are going to use your own Fitbit data, you wil need to empty out the Raw CSV folder and Raw JSON folder in the repository before proceeding.

1. Active Zone Minutes (moved to Raw CSV folder in repo) - located using the following path:
      - \Takeout\Fitbit\Active Zone Minutes (AZM)
2. Heart Rate (moved to Raw CSV folder in repo) - located using the following path:
      - \Takeout\Fitbit\Physical Activity_GoogleData
3. Steps (moved to Raw CSV folder in repo) - located using the following path:
      - \Takeout\Fitbit\Physical Activity_GoogleData
4. Sleep (moved to Raw JSON folder in repo) - located using the following path:
      - \Takeout\Fitbit\Global Export Data


## How to run program
If you downloaded your own Fitbit data and moved the corresponding above files to the correct folders, you will want to run all the scripts. Starting with the python scripts:

- Python
  - combining_and_cleaning_AZM.py
  - combining_and_cleaning_HR.py
  - combining_and_cleaning_STEPS.py
  - combining_and_flattening_SLEEP.py

After you run all the Python scripts, you can open up each of the Jupyter Notebooks and click "Run All" at the top of the notebook. 

- Jupyter Notebook
  - cleaning_sleep_data.ipynb
  - forming_sql_database.ipynb

This will output a final CSV file titled "cleaned_total_data.csv". This CSV file will contain all the cleaned and concatenated data. 


## Data Dictionary
| Column | Description | Data Type |
| ------- | --------- | --------- | 
| date | Date that the data was collected. | object |
| active_zone_minutes | Total number of minutes that my heart rate was above 117 beats per minute. | int64 |
| avg_beats_per_minute | Average of the day's beats per minute. | float64 |
| total_steps_taken | Number of recorded steps. | int64 |
| date_of_sleep | The date the sleep log ended. | object |
| sleep_start_time | Time the sleep log started. | object |
| sleep_end_time | Time the sleep log ended. | object |
| sleep_duration | Length of the sleep in milliseconds. | int64 |
| minutes_asleep | The total number of minutes the user was asleep. | int64 |
| minutes_awake | The total sum of "wake" minutes only. It does not include before falling asleep or after waking up. | int64 |
| minutes_after_wakeup | The total number of minutes after the user woke up. | int64 |
| time_in_bed | Total number of minutes the user was in bed. | int64 |
| sleep_efficiency | Calculated sleep efficiency score. (sleep efficiency = minutesAsleep/timeInBed) |int64 |
| sleep_type | The type of sleep log. (Classic = restless, asleep, and wake. Stages = deep, light, rem, and wake.) | object |
| sleep_info_code | An integer value representing the quality of data collected within the sleep log. (0 = Sufficient data to generate a sleep log. 1 = Insufficient heart rate data. 2 = Sleep period was too short (less than 3 hours). 3 = Server-side issue when generating the sleep log. No data impact.) | int64 |
| main_sleep | Boolean value: true or false | bool |
| sleep_restless_count | Total number of times the user entered the sleep level of restless. | float64 |
| sleep_restless_minutes | Total number of minutes the user appeared in the sleep level of restless. | float64 |
| sleep_awake_count | Total number of times the user entered the sleep level of awake. | float64 |
| sleep_awake_minutes | Total number of minutes the user appeared in the sleep level of awake. | float64 |
| sleep_asleep_count | Total number of times the user entered the sleep level of asleep. | float64 |
| sleep_asleep_minutes | Total number of minutes the user appeared in the sleep level of asleep. | float64 |
| sleep_deep_count | Total number of times the user entered the sleep level of deep. | float64 |
| sleep_deep_minutes | Total number of minutes the user appeared in the sleep level of deep. | float64 |
| sleep_deep_thirtyDayAvgMinutes | The average deep sleep stage time over the past 30 days. A sleep stage log is required to generate this value. When a classic sleep log is recorded, this value will be missing. | float64 |
| sleep_wake_count | Total number of times the user entered the sleep level of wake. | float64 |
| sleep_wake_minutes | Total number of minutes the user appeared in the sleep level of wake. | float64 |
| sleep_wake_thirtyDayAvgMinutes | The average wake sleep stage time over the past 30 days. A sleep stage log is required to generate this value. When a classic sleep log is recorded, this value will be missing. | float64 |
| sleep_light_count | Total number of times the user entered the sleep level of light. | float64 |
| sleep_light_minutes | Total number of minutes the user appeared in the sleep level of light. | float64 |
| sleep_light_thirtyDayAvgMinutes | The average light sleep stage time over the past 30 days. A sleep stage log is required to generate this value. When a classic sleep log is recorded, this value will be missing. | float64 |
| sleep_rem_count | Total number of times the user entered the sleep level of rem. | float64 |
| sleep_rem_minutes | Total number of minutes the user appeared in the sleep level of rem. | float64 |
| sleep_rem_thirtyDayAvgMinutes | The average rem sleep stage time over the past 30 days. A sleep stage log is required to generate this value. When a classic sleep log is recorded, this value will be missing. | float64 |


## Tech Used
All coding was done using Python. Pandas was used within Juypter Notebook for data analysis and data manipulation. SQLite was used to create my database. Everything was coded within the Visual Studio Code IDE. Tableau Public was used for visualizations. 


## Project Summary 
While exercise intensity does appear to influence sleep quality to some extent, my findings suggest it's only one piece of a much larger puzzle. Sleep is shaped by a complex interplay of factors including stress levels, diet, screen time, and individual physiology that go beyond physical activity alone.

### 1. Quantify correlations between exercise intensity and sleep quality.

| Step Range | Primary Sleep Stage Correlated with Higher AZM |
| ------- | --------- |
| 0–2,499 steps | Light Sleep |
| 2,500–4,999 steps | 	Deep Sleep |
| 5,000–7,499 steps | Light Sleep |
| 7,500–9,999 steps | REM Sleep |
| 10,000+ steps | Deep Sleep |

These findings suggest that the impact of exercise intensity on sleep architecture may shift depending on overall activity level. For example, medium activity (2,500–4,999 steps) appears to enhance restorative deep sleep, while higher activity levels (7,500–9,999 steps) may promote more REM sleep, associated with cognitive processing and memory.

### 2. Identify trends or thresholds where activity most positively impacts rest.

- Low Activity (0–2,499 steps): Increased AZM show modest gains in light sleep, but overall rest remains limited. Suggesting minimal movement may not be sufficient to trigger deeper restorative sleep stages.
- Moderate Activity (2,500–4,999 steps): This range marks a noticeable shift, where higher AZM correlates most strongly with deep sleep, indicating that even moderate movement paired with intensity can enhance physical recovery.
- Mid-High Activity (5,000–7,499 steps): AZM again aligns with light sleep, possibly reflecting a plateau effect where intensity supports rest but doesn’t yet push into deeper sleep stages.
- High Activity (7,500–9,999 steps): A compelling trend emerges here. AZM correlates most with REM sleep, which is critical for cognitive processing and memory.
- Very High Activity (10,000+ steps): At this threshold, AZM is most strongly linked to deep sleep, suggesting that sustained movement and intensity may optimize physical recovery and overall sleep architecture.

These thresholds suggest that moderate-to-high activity levels, especially when paired with higher (AZM), are most effective in promoting restorative sleep stages. The sweet spot appears to be between 2,500 and 10,000 steps, where different sleep stages are selectively enhanced depending on the activity profile.

### 3. Translate raw metrics into actionable insights for optimizing daily routines.
- Low Activity (0–2,499 steps)
  - Insight: Minimal movement yields only slight improvements in light sleep.
  - Action: Prioritize short, high-intensity bursts such as brisk short walks to boost AZM without needing high step counts.

- Moderate Activity (2,500–4,999 steps)
  - Insight: This range correlates most with deep sleep which is necessary for physical recovery. 
  - Action: Target this zone on rest days or when recovery is a priority. Add moderate-intensity movement like cycling or yoga to maximize deep sleep benefits.

- Mid-High Activity (5,000–7,499 steps)
  - Insight: AZM aligns with light sleep, suggesting a maintenance effect.
  - Action: Use this range for steady-state days ideal for maintaining rhythm without overexertion. Great for mental reset or low impact cardio.

- High Activity (7,500–9,999 steps)
  - Insight: Strong correlation with REM sleep, which supports memory and cognitive processing.
  - Action: Schedule cognitively demanding tasks such learning and problem-solving the day after hitting this range. Prioritize mental recovery.

- Very High Activity (10,000+ steps)
  - Insight: Deep sleep returns as the dominant benefit, indicating optimal physical restoration.
  - Action: Use this threshold for peak training days. Pair with proper nutrition and wind-down routines to fully capitalize on recovery potential.

By aligning your movement patterns with sleep outcomes, you can strategically design your day whether you're aiming for recovery, mental clarity, or performance.

## Tableau Public Dashboard
[Link to my Tableau Public visualizaion](https://public.tableau.com/views/FitbitDashboard_17549512206080/FitbitDataDashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


### Dedication
This project is dedicated to my late wife. She is the one who inspired me to reach out of my comfort zone and better myself through furthering my knowledge base. 