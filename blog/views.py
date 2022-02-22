from django.urls import reverse
from django.views.generic import ListView, DetailView


from .models import BlogPost


class BreadCrumbMixin:
    # Breadcrumbs must containing a dict of title => url_name
    # url_name will be used in django's reverse() function
    # example :
    # breadcrumbs = {
    #     "billets": "blog_post:list",
    #     "les recettes": "blog_post:tag-recette",
    # }
    breadcrumbs = dict()

    def get_context_breadcrumbs(self, pre_crumbs=None, next_crumbs=None):
        crumbs = [
            {"href": reverse("blog_post:list"), "title": "Accueil"},
        ]
        try:
            for title, url_name in self.breadcrumbs.items():
                crumbs.append({"title": title, "href": reverse(url_name)})
        except AttributeError:
            pass
        return crumbs

    def get_context_data(self, **kwargs):
        """Add bredcrumbs to context"""
        breadcrumbs = self.get_context_breadcrumbs()
        breadcrumbs[-1]["is_active"] = True
        kwargs.update({"breadcrumbs": breadcrumbs})
        return super().get_context_data(**kwargs)


class BlogPostListView(BreadCrumbMixin, ListView):
    template_name = "blog/list.html"
    context_object_name = "blog_posts"
    queryset = BlogPost.objects.filter(is_published=True).order_by("-created_date")


class BlogPostDetailView(BreadCrumbMixin, DetailView):
    template_name = "blog/detail.html"
    context_object_name = "blog_post"
    queryset = BlogPost.objects.filter(is_published=True)

    def get_context_breadcrumbs(self):
        crumbs = super().get_context_breadcrumbs()
        crumbs += [
            {
                "href": reverse("blog_post:detail", args={"slug": self.object.slug}),
                "title": self.object.title
            }
        ]
        return crumbs
