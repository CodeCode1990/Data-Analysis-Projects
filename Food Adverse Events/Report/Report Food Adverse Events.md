# 🧾 Food Adverse Event Analysis Report

**Platform:** Anaconda (Jupyter Notebook)  
**Language:** Python  
**Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn, scipy, datetime  
**Dataset:** Center for Food Safety and Applied Nutrition (CAERS) – Adverse Event Reporting System

---

## 📘 1. Introduction

This analysis explores the real world **FDA’s CAERS dataset**, which records adverse events associated with foods, cosmetics, and dietary supplements.  
The main goal was to identify patterns in **product safety**, **demographic impact**, **outcome severity**, and potential **predictive signals** for high-risk products or patient groups.  

By applying a structured analytical pipeline — from **data cleaning and validation** to **exploratory analysis** and **predictive modeling** — this project provides a holistic understanding of how consumer products relate to reported adverse effects.

---

## 📂 2. Data Overview

The dataset contained over **221,000 reports** covering a wide range of products, including foods, supplements, and cosmetics.  
Each record described when the FDA received the report, what product was involved, patient demographics (age, gender), and the resulting outcome (e.g., hospitalization, death, recovery).

Before analysis, the data underwent standardization:
- All date fields were converted to consistent formats.  
- Ages were unified into **years** for comparability.  
- Text fields such as outcomes and event descriptions were cleaned and standardized.  
- Duplicates and invalid report IDs were corrected.  

These cleaning steps ensured consistency across time and improved the reliability of subsequent analysis.

---

## 🧹 3. Data Quality and Preparation

Initial exploration revealed several inconsistencies:
- Some **patient ages** were entered in days, months, or decades, and these were converted uniformly into years.  
- **Report IDs** lacked uniformity, so each was reconstructed using the year and case number format.  
- Around **89 records** had event dates occurring *after* they were reported — likely due to follow-up reports — and were retained with appropriate flags.  
- Implausible age entries (e.g., 680 years) were corrected after identifying incorrect unit conversions.

The final dataset provided a clean, structured foundation for meaningful demographic and outcome analysis.

---

## 👥 4. Demographic Insights

### 4.1 Unique Patients and Age Distribution  
After de-duplication, there were approximately **132,600 unique patients**.  
Adults represented the largest portion of reports, followed by elders. Children and infants made up a very small share of total cases.  
Roughly **39% of reports** lacked explicit age data, indicating reporting gaps.

### 4.2 Gender Patterns  
Females accounted for nearly **70% of all reported cases**, while males made up about **24%**.  
This pattern suggests either greater reporting tendencies among female patients or potential product-category exposure differences (e.g., cosmetics and supplements being used more often by women) or the products tends to affect female more than males.

### 4.3 Severe Outcomes by Age  
Fatalities were concentrated in **adult and elderly age groups**, which together accounted for nearly **75%** of all deaths.  
Children and adolescents had far fewer severe outcomes, reflecting expected physiological resilience and lower exposure to high-risk supplement products.

### 4.4 Congenital Anomalies and the COVID Period  
A small subset (9 reports) showed **congenital anomalies during the COVID-19 pandemic window (2020–2023)**.  
Most were associated with prenatal or supplement-type products, suggesting closer scrutiny of perinatal supplement use during this period.

### 4.5 Age Distribution Summary  
The average reported patient age was **around 50 years**, with a median of **52**.  
This aligns with a demographic typically more engaged in supplement and health product use.

---

## 💊 5. Product Exposure and Patterns

### 5.1 Product Variety  
The dataset contained nearly **77,000 unique products**, spanning multiple product codes and categories.  
Of these, about **67,000** were classified as *suspect products* (potentially causing the event), and **10,000** as *concomitant products* (used alongside other items).

### 5.2 Repeated High-Risk Products  
Certain entries — such as **“EXEMPTION 4”**, **Johnson’s Powder**, and **Vitamin D supplements** — appeared repeatedly among reports linked to severe outcomes like hospitalization or death.  
Cosmetics and dietary supplements dominated the list, indicating their high representation in the database rather than inherent toxicity.

### 5.3 Product Frequency and Adverse Event Intensity  
Across all reports, products like **Multivitamins**, **Fish Oil**, and **Vitamin C** had the highest number of associated adverse event mentions.  
This likely reflects widespread usage rather than exceptional danger, emphasizing the need to contextualize raw counts against product popularity.

---

## ⚕️ 6. Outcomes and Severity Analysis

