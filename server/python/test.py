import meilisearch

client = meilisearch.Client('http://127.0.0.1:7700', 'myMasterKey1')

# An index is where the documents are stored.
index = client.index('movies')

documents = [
      { 'id': 1, 'title': 'Carol', 'genres': ['Romance', 'Drama'] },
      { 'id': 2, 'title': 'Wonder Woman jithin5', 'genres': ['Action', 'Adventure'] },
      { 'id': 3, 'title': 'Life of Pi', 'genres': ['Adventure', 'Drama'] },
      { 'id': 4, 'title': 'Mad Max: Fury Road', 'genres': ['Adventure', 'Science Fiction', 'jithin'] },
      { 'id': 5, 'title': 'Moana', 'genres': ['Fantasy', 'Action']},
      { 'id': 6, 'title': 'Philadelphia jithin', 'genres': ['Drama'] },
]

# If the index 'movies' does not exist, Meilisearch creates it when you first add the documents.
index.add_documents(documents) # => { "uid": 0 }

print(index.search('jithin'))