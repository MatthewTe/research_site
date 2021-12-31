# Native Django Imports:
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User for Best Practices:
class CustomUser(AbstractUser):
    pass

# Research Models:
class Organization(models.Model):
    """The model for root organizations that created publications. These are larger, behind the
    scenes organizations that are connected to publications. Eg: The New York Times is the 
    publication and The New York Times Company is the organization.

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
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Publication(models.Model):
    """The model for the publications that are assocaited with Authors and their sources.
    The model connects with the Authors and Sources models in a Many-to-Many relationship
    indending to show which Sources are associated with which publications and respective
    Authors.

    Args:
        title (models.CharField): The publication name.

        publication_description (models.CharField): A short description on what type of publication it is.

        organization (models.ForeignKey): The organization that the publication is apart of. Connected to the
            Organization model via a Many-to-one relationship.

        url (models.URLField): The url for the organization.

    """
    title = models.CharField(max_length=50)
    publication_description = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    """A database model for authors of articles and other reading materials. It is meant
    to connect to Sources and Publication database models in a Many-to-One relationships. 

    Args:
        name (models.CharField): The name of the author.
        
        publication (models.ForeignKey): The Many-to-One relationship connecting the author to
            their publication. An author can only be connected to one Publication but a publication
            can have many authors.

    """
    name = models.CharField(max_length=50)
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Source(models.Model):
    """A source represents any reading material that is added to the database. It can be
    an article, research paper or offical report. This source material is connected to both
    the Publication and Author database model in a Many-to-Many relationship as it connects
    the actual reading material to the Publicatons and the Authors that sponsored them.

    Args:
        title (models.CharField): The title of the source.

        takeaway (models.CharField): A short (~200 word) summary of the souce. Basic takeaways from 
            reading the source.

        date_read (models.DateTimeField): The date that the source was read. 

        date_published (models.DateTimeField): The date that the source was published. 

        authors (models.ManyToManyField): The authors who wrote the article. This can connect to multiple
            authors from the Author database model.

        publications (models.ForeignKey): The publication where the source was published. This connects 
            to the Publication database model as a ForeginKey Many-to-One.

        url (models.URLField): The url for the source if it exists.

        topic (models.ManyToManyField): A field that describes the broad topic that the source is related to.
            it connects to the database model Topic via a Many-to-Many field.

    """    
    title = models.CharField(max_length=50)
    takeaway = models.CharField(max_length=250)
    date_read = models.DateTimeField()
    date_published = models.DateTimeField()
    authors = models.ManyToManyField(Author)
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True)
    url = models.URLField(null=True)
    topic = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_published"] 