### 6.1 Most Frequent Adverse Events  
The top recurring medical terms were:
- Ovarian cancer  
- Diarrhea  
- Vomiting  
- Nausea  
- Abdominal pain  

Interestingly, these include both general reactions and chronic conditions, showing that CAERS reports often capture **possible associations**, not necessarily confirmed causality.

### 6.2 Common Patient Outcomes  
The most frequent outcomes were:
- *“Other serious or important medical event”* (70,000+ cases)  
- *Hospitalization* (20,000+ cases)  
- *Death* (14,800+ cases)  

This distribution demonstrates that a significant portion of the FDA’s incoming adverse event data involves **serious clinical situations** rather than mild reactions.

### 6.3 Age and Gender Cross-Patterns  
When stratified, **elderly and adult groups** had the most deaths and hospitalizations, while **females** accounted for a slightly higher share of severe outcomes overall.  
Such patterns may result from differences in product types used and pre-existing health conditions among older or female populations.

### 6.4 Overall Severity Proportion  
Roughly **64% of all reported outcomes** were considered *serious* (death, life-threatening, or hospitalization).  
This underscores that the FDA’s CAERS database is skewed toward **more clinically significant incidents**, since minor complaints are less likely to be formally reported.

---

## 📈 7. Temporal and Trend Analysis

### 7.1 Yearly Trends  
The number of cases increased steadily until 2021, suggesting growing consumer engagement with FDA reporting systems or increased market presence of dietary supplements.  
Reports then slightly declined in 2023–2024, possibly due to pandemic-related reporting disruptions.

### 7.2 Monthly Patterns  
Monthly analysis revealed subtle seasonal variation, with **late-year months (September–December)** typically showing higher report volumes.  
This may correspond to seasonal product usage, such as supplements or immune boosters during winter.

### 7.3 Age-Group Trends Over Time  
Across decades, **adults consistently formed the largest share** of reports.  
Infant and child cases remained relatively stable, indicating consistent reporting in these categories over time.

---

## 🧠 8. Advanced Statistical Insights

### 8.1 Correlation Studies  
Statistical testing found:
- A **very weak negative correlation** between patient age and the number of adverse events per case.  
- Similarly weak association between the **number of suspect products** used and total event count.  

These low correlations suggest that adverse events are likely influenced by **individual product characteristics and external factors**, rather than demographics alone.

### 8.2 Predictive Modeling of Severe Outcomes  
A logistic regression model was trained to predict whether a case would result in a *serious outcome* (death, hospitalization, or disability) based on age and sex.

**Model Findings:**
- Accuracy: ~63%  
- ROC-AUC: 0.63  
- Stronger ability to identify serious cases (recall ≈ 0.69) than to identify mild ones.  

This indicates that, while basic demographics alone offer **moderate predictive power**, more robust models could be built by including product attributes and clinical features.

---

## 🔍 9. Interpretation and Key Takeaways

1. **Adults and elders** are most affected by severe food and supplement-related events.  
2. **Female patients** represent the majority of reported adverse events, driven by usage patterns.  
3. Over **two-thirds of reports involve serious medical outcomes**, underscoring the importance of post-market surveillance.  
4. Products like **Exemption 4**, **Johnson’s Powder**, and common vitamins** appear frequently — not necessarily as the most dangerous, but as widely used and thus widely reported.  
5. Correlations between age, product count, and event severity are **minimal**, suggesting multifactorial causes.  
6. Predictive modeling demonstrates **potential for machine learning in pharmacovigilance**, though richer datasets are needed for stronger predictive insights.

---

## ⚙️ 10. Limitations

- Many entries lack complete demographic data (age, gender).  
- The dataset includes **self-reported associations**, not medically verified causality.  
- Some outcomes may be unrelated to the product itself but still included in reporting.  
- Product names are often inconsistent or generic, limiting precise grouping.

---

## 🧩 11. Conclusion

This analysis of the FDA’s CAERS database demonstrates a **full end-to-end data science workflow** — from data wrangling to insight generation and model building.

It reveals that:
- Severe outcomes dominate FDA adverse event submissions.  
- Adults and elders, particularly females, experience the majority of reported cases.  
- Despite the volume of data, demographic and product-level predictors alone only modestly explain adverse event severity.  

This work lays the foundation for **data-driven food and supplement safety monitoring**, emphasizing the need for richer, more standardized, and real-time surveillance data to protect public health.

---

**End of Report**


