
# Now let me create a comprehensive list of top 20-30 most important questions
# based on frequency and importance

important_questions = [
    # Data Warehouse (High Priority - appears 10 times)
    ("Explain features of Data Warehouse", "Data Warehouse", "Very High"),
    ("Explain Star schema and Snowflake schema with example", "Data Warehouse", "Very High"),
    ("Explain three-tier data warehouse architecture", "Data Warehouse", "High"),
    ("Explain different OLAP operations (Roll-up, Drill-down, Slice, Dice, Pivot)", "Data Warehouse", "Very High"),
    ("Explain ETL (Extract, Transform, Load) process in detail", "Data Warehouse", "Very High"),
    ("Define Metadata and explain types of metadata", "Data Warehouse", "Medium"),
    ("Why does every data structure in data warehouse contain time element?", "Data Warehouse", "Medium"),
    
    # Association Mining (Highest Priority - appears 19 times)
    ("Apply Apriori algorithm with given min-support and min-confidence", "Association Mining", "Very High"),
    ("What is Market basket analysis? Explain with example", "Association Mining", "Very High"),
    ("Explain Support, Confidence, and Lift in association mining with formula", "Association Mining", "Very High"),
    ("Explain multilevel association mining with example", "Association Mining", "High"),
    ("Explain multidimensional association mining with example", "Association Mining", "High"),
    
    # Clustering (High Priority - appears 9 times)
    ("Explain K-means clustering algorithm and apply on dataset", "Clustering", "Very High"),
    ("Explain DBSCAN algorithm with diagram", "Clustering", "High"),
    ("What is clustering? Explain hierarchical clustering (Agglomerative/Divisive)", "Clustering", "High"),
    ("Apply hierarchical clustering and draw dendrogram using single linkage", "Clustering", "High"),
    ("Explain BIRCH algorithm with diagram", "Clustering", "Medium"),
    ("Explain CLARANS extension in web mining", "Clustering", "Low"),
    
    # Classification (High Priority - appears 6 times)
    ("Explain Naive Bayesian classification with example and classify new tuple", "Classification", "Very High"),
    ("Explain Decision Tree classification with Information Gain", "Classification", "Very High"),
    ("Define classification and issues of classification", "Classification", "Medium"),
    
    # Data Preprocessing (High Priority - appears 8 times)
    ("What is data preprocessing? Explain data cleaning techniques", "Data Preprocessing", "High"),
    ("Explain different data normalization techniques (Min-Max, Z-score, Decimal scaling)", "Data Preprocessing", "High"),
    ("Explain different data sampling techniques with example", "Data Preprocessing", "High"),
    ("Explain data integration phase methods", "Data Preprocessing", "Medium"),
    
    # Web Mining (Medium-High Priority - appears 7 times)
    ("What is web mining? Explain web content mining in detail", "Web Mining", "High"),
    ("Explain HITS (Hyperlink Induced Topic Search) algorithm with example", "Web Mining", "High"),
    ("Explain web structure mining in detail", "Web Mining", "Medium"),
    
    # KDD Process (Medium Priority - appears 2 times)
    ("Draw and explain KDD (Knowledge Discovery in Databases) process with diagram", "KDD Process", "High"),
    ("Explain Data Mining Architecture", "KDD Process", "Medium"),
    
    # Evaluation Metrics (Medium Priority - appears 4 times)
    ("Calculate Accuracy, Recall, and Precision given TP, TN, FP, FN", "Evaluation Metrics", "High"),
    ("Explain confusion matrix with example", "Evaluation Metrics", "High"),
    
    # Prediction (Low-Medium Priority - appears 2 times)
    ("What is prediction? Explain Linear Regression method", "Prediction", "Medium"),
    
    # Similarity/Dissimilarity (Low-Medium Priority - appears 2 times)
    ("Compute dissimilarity between objects: Nominal and Asymmetric binary attributes", "Similarity", "Medium"),
    
    # Statistical Measures (appears occasionally)
    ("Calculate mean, median, mode, midrange, variance of data", "Statistics", "Low"),
    
    # Outliers (Low Priority - appears 1 time)
    ("What is outlier? Explain different types of outliers", "Outliers", "Low"),
]

print("=" * 100)
print("TOP 30 MOST IMPORTANT QUESTIONS FOR DATA WAREHOUSING AND MINING")
print("=" * 100)
print(f"{'No.':<5} {'Priority':<12} {'Topic':<25} {'Question'}")
print("=" * 100)

for i, (question, topic, priority) in enumerate(important_questions, 1):
    print(f"{i:<5} {priority:<12} {topic:<25} {question}")

print("=" * 100)
print(f"\nTotal Important Questions: {len(important_questions)}")
print("\nNOTE: Focus on 'Very High' and 'High' priority questions for maximum coverage")
