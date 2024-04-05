# Introduction
As part of this assignment, our goal was to design a microservices-based e-commerce system, using Docker and Docker Compose to orchestrate these services efficiently. Each microservice is dedicated to a specific function of the e-commerce platform.

### System Architecture
The system has been divided into several microservices, each service plays a crucial role in the functioning of the platform. Here is a brief description of each microservice:
     User Service:
         Manages user registration, authentication and profile information.
         Exposes an API on port 5000.
     Product Service:
         Manages product catalog and stock levels.
         Exposes an API on port 5001.
     Order Service:
         Manages the ordering process, including shopping carts and order history.
         Exposes an API on port 5002.
     Payment Service:
         Handles payment processing for completed orders.
         Exposes an API on port 5003.
     API gateway (Traefik):
         Serves as an entry point for external requests and routes them to the appropriate microservices.

![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/9c0f2597-c374-4692-a13e-369d532da0c3)

How it works?
In the terminal, access the root directory and do the docker-compose up --build command to build, (re)create or start the services.

### A brief explanation of the important code files:
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/a36a3253-69aa-4363-a864-e8ef8950aa52)

***

## In the app.py file
### Flask Application Setup:
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/c5266b8e-5d5e-4c8d-a5be-73260e653b6c)
* This section initializes the Flask app and configures SQLAlchemy for database interaction.
* Flask and necessary modules are imported.
* app is initialized as a Flask instance.
* SQLAlchemy is initialized with the database URI pointing to 'sqlite:///products.db', indicating the SQLite database file path.
* SQLALCHEMY_TRACK_MODIFICATIONS is set to False to improve performance by disabling modification tracking.

### Product Model Definition:
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/f96a8a01-bb89-42f9-9f0d-d8bf15c97b00)
* Defines the Product model that inherits from db.Model.
* id, productName, description, price, and quantity attributes represent columns in the database table.

### Routes and Their Functions:
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/638fb71c-f1bf-470a-bbc6-f67fa6889259)
* Defines the root route '/'.
* Fetches all products from the database and converts them into a list of dictionaries.
* Renders the index.html template, passing the product list as data.
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/47096568-73aa-4779-8570-7d204d0983ee)
* Defines a route to fetch all products ('/products' - GET method).
* Retrieves all products from the database and returns them as JSON.
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/9c1f0415-0df2-4a1b-9884-c9339da0bacc)
* Defines a route to fetch a single product by ID ('/products/<int:product_id>' - GET method).
* Retrieves a product based on the provided product_id.
* Returns the product's details as JSON or a 'Product not found' message with a 404 status if not found.
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/84e88166-1b74-42be-a191-3cc805afd4fd)
* Defines a route to add a product ('/products' - POST method).
* Extracts product details from the request JSON.
* Creates a new Product instance and adds it to the database.
* Returns a success message after adding the product.
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/c619b712-f4bb-4ac6-91d6-d4918e88cc9c)
Defines a route to update a product by ID ('/products/<int:product_id>/update' - POST method).
Retrieves the product based on the provided product_id.
Updates the product's attributes with the received JSON data.
Commits the changes to the database and returns the updated product details or a 'Product not found' message with 404.
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/586355da-a298-4b1c-8bf1-4e84a4a481ae)
* Defines a route to delete a product by ID ('/products/<int:product_id>/delete' - POST method).
* Retrieves the product based on the provided product_id.
* Deletes the product from the database and commits the changes.
* Returns a success message for deletion or 'Product not found' with 404 if the product doesn't exist.
### Database Initialization and Application Run:
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/5cf30b8b-cc74-4b65-ac6a-6ffe02975151)
* Checks if the script is executed as the main program.
* Initializes the database tables based on the defined models (Product) using db.create_all().
* Runs the Flask application on 0.0.0.0:5001 in debug mode (debug=True).

***

## In the Dockerfile
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/e8c257b8-8662-483b-88cb-6678be512fb1)
As an overall functionality, this Dockerfile sets up a Docker image for running a Flask application (app.py) with its necessary dependencies, including the required Python packages listed in ‘requirements.txt’. It creates an environment where the Flask application can run inside a container, initializing the necessary components, and launching the application using the ‘CMD’ instruction.

***

## In the index.html:
### Navigation:
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/858254bf-851e-4c95-9e8c-2f58afd4a525)
* The <header> contains a title "Order Service Navigation".
* The <nav> section includes an unordered list (<ul>) of links (<a>) pointing to different services (User, Product, Order, Payment) identified by their respective localhost URLs.

### Methods for Product Management (Add, Update, Delete):
**Add Product Form:**
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/7e5e39ec-130c-4fa1-9b34-282c207ef624)
* The form allows users to add a new product via a POST request to /products.
* Fields include Product Name, Description, Price, and Quantity.

**Table for Displaying Products:**
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/0262ea2f-ffe3-4d5b-8045-794dbc441abf)
* Renders a table displaying product information fetched from the server.
* Table headers include Product Name, Description, Price, Quantity, and Actions.

### JavaScript for Product CRUD Operations:
**Delete Product Functionality:**
![image](https://github.com/saad-mhmd/Dockerized_Web_Server/assets/156656627/3dfbfb6a-37de-4a4c-8557-9ad32b5b7b83)
* Sets up a listener for clicks on elements with the class delete-btn (e.g., the 'Delete' button).
* Performs an AJAX POST request to delete a specific product based on its ID when the 'Delete' button is clicked.
* Upon success or failure, appropriate actions or UI updates can be executed within the success and error callbacks.

***

These are the main parts of the project. The project still has a lot of issues to be fixed. Nevertheless, it represented an educational journey in the world of Docker and highlighted, through a simple project, the benefits that it brings to the world of technology and computers. 
