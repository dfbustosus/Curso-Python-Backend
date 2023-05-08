from django.test import TestCase

from App1.forms import CursoFormulario, ProfesorFormulario
import django 
# Import the Django model you want to test
from App1.forms import ProfesorFormulario
import unittest
# Import the Django test framework
from django.test import TestCase

# Write your unit test(s)
class ProfesorFormularioTest(TestCase):
    def test_valid_form(self):
        form_data = {'id': 1, 'nombre': 'John', 'apellido': 'Doe', 'email': 'john.doe@example.com', 'profesion': 'Developer'}
        form = ProfesorFormulario(data=form_data)
        print(form)
        #print(self.assertTrue(form.is_valid()))

    def test_invalid_form(self):
        form_data = {'id': 1, 'nombre': 'John', 'apellido': 'Doe', 'email': None, 'profesion': 'Developer'}
        form = ProfesorFormulario(data=form_data)
        print(form)
        #print(self.assertFalse(form.is_valid()))

# Run your unit test(s) with a test runner
if __name__ == '__main__':
    django.setup()
    unittest.main()