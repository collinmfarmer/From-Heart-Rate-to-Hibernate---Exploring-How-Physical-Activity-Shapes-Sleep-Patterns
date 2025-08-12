# From Heart Rate to Hibernate: Exploring How Physical Activity Shapes Sleep Patterns

From Heart Rate to Hibernate investigates how physical activity influences sleep quality, using real-world data collected from Fitbit wearables. The primary aim of this analysis is to uncover patterns and correlations between daily movement metrics—like step count, active minutes, and heart rate variability—and key sleep indicators such as total sleep duration, sleep efficiency, and restlessness.




## Objectives:

1. Quantify correlations between exercise intensity and sleep quality

2. Identify trends or thresholds where activity most positively impacts rest

3. Translate raw metrics into actionable insights for optimizing daily routines




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
 3. Click Download.
 
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


## Steps to run program
??????????????????????????????????????????


## Data Dictionary
| Column | Description | Data Type |
| ------- | --------- | --------- | 
| date | Date that data was collected. | object |
| active_zone_minutes | Total number of minutes that my heart rate was above 117 BPM. | int64 |
| avg_beats_per_minute | Average of the day's BPM. | float64 |
| total_steps_taken | Number of recorded steps. | int64 |
| date_of_sleep | The date the sleep log ended. (Shifted back by one day) | object |
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
| sleep_awake_count | Total number of times the user entered the sleep level if awake. | float64 |
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




## Project Summary 
????????????????????????????????????????????????????