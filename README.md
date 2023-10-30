# Azure Function - Recommendation engine with collaborative filtering

## Overview
This Azure Function is designed to provide article recommendations using a collaborative filtering approach. It utilizes the Implicit library and a pre-trained model to suggest articles based on a user's preferences.  

## Prerequisites  
Before deploying and using this Azure Function, make sure you have the following prerequisites:  
1. __Azure account__: You need an active Azure account to deploy and host this Azure Function.  
2. __Implicit library__: The function uses the Implicit library for collaborative filtering. Make sure you install this library or ensure it's included in your deployment package.  
3. __Pre-trained model__: The function relies on a pre-trained model for generating recommendations. Ensure this model is available in the same directory as the function.  
4. __CSR data__: The function loads CSR data from the csr_article_popularity.npz file. Make sure this file is available in the same directory.  
5. __Python environment__: The function is written in Python. You should have a Python environment (3.6 or higher) for running this function.  

## Usage 
### Input
The Azure Function accepts a single parameter, "user_id," either through a query string or a JSON request body. It uses the user_id to generate personalized article recommendations.  
### Output
The function returns a JSON response containing a list of recommended article IDs. The recommendations are based on the user's preferences and the collaborative filtering model.  
### Example request  
To get recommendations for a user, you can send an HTTP request to the Azure Function with the user_id as a parameter.  

Example using cURL:  
```bash
curl -X GET "https://your-function-url.azurewebsites.net/api/HttpTrigger?user_id=123"
```
### Example Response  
The response will be a JSON array of recommended article IDs:  
```json
["12345", "67890", "54321", "98765", "11223"]
```

## Deployment
You can deploy this Azure Function to your Azure account using Azure Functions. Make sure to set up the necessary environment and configurations, including your Azure credentials.

## License
This Azure Function is available under the MIT License.