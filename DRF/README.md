# DRF

Models for Post and Comment should belong to the user (FK relationship).

Serializers for these models.

CRUD operations using viewsets for working with these models in a way that:

- All users can view posts and comments.
- Only logged-in users can add posts and comments.
- Only owners can edit or delete posts or comments (when a post is deleted, all comments are deleted regardless of their owners - on_delete=Cascade).
