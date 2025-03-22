from locust import HttpUser, between, task


class MyUser(HttpUser):
    wait_time = between(1, 3)  # Thời gian chờ giữa các yêu cầu

    @task(2)
    def test_home(self):
        self.client.get("/")

    @task(2)
    def test_about(self):
        self.client.get("/about")

    @task(1)
    def test_random(self):
        self.client.get("/?cate_id=3")
        self.client.get("/book/2")
