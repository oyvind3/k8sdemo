from locust import HttpUser, task

class UserVisit(HttpUser):
    host = "http://138.91.199.32:8089/"
    
    @task
    def visit(self):
        self.client.get("/")
