from django.test import TestCase
from Restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User

class MenuTest(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='tao', password='123')
        self.client.login(username='tao', password='123')

    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 80")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)

    def test_get_item_method(self):
        """Test the get_item method of the Menu model."""
        item = Menu.objects.create(title="Ice Cream", price=2.5, inventory=100)
        item = Menu.objects.get(title="Ice Cream")
        self.assertEqual(item.get_item(), "Ice Cream : 2.50")
        
    def test_list_menu_items(self):
        """Test listing all menu items."""
        self.client.login(username='tao', password='123')
        url = reverse('menu-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)  # Assuming we only have the 2 items we added in setUp
