import requests

def get_data(url):

    response = requests.get(url)
    return response.json()

def compare_data(url):

    data1 = get_data(url)
    data2 = get_data(url)

    result = {}

    for user, user_data in data2.items():
        if user in data1:
            achievements1 = set(data1[user]['achievements'].keys())
            achievements2 = set(user_data['achievements'].keys())

            end_achievements = achievements2 - achievements1

            if end_achievements:
                result[user] = {
                    'metadata': user_data['metadata'],
                    'achievements': {achievement: True for achievement in end_achievements}
                }
            else:
                result[user] = {
                    'metadata': user_data['metadata'],
                    'achievements': {}
                }

        else: 
            result[user] = user_data

    return result

def main():

    url = "https://base.media108.ru/training/sample/"
    print(compare_data(url))


if __name__ == "__main__":
    main()
