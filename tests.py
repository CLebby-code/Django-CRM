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
        response = c.get("/record/%s" % cust.id)
        self.assertIn("bob dobalina", str(response.content))
        self.assertIn("Email", str(response.content))
        self.assertIn("Phone", str(response.content))
