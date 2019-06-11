import requests
import pprint
# Here we define our query as a multi-line string
query = '''
query ($id: Int, $page: Int, $perPage: Int, $search: String) {
    Page (page: $page, perPage: $perPage) {
        pageInfo {
            total
            currentPage
            lastPage
            hasNextPage
            perPage
        }
        media (id: $id, search: $search) {
            id
            title {
                english
                native
                romaji
            }
        }
    }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'search': str(input("Davay nazvanie anime: ")),
    'page': 1,
    'perPage': 1000
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})
pprint.pprint(response.json())
