from django.test import TestCase, Client
from django.contrib.auth.models import User
from website.models import Company, Customer


# pip install coverage
# and then
# coverage run --source='./website' --omit='website/migrations/*' manage.py test && echo -e "\nCoverage\n" && coverage report   # noqa: E501


class ModelsTestCase(TestCase):
    def setUp(self):
        comp = Company.objects.create(name="company 1")
        Customer.objects.create(first_name="bob", last_name="dobalina", company=comp)

    def test_models_are_sane(self):
        c = Customer.objects.get(first_name="bob", last_name="dobalina")
        self.assertEqual(c.company.name, "company 1")


class ViewsTestCase(TestCase):
    def setUp(self):
        comp = Company.objects.create(name="company 1")
        Customer.objects.create(first_name="bob", last_name="dobalina", company=comp)

        User.objects.create_user(username="testuser", password="12345")

    def test_customer_list(self):
        c = Client()
        c.login(username="testuser", password="12345")
        response = c.get("/")
        self.assertIn("<table", str(response.content))
        self.assertIn("bob dobalina", str(response.content))

    def test_customer_details(self):
        c = Client()
        c.login(username="testuser", password="12345")
        cust = Customer.objects.get(first_name="bob", last_name="dobalina")
        response = c.get("/customer_record/%s" % cust.id)
        self.assertIn("bob dobalina", str(response.content))
        self.assertIn("Email", str(response.content))
        self.assertIn("Phone", str(response.content))

    def test_update_customer(self):
        c = Client()
        c.login(username="testuser", password="12345")
        response = c.get("/")
        cust = Customer.objects.get(first_name="bob", last_name="dobalina")
        comp = Company.objects.get(name="company 1")
        response = c.get("/customer_record/%s" % cust.id)
        response = c.post(
            "/update_customer/%s" % cust.id,
            {
                "first_name": "bobby",
                "last_name": "dobbins",
                "email": "bdobalina@gmail.com",
                "phone": "07901342345",
                "address": "10 seafield drive",
                "city": "london",
                "postcode": "N1 5QL",
                "company": comp.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        response = c.get("/home/")
        self.assertIn("<table", str(response.content))
        self.assertIn("bobby dobbins", str(response.content))

    def test_add_customer(self):
        c = Client()
        c.login(username="testuser", password="12345")
        response = c.get("/")
        comp = Company.objects.get(name="company 1")
        Customer.objects.get(first_name="bob", last_name="dobalina", company=comp)
        response = c.post(
            "/add_customer/",
            {
                "first_name": "bob",
                "last_name": "dobalina",
                "email": "bdobalina@gmail.com",
                "phone": "07901342345",
                "address": "10 seafield drive",
                "city": "london",
                "postcode": "N1 5QL",
                "company": comp.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        response = c.get("/home/")
        self.assertIn("<table", str(response.content))
        self.assertIn("bob dobalina", str(response.content))

    def test_delete_customer(self):
        c = Client()
        c.login(username="testuser", password="12345")
        response = c.get("/")
        self.assertIn("<table", str(response.content))
        self.assertIn("bob dobalina", str(response.content))
        cust = Customer.objects.get(first_name="bob", last_name="dobalina")
        c.post("/delete_customer/%s" % cust.id)
        response = c.get("/")
        self.assertIn("<table", str(response.content))
        self.assertNotIn("bob dobalina", str(response.content))

    def test_user_login(self):
        c = Client()
        c.login(username="testuser", password="12345")
        response = c.get("/")
        self.assertIn("<table", str(response.content))
        self.assertIn("bob dobalina", str(response.content))
        c.post("/logout/")
        response = c.get("/")
        self.assertNotIn("<table", str(response.content))
        self.assertNotIn("bob dobalina", str(response.content))

    def test_home_page(self):
        c = Client()
        c.login(username="testuser", password="12345")
        response = c.get("/")
        self.assertIn("<table", str(response.content))
        self.assertIn("bob dobalina", str(response.content))

    def test_add_note_post(self):
        c = Client()
        c.login(username="testuser", password="12345")
        response = c.get("/")
        cust = Customer.objects.get(first_name="bob", last_name="dobalina")
        response = c.get("/customer_record/%s" % cust.id)
        author = User.objects.get(username="testuser")
        response = c.post(
            "/add_note/",
            {"add_note": "test note", "customer": cust.id, "author": author.id},
        )
        self.assertEqual(response.status_code, 302)
        response = c.get("/customer_record/%s" % cust.id)
        self.assertIn("test note", str(response.content))
        self.assertIn("testuser", str(response.content))

    def test_login_success(self):
        c = Client()
        c.login(username="testuser", password="12345")
        response = c.post("/home/", {"username": "testuser", "password": "12345"})
        self.assertEqual(response.status_code, 302)

    def test_register_user(self):
        c = Client()
        response = c.post("/register_user/", {"username": "testuser", "password": "12345"})
        c.login(username="testuser", password="12345")
        response = c.get("/")
        self.assertIn("<table", str(response.content))
        self.assertIn("bob dobalina", str(response.content))

    def test_company_list(self):
        c = Client()
        c.login(username="testuser", password="12345")
        response = c.get("/company_list/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("<table", str(response.content))
        self.assertIn("company 1", str(response.content))

    def test_company_details(self):
        c = Client()
        c.login(username="testuser", password="12345")
        comp = Company.objects.get(name="company 1")
        Customer.objects.get(first_name="bob", last_name="dobalina", company=comp)
        response = c.get("/company_details/%s" % comp.id)
        self.assertIn("bob dobalina", str(response.content))
        self.assertIn("company 1", str(response.content))

    def test_delete_company(self):
        c = Client()
        c.login(username="testuser", password="12345")
        comp = Company.objects.get(name="company 1")
        response = c.get("/company_list/")
        self.assertIn("<table", str(response.content))
        self.assertIn("company 1", str(response.content))
        response = c.get("/company_details/%s" % comp.id)
        c.post("/delete_company/%s" % comp.id)
        response = c.get("/")
        response = c.get("/company_list/")
        self.assertIn("<table", str(response.content))
        self.assertNotIn("company 1", str(response.content))

    def test_update_company(self):
        c = Client()
        c.login(username="testuser", password="12345")
        response = c.get("/")
        comp = Company.objects.get(name="company 1")
        response = c.get("/company_details/%s" % comp.id)
        response = c.post(
            "/update_company/%s" % comp.id,
            {
                "name": "company 2",
                "website": "www.company2.co.uk",
                "phone": "07901342345",
                "email": "company2@gmail.com",
                "industry": "gardening",
            },
        )
        self.assertEqual(response.status_code, 302)
        response = c.get("/home/")
        response = c.get("/company_list/")
        self.assertIn("<table", str(response.content))
        self.assertIn("company 2", str(response.content))
