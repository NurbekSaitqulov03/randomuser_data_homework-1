import get_data

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    gender = []
    for gen in data['results']:
        if gen['gender']=='male':
            x = f'Male:1'
            gender.append({x})
        if gen['gender']=='female':
            y = f'Female:0'
            gender.append({y})
    return gender
data = get_data.get_data('randomuser_data.json')
print(get_gender_users(data))