# Real-Time Distributed Stock Prediction and Anomaly Detection

## 📌 Overview

This project implements a real-time distributed stock data processing and prediction pipeline using **Apache Kafka** and **Apache Spark Streaming**.

The system generates streaming stock data, publishes it through Kafka, processes the incoming stream using Spark, and performs real-time prediction and anomaly detection.

## 🏗️ System Architecture

Stock Data Generator  
↓  
Apache Kafka  
↓  
Kafka Topic  
↓  
Apache Spark Streaming  
↓  
Real-Time Data Processing  
↓  
Prediction & Anomaly Detection  
↓  
Output / Storage

## 🚀 Key Features

- Real-time stock data generation
- Kafka-based distributed data streaming
- Real-time stream processing using Apache Spark
- Machine learning-based stock prediction
- Anomaly detection in streaming data
- Checkpointing for model/pipeline state
- Distributed processing architecture

## 🛠️ Technologies Used

- Python
- Apache Kafka
- Apache Spark
- PySpark
- Machine Learning
- Real-Time Data Processing

## 📂 Project Structure

```text
real-time-distributed-stock-prediction/
│
├── data_generator.py       # Generates streaming stock data
├── stream_processor.py     # Processes the Kafka stream using Spark
├── checkpoint.pkl          # Model/checkpoint file
├── requirements.txt        # Python dependencies
└── .gitignore              # Files excluded from Git
