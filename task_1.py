import requests


if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    resources = response.json()
    new_recourses = list()
    for item in resources:
        new_recourses.append({
            "id": item['id'],
            "title": item['title']
        })
