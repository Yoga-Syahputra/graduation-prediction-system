from locust import HttpUser, task, between

class WebAppUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def predict_kelulusan(self):
        self.client.post("/", data={
            "nama": "Student",
            "nim": "2101020000",
            "ip1": 3.5,
            "ip2": 3.6,
            "ip3": 3.7,
            "ip4": 3.8,
            "ip5": 3.9,
            "ip6": 4.0,
            "ipk": 3.75
        })
