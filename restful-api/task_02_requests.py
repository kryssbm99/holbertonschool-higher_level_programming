import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from the given URL and prints their titles.

    This function makes a GET request to the specified URL, retrieves the posts
    in JSON format, and prints the title of each post. If the request fails, it
    prints an error message.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts")

def fetch_and_save_posts():
    """
    Fetches posts from the given URL and saves them to a CSV file.

    This function makes a GET request to the specified URL, retrieves the posts
    in JSON format, and saves them to a CSV file named 'posts.csv'. Each post
    is saved with its ID, title, and body. If the request fails, it prints an
    error message.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        data = []
        for post in posts:
            data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
        
        with open('posts.csv', 'w', newline='') as cf:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(cf, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    else:
        print("Failed to fetch posts")
