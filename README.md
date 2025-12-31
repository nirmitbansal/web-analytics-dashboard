**📊 Web Analytics Performance Dashboard**

    A comprehensive Web Analytics Dashboard built using Tableau Public, designed to analyze traffic performance, user behavior, revenue trends, and conversion efficiency across multiple marketing sources.

**🚀 Project Overview**

        🔹 This project transforms raw web analytics data into actionable insights using interactive Tableau visualizations.  
        🔹 It enables stakeholders to track KPIs, compare traffic sources, and identify optimization opportunities.

**🎯 Key Business Objectives**

        📈 Monitor Revenue & User trends over time
        
        🔍 Analyze traffic source performance
        
        💡 Understand conversion efficiency & engagement behavior
        
        📉 Identify high bounce rate vs low session duration patterns

**📌 KPIs Tracked**

        👥 Total Users
        
        🔄 Total Sessions
        
        💰 Total Revenue
        
        🛒 Total Transactions
        
        📊 Average Conversion Rate

        ⏱ Average Session Duration
        
        🚪 Bounce Rate

**📊 Dashboard Visualizations**

        📈 Trend Analysis
        
        📅 Monthly Revenue Trend
        
        👤 Monthly Users Trend
        
        🌐 Traffic Source Performance
        
        💰 Revenue by Traffic Source
        
        👥 Users by Traffic Source
        
        🛒 Transactions by Traffic Source
        
        📈 Conversion Rate by Traffic Source
        
        🔍 Engagement Analysis
        
        🎯 Bounce Rate vs Session Duration
        (Bubble size represents Sessions volume)

**🔄 ETL Workflow**

        📥 Load raw web analytics data
        
        🧹 Clean missing & inconsistent values
        
        📐 Standardize metrics (rates, durations)
        
        📤 Export analytics-ready CSV
        
        📊 Visualize in Tableau Public

**📁 Dataset Information**

        📌 Source: Web analytics sample data
        
        📌 Format: CSV
        
        📌 Metrics Included:
        
                •Users, Sessions, Revenue
                
                •Transactions, Conversion Rate
                
                •Bounce Rate, Session Duration
                
                •Traffic Source & Time dimensions

**🧠 Key Insights Generated**

        🔥 Identified top-performing traffic sources driving maximum revenue.
        
        📉 Detected sources with high bounce rate but low engagement.
        
        📊 Compared conversion efficiency across marketing channels.
        
        📈 Observed seasonal trends in users and revenue.

**📂 Project Structure**
```text
Web-Analytics-Dashboard/
│
├── dashboard/
│   └── Web_Analytics_Dashboard.twb
│
├── data/
│   ├── raw/
│   │   └── web analytic_dataset.csv
│   └── processed/
│       └── web_analytics_cleaned.csv
│       └──web_analytics_tableau.csv    
├── etl/
├── read_data.py
├── clean_users.py
├── clean_transactions.py
├── clean_revenue.py
├── clean_quantity_sold.py
├── clean_avg_session_duration.py
├── final_clean_etl.py
└── load_to_mysql.py
│
│
├── requirements.txt
├── .gitignore
└── README.md
