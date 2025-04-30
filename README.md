
# 🚀 **Azure Data Engineering Pipeline**  


![image](https://github.com/user-attachments/assets/9988c7a9-1c4b-4020-89bc-31d50474e52c)


## **Overview**  
This project demonstrates an end-to-end **Azure data engineering pipeline**, covering **data ingestion, transformation, storage, governance, and reporting** using **Azure Databricks, Delta Lake,  and Power BI**.  

## **Key Technologies Used**  
✔ **Azure Data Factory** – Data ingestion & orchestration  
✔ **Azure Databricks** – Scalable processing & transformations  
✔ **Delta Lake** – Optimized storage & versioning  
✔ **Unity Catalog** – Access control & data governance  
✔ **Azure Data Lake Gen2** – Secure cloud storage  
✔ **Power BI** – Interactive visualization & reporting  

## **Architecture Breakdown**  

### 🔹 **Bronze Layer (Raw Data Storage)**  
- Ingested **NYC Taxi Service** data using **Azure Data Factory**  
- Stored raw files in **Data Lake Gen2 (Bronze Layer)**  

### 🔹 **Silver Layer (Data Transformation & Optimization)**  
- Cleaned and processed data with **PySpark SQL transformations**  
- Applied **column renaming, type casting, and feature extraction**  
- Stored **optimized Parquet format** in **Silver Layer**

 ![image](https://github.com/user-attachments/assets/09f53b81-3baa-464a-8d78-fbe7153bef7c)

### 🔹 **Gold Layer (Finalized Structured Data & Delta Lake Storage)**  
- Created **Delta Tables** for structured reporting  
- Used **Unity Catalog** to manage permissions  
- **Delta Lake versioning** implemented for data tracking  

![image](https://github.com/user-attachments/assets/f50a7a69-fd34-42fe-9019-3652d4cf3a01)


### **Delta Versioning & Testing**  
✔ **Versioning History** (`DESCRIBE HISTORY trip_zone`) for tracking changes  
✔ **Update & Delete Tests** to validate data integrity  
✔ **Restoring previous versions** (`RESTORE trip_zone VERSION AS OF X`) for rollback scenarios  

![image](https://github.com/user-attachments/assets/54922c54-b498-4402-9541-84686f356540)




This ensures **data traceability** and enables **efficient recovery** when needed.


Let me know if this works for you or if you need further refinements! 🚀

## **Power BI Integration**  
- Connected **Power BI** to **Databricks** for real-time analytics  
- Optimized query performance for audience engagement

Sample Testing Screenshot 

![image](https://github.com/user-attachments/assets/3a1e0489-750c-4d8d-9fef-b12b7f10d156)

Data modeling 

![image](https://github.com/user-attachments/assets/f8e50362-4b13-4fa5-81cf-b2153c675e7c)



## **Challenges & Learnings**  
✅ Fixed **Databricks cluster setup errors**  
✅ Resolved **external storage location issues**  
✅ Implemented **Delta Lake versioning and recovery**  


