# 🚴‍♀️ Apex Rides 2024‑25 Reports  
### *Rides Analysis & Dashboarding Project*  

---

## 📘 Project Overview  

The **Apex Rides 2024‑25 Reports** project dives deep into **12 months of Divvy/Lyft bike‑share data (April 2024 → March 2025)**, exploring how Chicago’s riders move through their city.  
Through **SQL‑based data preparation**, **Excel analysis**, and dynamic **Tableau dashboards**, this project transforms **5.78 million rides** into clear stories of commuter patterns, seasonal shifts, and station‑level activity.

This project is part of the **Data Analysis Projects** repository, alongside *Food Adverse Event Analysis* and other case studies showcasing applied data storytelling techniques across domains.

---

## 🧩 Objectives  

- Explore how **rider type (Casual vs Member)** affects ride frequency and duration.  
- Identify **weekly and monthly riding trends.**  
- Analyze **bike‑type preferences** – classic bike, e‑bike, and e‑scooter.  
- Highlight **top active stations** and **daily commuting patterns.**  
- Develop an **interactive Tableau dashboard** for data‑driven exploration.  

---

## 📊 Dashboard Highlights  

### **1️⃣ Ride Statistics Overview**

![Apex Dashboard](Apex Rides Reports (Rides Analysis and Dashboarding)/Snapshots/Ride1.png)

- **Total Rides:** 5.78 million  
- **Average Daily Rides:** 15,834  
- **Members vs Casuals:**  
  - **Members:** 3.64 million (≈ 63%)  
  - **Casuals:** 2.14 million (≈ 37%)  
- **Most Active Day:** **Sat, Sept 21 2024 → 34,698 rides**  
- **Least Active Day:** **Tue, Jan 21 2025 → 1,309 rides**  
- **Peak Quarter:** Q3 (2.33 million rides ≈ 40%)  

**Ride Type Breakdown:**  
- 🚲 Classic Bikes → **44.7 %**  
- ⚡ E‑Bikes → **52.8 %**  
- 🛴 E‑Scooters → **2.5 %** (Expected to be low since it was launched later in the year)

> 💡 On an average summer weekend day, rides were almost **20× higher** than on the coldest winter weekday!

---

### **2️⃣ Ride Trends & Patterns**

![Ride Trends](https://github.com/CodeCode1990/Data-Analysis-Projects/Apex%20Rides%20Reports%20(Rides%20Analysis%20and%20Dashboarding)/Snapshots/Ride2.png)

**When do people ride the most?**  
- **Members** dominate weekdays → daily commuting behavior.  
- **Casual riders** flood weekends → tourism & leisure rides.  

**Monthly bike type usage:**  
- **June → September 2024**: over **700 K rides per month** – summer surge!  
- **E‑Bikes** show steady year‑round presence.  
- **Classic bikes** peak in summer (≈ 60 % of rides during May–Sept).  

**Notable observations:**  
- *August and September 2024* record highs – outdoor festivals & tourism season.  
- *January 2025* marks the lowest ridership – cold weather deterrent.

---

### **3️⃣ Utilization Insights**

![Utilization Insights](https://github.com/CodeCode1990/Data-Analysis-Projects/Apex%20Rides%20Reports%20(Rides%20Analysis%20and%20Dashboarding)/Snapshots/Ride3.png)

**Top 10 Start Stations:**  
1. Streeter Dr & Grand Ave  
2. DuSable Lake Shore Dr & Monroe St  
3. Kingsbury St & Kinzie St  
4. Michigan Ave & Oak St  
5. Clark St & Elm St  
6. Clinton St & Washington Blvd  
7. Millennium Park  
8. Clinton St & Madison St  
9. Wells St & Concord Ln  
10. Theater District Hub  

Central locations and tourism corridors dominate – Downtown and lakeside stations drive over **25 % of all ride starts**.

**Time‑of‑day utilization:**  
- **Morning & evening peaks:** 7 a.m.–9 a.m. and 4 p.m.–6 p.m.  
- **Casual ridership spikes:** late mornings through sunset (11 a.m.–7 p.m.).  

---

## 🧮 Ride Duration Categories  

| Category | Duration | Share | Behavioral Snapshot |
|-----------|-----------|--------|----------------|
| **Short Ride** | < 10 min | **47 %** | Quick hops – typical work commute trips. |
| **Medium Journey** | 10–20 min | **29 %** | Short errands and cross‑town routes. |
| **Extended Trip** | 20–40 min | **14 %** | Scenic leisure rides & park loops. |
| **Long Haul** | > 40 min | **6 %** | Fitness or long‑trail rides. |
| **Quick Spin** | < 2 min | **4 %** | Short tests or docking retries. |

---

## 🧠 Key Findings and Business Insights  

| No. | Insight | Implication |
|:---:|:------------------------------|:------------------------------------------------|
| 1 | **Peak utilization in Q3 (2.32 M rides).** | Resource & maintenance planning should prioritize summer. |
| 2 | **Members ride twice as much as casuals.** | Indicates steady daily‑use culture and strong retention. |
| 3 | **Casuals form 38 % of total rides.** | Marketing opportunity → target leisure users & tourists. |
| 4 | **E‑Bikes outpace Classic Bikes.** | Growing adoption of electric mobility → invest in charging hubs. |
| 5 | **Morning/evening peaks reflect commuter hours.** | Ideal timing for dynamic pricing or off‑peak maintenance. |

---

## 🧾 Tools & Techniques  

| Step | Tools / Methods |
|------|----------------|
| **Data Source** | Divvy Trip Data (Apr 2024 – Mar 2025) |
| **Source of Data** | Excel |
| **Data Cleaning & Transformation** | SQL Server 2019 – scripts for merging & duration segmentation |
| **Visualization & Dashboarding** | Tableau Desktop (multi‑page dashboard) |
| **Version Control & Collaboration** | Git + GitHub |
| **External Dataset Host** | Google Drive |

---

## 📦 Dataset Sources  

- **Public Divvy Trip Data:**  
  [https://divvy-tripdata.s3.amazonaws.com/index.html](https://divvy-tripdata.s3.amazonaws.com/index.html)  
  *(April 2024 → March 2025 data files.)*  

- **Merged Dataset:**  
  [Google Drive Link (All Tables CSV)](https://drive.google.com/file/d/1HZyLsccJLyCGti4Kkfs__tAaQIZmMmfl/view?usp=drive_link)

---

## 🧭 How to Recreate the Analysis  

1. **Download Data**  
   - From the URLs above (CSV files Apr 2024 → Mar 2025).  
2. **Import to SQL Server / SQLite**  
   - Run `Merging_tables.sql` and `Ride_categories_creation.sql`.  
3. **Open Tableau Dashboard**  
   - Load `A Ride Analytics Project.twbx` and connect your data source.  
4. **Interact & Explore**  
   - Filter by month, ride‑type, and station for insights.

---

## 🏁 Conclusion  

The **Apex Rides 2024‑25** analysis spotlights how mobility data reflects city rhythm — from commuter rush hours to sunny‑day leisure surges.  
It proves how data visualization can guide **sustainable transport decisions**, **fleet optimization**, and **rider‑centric planning**.

Through **SQL transformation**, **Tableau storytelling**, and **insightful metrics**, this dashboard transforms raw rides into actionable urban‑mobility intelligence.  

> *Every pedal stroke tells a story — this dashboard simply lets the city speak.* 🚴‍♀️💡  
