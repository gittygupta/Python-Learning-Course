def get_gender(gender = 'Unknown'):
    if gender is 'm':
        gender="male"
    elif gender is 'f':
        gender='female'
    print("Gender is ", gender)

get_gender('m')
get_gender('f')
get_gender()

def sentence(name = 'Aousnik', gender = 'male', category = 'general'):
    print(name, gender, category)

sentence('abcd', 'female', 'SC')
sentence(category = 'ST')
sentence(gender = 'other')
sentence()