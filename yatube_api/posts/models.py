from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title[:20]


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    group = models.ForeignKey(Group,
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL,
                              related_name="posts",
                              )
    image = models.ImageField(
        upload_to="images/", null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        ordering = ("pub_date",)

    def __str__(self):
        return self.text[:20]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.text[:20]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="follower",
        null=True,
    )
    following = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="following",
        null=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["following", "user"],
                name="unique_follow", )
        ]

    def __str__(self):
        return f"{self.user} - подписчик {self.following}"
