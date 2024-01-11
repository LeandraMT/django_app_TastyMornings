from django.test import TestCase
from django.urls import reverse
from .models import Profile


# Create your tests here.
class ProfileModelTest(TestCase):
    def setUpTestData():
        Profile.objects.create(name="Anna", email="anna@example.com")

    def test_user_name(self):
        recipe = Profile.objects.get(id=1)
        field_label = recipe._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        recipe = Profile.objects.get(id=1)
        max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(max_length, 120)

    def test_user_email_valid(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.email, "anna@example.com")

    def test_birthday_null_blank(self):
        profile = Profile.objects.get(id=1)
        self.assertIsNone(
            profile.birthday
        )  # Ensure the birthday field allows null values

    def test_birthday_blank(self):
        # When Profile was created without a birthday input
        profile = Profile.objects.create(name="Jane", email="jane@example.com")
        self.assertIsNone(profile.birthday)

    def test_profile_authenticated(self):
        self.client.login(username="Anna", email="anna@example.com")
        # Accessing the profile view
        response = self.client.get(reverse("profiles:profile"))
        self.assertEqual(response.status_code, 302)

    def test_profile_unauthenticated(self):
        self.client.logout()
        # Accessing the profile view without authentication
        response = self.client.get(reverse("profiles:profile"))
        self.assertEqual(response.status_code, 302)
