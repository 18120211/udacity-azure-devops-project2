import time
import json
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def predict(self):
        with open("payload.json") as f:
            data = json.load(f)
        self.client.post("/predict", json=data, headers={"Content-Type": "application/json"})