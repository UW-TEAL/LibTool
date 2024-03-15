# Tateuchi East Asian Library Database

## Description
This web application serves as a dynamic and comprehensive platform for managing and accessing a vast literature collection. Built on the robust Django framework and utilizing a MySQL database hosted on AWS RDS, it offers a resilient and scalable solution for literature enthusiasts, researchers, and administrators. The platform features a rich, user-friendly interface designed with Bootstrap and enhanced by DataTables, enabling interactive and efficient exploration of literature records.

Key functionalities include a detailed display of literature collections with information sourced from WorldCat, Google Books API, and Open Library API, and an admin portal for straightforward collection management. Users benefit from advanced features such as real-time search, sorting, pagination, and the ability to export data to Excel, facilitating academic research and personal interest exploration. This project epitomizes a modern web application's power to make literature accessible and manageable on a large scale, supporting the dissemination and preservation of knowledge.

## Technologies Used
- Django
- MySQL
- AWS (EC2, RDS)
- Bootstrap
- DataTables
- Selenium
- Google Books API
- Open Library API

## Features
### Comprehensive Literature Collection Database
- **Dynamic Display of Collections:** Leveraging DataTables, our application presents a rich literature collection database that users can easily interact with. Features such as real-time search, sorting, and pagination enhance the user experience by allowing them to navigate through the database efficiently.
- **Detailed Book Information:** Each entry in our literature collection contains comprehensive details sourced from WorldCat, Google Books API, and the Open Library API, including titles, authors, publication years, genres, and summaries. For select books, direct links to digital copies or additional resources are provided, enriching the database's value for research and reading.
- **Export to Excel Feature:** Users have the capability to export the displayed literature collection data into an Excel file with just a click. 


### Admin Portal for Collection Management
- **Secure Access:** The admin portal, powered by Django, offers secure access to authorized users for the management of the literature collection. This ensures that only designated personnel can add, edit, or delete database entries.
- **Intuitive Interface for CRUD Operations:** The admin portal features an intuitive interface for performing CRUD (Create, Read, Update, Delete) operations. This allows administrators to:
    - **Add new literature:** Seamlessly integrate new books into the collection with detailed metadata.
    - **Edit existing entries:** Update book details as new information becomes available or to correct existing data.
    - **Delete literature:** Remove entries from the database as necessary, maintaining the collection's relevance and accuracy.
- **Bulk Uploads and Updates:** For efficient database management, the admin portal supports bulk uploading and updating capabilities, allowing for the streamlined addition or modification of literature records.

These features combine to make our web application a comprehensive and user-friendly resource for literature enthusiasts, researchers, and general readers alike, offering both extensive data on a wide range of literature and effective tools for collection management.


## Setup and Installation
1. Clone the repository
2. Install dependencies
3. Set up AWS services
4. Run the application

## Contact Information
Reach out to your supervisor for more details and set up instructions.
