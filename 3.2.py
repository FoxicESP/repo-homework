def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Green', name='Bob', year='1976', city='NY', email='bob_green@google.com',
              telephone='1-212-123 45 67'))
