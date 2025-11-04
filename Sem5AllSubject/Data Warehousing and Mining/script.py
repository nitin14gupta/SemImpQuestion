
# Let me analyze all the question papers and extract all questions
# I'll create a comprehensive analysis

papers = {
    "2024_December": {
        "Q1": [
            "Explain CLARANS extension in web mining (5)",
            "Explain in detail the extract/transform/load (ETL) design of an automated warehouse (5)",
            "What is prediction? Explain about Linear regression method (5)",
            "Cluster data {6,14,18,22,1,40,50,11,25} using K-means algorithm, K=2 (5)"
        ],
        "Q2": [
            "Compute dissimilarity between objects: Nominal attributes, Asymmetric binary attributes (10)",
            "Discuss about a three-tier data warehouse architecture (10)"
        ],
        "Q3": [
            "Describe various phases in knowledge discovery process with diagram (10)",
            "Explain Decision tree induction algorithm for classification. Discuss information gain (10)"
        ],
        "Q4": [
            "Apply single linkage clustering & dendrogram on protein/fat data (10)",
            "Apply Apriori algorithm with min support 30% and min confidence 75% (10)"
        ],
        "Q5": [
            "Explain Hyperlink Induced Topic Search Algorithm (HITS) with example (10)",
            "What is market basket analysis? Explain Support and Confidence (10)"
        ],
        "Q6": [
            "Describe working of K-method clustering with sample dataset (10)",
            "Define multidimensional and multilevel association mining (10)"
        ]
    },
    "2023_May": {
        "Q1": [
            "Every data structure in data warehouse contains time element. Why? (5)",
            "Calculate Accuracy, Recall and Precision with TP=50, TN=20, FP=20, FN=10 (5)",
            "What is Market basket analysis? (5)",
            "Draw and explain KDD process (5)"
        ],
        "Q2": [
            "Draw star schema diagram for data warehouse (date, spectator, location, game dimensions) (10)",
            "What is clustering? Explain K-mean clustering. Apply on {2,4,10,12,3,20,30,11,25,56,23} (10)"
        ],
        "Q3": [
            "Find frequent itemsets and association rules using Apriori (min sup 50%, min conf 70%) (10)",
            "What is data preprocessing? Explain data cleaning techniques (10)"
        ],
        "Q4": [
            "Using Naïve Bayesian classification predict class label (10)",
            "What is web mining? Explain HITS algorithm (10)"
        ],
        "Q5": [
            "Explain multilevel and multidimensional association mining with example (10)",
            "Explain working of DBSCAN algorithm with diagram (10)"
        ],
        "Q6": [
            "Explain different data sampling techniques with example (10)",
            "Short notes: OLTP vs OLAP, Web Content mining, Data Loading in ETL (10)"
        ]
    },
    "2022_December": {
        "Q1": [
            "Explain features of data warehouse (5)",
            "Demonstrate with diagram the process of KDD (5)",
            "What is Market basket analysis? (5)",
            "Explain confusion matrix, accuracy and precision with example (5)"
        ],
        "Q2": [
            "Design star schema for Big_University. Create base cuboid and apply OLAP operations (10)",
            "What is clustering? Explain K-mean clustering. Apply on {2,4,10,12,3,20,30,11,25} (10)"
        ],
        "Q3": [
            "Explain ETL process in detail (10)",
            "Use Apriori with min-support count=2 and min-confidence=60% (10)"
        ],
        "Q4": [
            "Illustrate classification technique, classify (Homeowner=YES, Status=Employed, Income=Average) (10)",
            "What is web mining? Explain web content mining in detail (10)"
        ],
        "Q5": [
            "Explain different data cleaning techniques (10)",
            "Explain working of DBSCAN algorithm with diagram (10)"
        ],
        "Q6": [
            "Explain Multidimensional and multilevel rule mining with example (10)",
            "Explain different data sampling techniques with example (10)"
        ]
    },
    "2023_December": {
        "Q1": [
            "Explain features of Datawarehouse (5)",
            "What is Data Preprocessing? Explain data integration phase methods (5)",
            "What is hierarchical clustering? Explain divisive clustering (5)",
            "Define Metadata and explain types of metadata (5)"
        ],
        "Q2": [
            "Explain association rule mining and multilevel association rules with multidimensional examples (10)",
            "Give Data mining as step in KDD. Give architecture of typical Data Mining system (10)"
        ],
        "Q3": [
            "Explain Extraction and transformation in ETL process (10)",
            "Illustrate Multidimensional association rules with examples (10)"
        ],
        "Q4": [
            "Define classification, issues of classification, explain Naïve bayesian classification (10)",
            "Find mean, median, mode, midrange, variance of given data (10)"
        ],
        "Q5": [
            "Explain HITS algorithm and illustrate its working (10)",
            "Explain Web structure mining in detail (10)"
        ],
        "Q6": [
            "What is clustering? Explain k-means clustering. Apply on {2,4,10,12,3,20,11,25}, K=2 (10)",
            "Illustrate various operations and examples of OLAP cube (10)"
        ]
    },
    "2024_May": {
        "Q1": [
            "Demonstrate with diagram Data Mining Architecture (5)",
            "What is outlier? Explain different types of outliers (5)",
            "What is prediction? Explain Linear regression method (5)",
            "Explain different OLAP operations on multidimensional data (5)"
        ],
        "Q2": [
            "Compute dissimilarity: Nominal attributes, Asymmetric binary attributes (10)",
            "Calculate Accuracy, Recall, Precision with TP=45, TN=25, FP=18, FN=12 (10)"
        ],
        "Q3": [
            "Describe various phases in knowledge discovery process with diagram (10)",
            "What is web mining? Explain web content mining in detail (10)"
        ],
        "Q4": [
            "Discuss Agglomerative algorithm and plot Dendrogram using single link (10)",
            "Find frequent itemsets using Apriori with min-support=60%, min-confidence=80% (10)"
        ],
        "Q5": [
            "Explain Decision Tree classification Approach in detail (10)",
            "What is market basket analysis? Explain Support and Confidence (10)"
        ],
        "Q6": [
            "Explain BIRCH algorithm with diagram (10)",
            "Define multidimensional and multilevel association mining (10)"
        ]
    },
    "2025_May": {
        "Q1": [
            "Explain data warehouse features (5)",
            "Demonstrate with diagram the process of KDD (5)",
            "What is Market basket analysis? (5)",
            "Explain confusion matrix, accuracy and precision with example (5)"
        ],
        "Q2": [
            "Explain with example Star schema and Snowflake schema (10)",
            "Explain with example any four OLAP operations (10)"
        ],
        "Q3": [
            "Data preprocessing is necessary before data mining. Justify your answer (10)",
            "Explain any 3 data normalization techniques (10)"
        ],
        "Q4": [
            "Explain Support, Confidence and Lift function in association mining (10)",
            "Consider transaction database, use Apriori with min-support 40%, min-confidence 70% (10)"
        ],
        "Q5": [
            "Illustrate classification technique, classify (Homeowner=employed, Status=Employed, Income=Average) (10)",
            "What is web mining? Explain web content mining in detail (10)"
        ],
        "Q6": [
            "Explain K-means clustering with example (10)",
            "Explain working of DBSCAN algorithm with diagram (10)"
        ],
        "Q7": [
            "Explain Multidimensional and multilevel rule mining with example (10)",
            "Explain different data sampling techniques with example (10)"
        ]
    }
}

