from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib.auth.forms import PasswordChangeForm


class PasswordChange(TestCase):
    """test for check change password"""

    def test_incorrect_old_password(self):
        """test for chek old password"""
        self.user = User.objects.create_user(username='testuser', password='12345')
        data = {
            'old_password': 'abcdr',
            'new_password1': 'abc123',
            'new_password2': 'abc123',
        }
        form = PasswordChangeForm(self.user, data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form["old_password"].errors, [form.error_messages['password_incorrect']])

    def test_success_change_password(self):
        """test for check check the password change """
        self.user = User.objects.create_user(username='testuser', password='12345')
        data = {
            'old_password': '12345',
            'new_password1': 'Mbc12395634@',
            'new_password2': 'Mbc12395634@',
        }
        form = PasswordChangeForm(self.user, data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form["old_password"].errors,
                         [])
