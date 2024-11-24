# Django Permissions and Groups Implementation

This project demonstrates how to manage permissions and groups in a Django application to restrict access to specific parts of the application. The focus is on using Django's built-in permissions framework to enhance security and provide role-based access control.

## Features
- Custom permissions for controlling model actions like view, create, edit, and delete.
- User groups with assigned permissions for role-based access.
- Secure views that enforce permission checks using Django's `permission_required` decorator.

---

## Custom Permissions
Custom permissions were added to the `Book` model. These permissions include:
- `can_view`: Permission to view books.
- `can_create`: Permission to create new book entries.
- `can_edit`: Permission to edit book details.
- `can_delete`: Permission to delete book entries.

### Code Snippet: Adding Permissions
```python
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ('can_view', 'Can view books'),
            ('can_create', 'Can create books'),
            ('can_edit', 'Can edit books'),
            ('can_delete', 'Can delete books'),
        ]