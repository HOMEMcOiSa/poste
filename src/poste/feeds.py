from django.contrib.syndication.views import Feed

from .models import Post

class LatestEntries(Feed):
    title = "System feeds" # title for the feed
    link = "/"
    description = "Description a feeds" # description of the feeds

    def items(self):
        return Post.objects.order_by('-pub_date')[:5]
