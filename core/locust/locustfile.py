from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    def on_start(self):
        response = self.client.post('/accounts/api/v2/jwt/create/', data={"email":"pampam7072@gmail.com","password":"123"}).json()
        self.client.headers = {'Authorization': f"Bearer {response.get('access', None)}"}
    
    
    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/")


    @task
    def post_category(self):
        self.client.get("/blog/api/v1/category/")