# Count frequency of topics across all papers
from collections import defaultdict

topic_frequency = defaultdict(int)
all_questions = []

# Extract unique questions and categorize by topic
topics_map = {
    "Data Warehouse": ["warehouse", "star schema", "snowflake", "OLAP", "three-tier", "ETL", "metadata"],
    "KDD Process": ["KDD", "knowledge discovery"],
    "Clustering": ["clustering", "k-means", "DBSCAN", "hierarchical", "dendrogram", "BIRCH", "CLARANS"],
    "Association Mining": ["apriori", "association", "market basket", "support", "confidence", "lift", "multilevel", "multidimensional"],
    "Classification": ["classification", "decision tree", "naive bayesian", "information gain"],
    "Prediction": ["prediction", "regression"],
    "Data Preprocessing": ["preprocessing", "data cleaning", "normalization", "sampling", "integration"],
    "Web Mining": ["web mining", "HITS", "web content", "web structure"],
    "Evaluation Metrics": ["accuracy", "precision", "recall", "confusion matrix"],
    "Similarity/Dissimilarity": ["dissimilarity", "nominal", "binary attributes"],
    "Outliers": ["outlier"],
    "Data Mining Architecture": ["data mining architecture", "data mining system"]
}

# Analyze questions
question_analysis = []
for year, questions_dict in papers.items():
    for q_num, q_list in questions_dict.items():
        for q in q_list:
            q_lower = q.lower()
            question_analysis.append({
                "year": year,
                "question": q,
                "q_number": q_num
            })
            
            # Count topics
            for topic, keywords in topics_map.items():
                if any(keyword in q_lower for keyword in keywords):
                    topic_frequency[topic] += 1

print("=" * 80)
print("TOPIC FREQUENCY ANALYSIS")
print("=" * 80)
sorted_topics = sorted(topic_frequency.items(), key=lambda x: x[1], reverse=True)
for topic, count in sorted_topics:
    print(f"{topic:35s}: {count:2d} times")

print(f"\nTotal questions analyzed: {len(question_analysis)}")
