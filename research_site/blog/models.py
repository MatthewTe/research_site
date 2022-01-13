# Importing default django packages:
from django.db import models
from django.template.defaultfilters import slugify

# Importing models from the research core:
from research_core.models import Topic

# Importing 3rd party packages:
from tinymce import models as tinymce_models

class BlogPost(models.Model):
    """The main model for Blog Posts. The main content for the blog is rendered via a 
    tinymce HTML field and it connects to the research_core application via a ForeginKey
    connecton to the Topic model. 

    Args:
        title (models.CharField): The title of the blog post that is displayed on the page and
            is used to generate the slug (unique ID) for the post.
        
        blog_thumbnail (models.ImageField): The image that is used as the thumbnail and header image
            in the blog post. If none is provided that thumbnail img for the posts' Topic object is used.

        content (tinymce.HTMLField): The main content of the blog post. It is HTML content that is stored in
            the database and is ediable in the admin page as a fully functional text editor. This field is
            a 3rd party package called TinyMCE that deals with all CRUD functions of the text field.

        published_at (models.DateTimeField): The datetime when the blog post was created.

        last_updated (models.DateTimeField): The datetime when the last changes were made to the model instance.

        slug (models.SlugField): The unique URL identifier that is used to query specific blog posts. It is generated
            by 'slugifying' the title or can be directly created.

        topic (models.ForeignKey): The topic that the blog post is assocaited with. It connects to the topic object in the
            'research core' application via a ForeignKey.

    """
    # Model Specific Fields:
    title = models.CharField(max_length=250, unique=True)
    blog_thumbnail = models.ImageField(upload_to="blog/thumbnails", null=True, blank=True, default=None)
    content = tinymce_models.HTMLField()
    published_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=300, unique=True, null=True, blank=True)

    # Foregin Connection Fields:
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):    
        # If slug field is empty, generate slug based off of title:
        if self.slug:
            pass
        else:
            self.slug = slugify(self.title)

        # If there was no image field provided, use the thumbnail from the topic ForeginKey as the thumbnail: 
        if self.blog_thumbnail:
            pass
        else:
            self.blog_thumbnail = self.topic.topic_img
        
        super(BlogPost, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["-published_at"]
    
    def __str__(self):
        return self.title