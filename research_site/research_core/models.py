# Native Django Imports:
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User for Best Practices:
class CustomUser(AbstractUser):
    pass

# Research Models:
class Organization(models.Model):
    """The model for root organizations that created Publishers. These are larger, behind the
    scenes organizations that are connected to Publishers. Eg: The New York Times is the 
    Publishers and The New York Times Company is the organization.

    Args:
        title (models.CharField): The organization name.

    """
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Topic(models.Model):
    """The categories of topics that are used to categorize Sources. These are used to
    search and organize each source and as such are connected to Sources via its 
    Many-to-Many field.

    Args:
        topic (models.CharField): The name of the topic.

    """
    #TODO: Incorpoate Image Uploading for Topic model to create Card Thumbnails and Carousel Imgs
    
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.topic

class Publisher(models.Model):
    """The model for the publishers that are assocaited with Authors and their sources.
    The model connects with the Authors and Sources models in a Many-to-Many relationship
    indending to show which Sources are associated with which publishers and respective
    Authors.

    Args:
        title (models.CharField): The publisher name.

        publisher_description (models.CharField): A short description on what type of publisher it is.

        organization (models.ForeignKey): The organization that the publisher is apart of. Connected to the
            Organization model via a Many-to-one relationship.

        url (models.URLField): The url for the organization.

    """
    title = models.CharField(max_length=50)
    publisher_description = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    """A database model for authors of articles and other reading materials. It is meant
    to connect to Sources and Publisher database models in a Many-to-One relationships. 

    Args:
        firstname (models.CharField): The first name of the author.
        
        middlename (models.CharField): The middle name of the author
        
        lastname (models.CharField): The last name of the author
        
        publisher (models.ForeignKey): The Many-to-One relationship connecting the author to
            their publisher. An author can only be connected to one Publisher but a publisher
            can have many authors.

    """
    firstname = models.CharField(max_length=50, null=True, blank=True)
    middlename = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class SourceType(models.Model):
    """The basic database model describing the category the Source object belongs too.
    It connects to the Source object through a Source ForeginKey. This is the model's 
    primary purpose.

    Eg:
        Journal Article, Blog Post, Research Paper, Report, etc.

    Args: 
        source_type (models.CharField): The type of souce that will be used to classify the Source 
            object eg: Report.
    """
    source_type = models.CharField(max_length=100)

    def __str__(self):
        return self.source_type

class Source(models.Model):
    """A source represents any reading material that is added to the database. It can be
    an article, research paper or offical report. This source material is connected to both
    the Publisher and Author database model in a Many-to-Many relationship as it connects
    the actual reading material to the Publicatons and the Authors that sponsored them.

    Args:
        title (models.CharField): The title of the source.

        takeaway (models.TextField): A short summary of the souce. Basic takeaways from 
            reading the source.

        date_read (models.DateTimeField): The date that the source was read. 

        date_published (models.DateTimeField): The date that the source was published. 

        authors (models.ManyToManyField): The authors who wrote the article. This can connect to multiple
            authors from the Author database model.

        source_type (models.ForeignKey): A ForeginKey connection to the SourceType data model describing 
            what category of source it is. Eg: Journal Article or Blog Post.

        publisher (models.ForeignKey): The publisher where the source was published. This connects 
            to the Publisher database model as a ForeginKey Many-to-One.

        url (models.URLField): The url for the source if it exists.

        topic (models.ManyToManyField): A field that describes the broad topic that the source is related to.
            it connects to the database model Topic via a Many-to-One field as a Source can have one topic but
            a topic can have many Sources.

    """    
    #TODO: Incorpoate Image Uploading for Source model to create thumbnails and make homepage dynamic.

    title = models.CharField(max_length=200)
    takeaway = models.TextField()
    date_read = models.DateTimeField()
    date_published = models.DateTimeField()
    authors = models.ManyToManyField(Author)
    source_type = models.ForeignKey(SourceType, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    url = models.URLField(null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_published"] 