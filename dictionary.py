from datetime import date

USERS = [
    {
        'email': 'cvander@platzi.com',
        'first_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': '1234567',
        'is_admin': True
    },
    {
        'email': 'freddier@platzi.com',
        'first_name': 'Freddy',
        'last_name': 'Vega',
        'password': '987654321',
    },
    {
        'email': 'yesica@platzi.com',
        'first_name': 'Yesica',
        'last_name': 'Cortes',
        'password': 'qwerty',
        'birthdate': date(1990,12,19)
    },
    {
        'email': 'arturo@platzi.com',
        'first_name': 'Arturo',
        'last_name': 'Martines',
        'password': 'msicomputer',
        'is_admin': True,
        'birthdate': date(1981,11,6),
        'bio': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s'
    }
]

from posts.models import User

for user in USERS:
    obj= User.objects.create(**user)
    print(obj.pk, ' : ', obj.email)