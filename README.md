# Overview

<TODO: complete this with an overview of your project>

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

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application



## Enhancements


## Demo 



