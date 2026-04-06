from locust import HttpUser, task, constant

class BlazeDemoPerformance(HttpUser):
    wait_time = constant(0) # Foco em atingir 250 RPS

    @task
    def fluxo_compra(self):
        self.client.get("/")
        self.client.post("/reserve.php", data={"fromPort": "Paris", "toPort": "London"})
        self.client.post("/purchase.php", data={"flight": "43", "price": "472.56", "airline": "Virgin"})
        self.client.post("/confirmation.php", data={"inputName": "Luciana Lux", "cardType": "visa", "creditCardNumber": "123456789"})
