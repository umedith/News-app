class Article:
    '''
    Articles class to define News Objects
    '''
    def __init__(self,id,author,title,description,url,image_url,content,publishedAt):
        self.id =id
        self.title = title
        self.description= description
        self.url = url
        self.image_url = image_url
        self.content = content
        self.publishedAt = publishedAt
        self.author = author
        # self.vote_count = vote_count

        