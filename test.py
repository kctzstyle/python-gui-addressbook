
from addressbook.models import AddressBook
from addressbook.db import AddressBookDAO


dao = AddressBookDAO()
dao.create()

addrBook = AddressBook(1, 'Test Name', 'Test Addr', '010-1111-2222', 'test@gmail.com')
dao.add(addrBook)

result = dao.view_all()
print(result)
