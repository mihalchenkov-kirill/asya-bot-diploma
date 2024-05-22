import json

from locust import HttpUser, TaskSet, between, task


class UserBehavior(TaskSet):
    def on_start(self):
        self.token = '****'
        self.chat_id = '****'
        self.url = f'https://api.telegram.org/bot{self.token}/sendMessage'

    @task(1)
    def send_message(self):
        payload = {'chat_id': self.chat_id, 'text': 'Hello from Locust!'}
        headers = {'Content-Type': 'application/json'}
        self.client.post(self.url, data=json.dumps(payload), headers=headers)


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(0.1, 0.5)
