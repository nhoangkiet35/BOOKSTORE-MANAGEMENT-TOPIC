from locust import HttpUser, between, task


class MyUser(HttpUser):
    wait_time = between(1, 3)  # Thời gian chờ giữa các yêu cầu

    @task
    def load_test(self):
        self.client.get("/")
        self.client.get("/about")
