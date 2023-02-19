from django.test import TestCase

from .models import Bank, Supplier

class BankTestCase(TestCase):
    def test_max_length_name_bank(self):
        bank = Bank.objects.create(
            name='a'*51,
        )
        with self.assertRaises(Exception) as context:
            bank.full_clean()
        
        self.assertIn('name', context.exception.message_dict)

def create_supplier(name,nit,person_name,person_phone):
    return Supplier.objects.create(
        name= name ,
        nit=nit,
        contact_person_name = person_name,
        contact_person_phone = person_phone
    )

class SupplierTestCase(TestCase):

    def test_supplier_correct(self):
        supplier = create_supplier("fake supplier",'123456789-0',"Jhon Doe",'1234567890')
        supplier.full_clean()
        supplier.save()

    def test_field_regex_in_nit(self):
        supplier = create_supplier("fake supplier",'1234-1',"Jhon Doe",'1234567890')
        with self.assertRaises(Exception) as context:
            supplier.full_clean()
        self.assertIn('nit', context.exception.message_dict)
    
    def test_type_nit(self):
        supplier = create_supplier("fake supplier",1234-1,"Jhon Doe",'1234567890')
        with self.assertRaises(Exception) as context:
            supplier.full_clean()
        self.assertIn('nit', context.exception.message_dict)


    def test_max_length_contact_phone_supplier(self):
        supplier = create_supplier("fake supplier",'123456789-0',"Jhon Doe",123456789008)
        with self.assertRaises(Exception) as context:
            supplier.full_clean()
        
        self.assertIn('contact_person_phone', context.exception.message_dict)

