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
            gender.append({'Male':1})
            
        if gen['gender']=='female':
            gender.append({'Female':0})
            
    return gender
data = get_data.get_data('randomuser_data.json')
print(get_gender_users(data))