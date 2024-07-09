from django.core import mail
from django.test import TestCase
from django.core.mail import send_mail

class EmailTest(TestCase):
    def test_send_email(self):
        # Wysłanie e-maila
        send_mail(
            'Test Email',
            'This is a test email.',
            'mayster.app@mbecht.pl',
            ['recipient-email@example.com'],
            fail_silently=False,
        )

        # Sprawdzenie, czy jeden e-mail został wysłany
        self.assertEqual(len(mail.outbox), 1)

        # Sprawdzenie zawartości e-maila
        email = mail.outbox[0]
        self.assertEqual(email.subject, 'Test Email')
        self.assertEqual(email.body, 'This is a test email.')
        self.assertEqual(email.from_email, 'mayster.app@mbecht.pl')
        self.assertEqual(email.to, ['recipient-email@example.com'])

