student_data = {'id1':
    {'name': ['Sara'],
     'class': ['V'],
     'subject_intgegration': ['english,math,science']
    },
    'id2':
    {'name': ['David'],
     'name': ['V'],
     'subject_integration': ['english,math,science']
    },
    'id3':
     {'name': ['sara'],
     'name': ['V'],
     'subject_integration': ['english,math,science']
    },
    'id4':
    {'name': ['Surya'],
     'name': ['V'],
     'subject_integration': ['english,math,science']
    },
}
result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)