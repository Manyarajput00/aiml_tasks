


contaces={}

contact_grp={
    'family':set(),
    'office':set(),
    'friends':set()
}

def add_contact(name,phone , email):
    if name in contact_grp:
        print('contact already present')
    else:
        contaces[name]={'phone':phone,'email':email}
        print(f'contact of {name} add sucessfully') 

def view_contacts():
    if not  contaces:
        print('contact book is empty')   
    else:
        print ('all contacts are:')
        for name,info in contaces.items():
            print(f'{name} => phone: {info["phone"]}, email: {info["email"]}')


def search_contact(name):
    if name in contaces:
        print(f'found contact: {name} => phone: {contaces[name]["phone"]}, email: {contaces[name]["email"]}')
    else:
        print('contact not found')

def update_contact(name, phone=None, email=None):
    if name in contaces:
        if phone:
            contaces[name]['phone']=phone
        if email:
            contaces[name]['email']=email
        print(f'contact {name} updated sucessfully')
    else:
        print('contact not found')

def deleted_contact(name):
    if name in contaces:
        del contaces[name]
        for group in contact_grp:
            contact_grp[group].discard(name)
        print(f'contact {name} deleted sucessfully')
    else:
        print('contact not found')  

def add_grp(name , grp):
    if name not in contaces:
        print('contact not found')
    elif grp not in contact_grp:
        print('group not found')
    else:
        contact_grp[grp].add(name)
        print(f'contact {name} added to group {grp} sucessfully')


def view_grp(grp):
    if grp in contact_grp:
        print(f'group {grp} has following contacts:')
        for name in contact_grp[grp]:
            print(f'- {name}')
    else:
        print('group not found')    


add_contact("Manya", "9876543210", 'manyahjdud')
add_contact("Ravi", "9123456780", 'JHGJUGUHU')

view_contacts()

search_contact("Manya")

update_contact("Manya", email="new_manya@example.com")

add_grp("Manya", "Friends")
add_grp("Ravi", "Work")

view_grp("Friends")
view_grp("Work")

deleted_contact("Ravi")
view_contacts()