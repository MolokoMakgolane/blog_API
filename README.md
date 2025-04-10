A basic RESTful blog API built using Django and Django Rest Framework.
It supports creating, deleting, updating and reading blog posts.

Features:
  CRUD for blog posts
  API endpoints for listing users and their posts
  Django admin integration

API Endpoints
  Method	Endpoint       	Description	
 GET	   /api/posts/	    List all blog posts	
 POST	   /api/posts/	    Create a new blog post	
 GET	   /api/posts/<id>/	Get a specific blog post	
 PUT   	/api/posts/<id>/	Update a blog post	
 DELETE	/api/posts/<id>/	Delete a blog post	
 GET   	/api/users/	      List all users	
 GET	   /api/users/<id>/	Get user + their posts	

Admin access-Login to the Django Admin at: http://localhost:8000/admin to manage blog posts and users.


