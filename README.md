# Overview
This is a Python-based machine learning project deployed on Azure Web App service and using Flask web-framework as it rest-API. The machine learning model will predict the price of Boston houses according to some information such as average room in the house, data about highway access and so on.

## Project Plan
- [Project plan](https://docs.google.com/spreadsheets/d/1lS0_nD0a2gimpy0jQcHxFSqQ9Rm3pjqQlrCMkl8MxZY/edit?usp=sharing)
- [Trello](https://trello.com/invite/b/tJXvs7Jm/ATTId37511caf76a188e3e1ba8704824dee5C3B3ADE2/udacity-azure-devops-project2)

## Instructions

![diagram](images/udacity-azure-devops-project2.drawio.png)



* Project running on Azure App Service
```
    az webapp up --sku F1 -n <web_app_name> -g <azure-resoure-group>
```
![diagram](images/azure-webapp-deploy.PNG)


* Project cloned into Azure Cloud Shell
![diagram](images/repo-cloudshell.PNG)


* Passing tests that are displayed after running the `make all` command from the `Makefile`
![diagram](images/make-all-passed.PNG)


* Output of a test run
![diagram](images/github-acction-passed.PNG)

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

    ![diagram](images/azure-webapp.PNG)

* Running Azure App Service from Azure Pipelines automatic deployment
![diagram](images/azure-pipeline.PNG)

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:
![diagram](images/make-predict-azure.PNG)

* Output of streamed log files from deployed application
![diagram](images/webapp-log.PNG)

* Locust
![diagram](images/locust.PNG)



## Enhancements
- Deploy infrastructure using provisioning tool like Terraform
- Deploy the application on Kubernetes cluster
- Apply rolling update 
- Adding more test/case to the application.


## Demo 
Youtube: https://www.youtube.com/watch?v=n2PNlUqwNtg