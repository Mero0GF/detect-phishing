# Phishing Detection with Machine Learning

## Team Members
Eric Akio Uchiyamada <br/>
Lucas Goulart de Farias Meres <br/>
Oliver Kieran Galvão McCormack <br/>
Pedro Loureiro Morone Branco Volpe <br/>
Renan Tagliaferro <br/>

# Overview
This project explores the use of machine learning algorithms for the automated detection of phishing websites, based on characteristics extracted from URLs and page content. The study compares the performance of three algorithms: Logistic Regression, K-Nearest Neighbors (KNN), and Random Forest, using a dataset containing 5,780 samples, with 578 phishing sites and 5,000 legitimate sites.

# Datasets
For the project, we collected data from the Zenodo website (Link: https://zenodo.org/records/8041387). It presents several datasets separated into phishing and non-phishing (legitimate) categories.
We analyzed and selected two datasets, one with 5,000 phishing cases and another with 5,000 legitimate cases, both containing the same columns (values).
The datasets downloaded were not-phishing.csv and phishing.csv.

The data preprocessing is described in the article (Note: the article is in Portuguese).

# Algorithms Used
Logistic Regression: A simple and interpretable model for binary classification.
K-Nearest Neighbors (KNN): An instance-based algorithm that classifies based on the proximity of neighbors.
Random Forest: An ensemble model that uses multiple decision trees to improve accuracy.

# Results
KNN and Logistic Regression showed good accuracy for legitimate sites but struggled to identify phishing, with high false negatives.
Random Forest performed better in detecting phishing, with fewer false negatives, but more false positives.

# Conclusion
The Random Forest model is the most effective for detecting phishing, although it comes with a higher cost in false positives, which is acceptable for security purposes, as false negatives are more harmful.

# Additional Information
More details about the project can be found in the article "Phishing Website Detection with Machine Learning_ A Data Analysis Approach Based on Authentic and Malicious Websites."

We also provide a .ipynb file with the codes organized for better visualization of the information, serving as an extra version of the code found in the project’s Docker.

# Run Docker
## Option 1: Obtain Image from Docker Hub
### a. Install Docker (if not already installed):
Follow the installation instructions for Docker based on your operating system: Docker

### b. Log in to Docker Hub
Open the terminal and type:

```bash
docker login
```
Enter your Docker Hub username and password. If the container is public, this step may be optional.

### c. Download the container image from Docker Hub:
```bash
docker pull eriaki/detect-phishing:latest
```
### d. Prepare the .csv file with prediction data
Note: The .csv file must have a specific format for prediction to work properly. <br/>
The .csv file must contain the following columns: `brands`, `features.html`, `whois_domain_age`, `remote_ip_address`, `domain`, `whois_registrar_url`, `url`, `assets_downloaded`, and `is_phishing`. <br/>
It is recommended to use a modified dataset from the Zenodo website (Link: https://zenodo.org/records/8041387).

### e. Run the container
```bash
docker run -p 8501:8501 eriaki/detect-phishing
```  
### f. Open localhost in your browser
Search for http://localhost:8501/ in your preferred browser.

### g. Upload the .csv file for prediction
A field to upload files will be available. Insert the .csv file in the field. <br/>
With this, the models will predict based on the provided .csv file.

## Option 2: Obtain Image from Docker Folder
### a. Install Docker (if not already installed):
Follow the installation instructions for Docker based on your operating system: Docker

### b. Download the Docker folder from this repository
### c. Open the terminal inside the Docker folder
### d. Build the Docker image
First, check if Docker is installed with:

```bash
docker --version
```  
If it is installed, its version will appear. <br/>
Then, build the image:

```bash
docker build -t streamlit-app .
``` 
This process may take some time.

### e. Run the image
```bash
docker run -p 8501:8501 streamlit-app
```  
### f. Open localhost in your browser
Search for http://localhost:8501/ in your preferred browser.

g. Upload the .csv file for prediction
A field to upload files will be available. Insert the .csv file in the field. <br/>
With this, the models will predict based on the provided .csv file.
