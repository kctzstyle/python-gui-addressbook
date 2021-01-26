
from addressbook.models import AddressBook
from addressbook.db import AddressBookDAO


dao = AddressBookDAO()
# dao.create()

# addrBook = AddressBook(1, 'Test Name', 'Test Addr', '010-1111-2222', 'test@gmail.com')
# dao.add(addrBook)

# result = dao.view_all()
# print(result)

columns = dao.table_columns()
# for column in columns:
#     for col in column:
#         print(col)
print(columns)

# info = dao.table_info()
# print(info)