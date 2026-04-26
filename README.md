# CS-340-MongoDB-Dashboard

Grazioso Salvare Dashboard Project
Overview
This project involved the development of an interactive dashboard application for Grazioso Salvare, an international rescue animal training organization. The purpose of the application is to assist in identifying and categorizing dogs from shelter data that are suitable for different types of search-and-rescue training.
The dashboard provides a user-friendly interface that allows users to filter, explore, and visualize animal data. This reduces the time required to identify suitable candidates and improves the overall efficiency of the selection process.
Functionality
The application allows users to filter animal data based on specific rescue categories, including Water Rescue, Mountain or Wilderness Rescue, and Disaster or Tracking. A reset option is also available to return the dashboard to its original unfiltered state.
The data table dynamically updates based on the selected filter, displaying only the animals that meet the criteria for the chosen rescue type. In addition to the table, a pie chart is used to visualize the distribution of the top ten dog breeds within the filtered dataset.
A geolocation map is also included, which updates based on the selected row in the data table. This allows users to view the geographic location associated with a specific animal entry.
The dashboard also includes the Grazioso Salvare logo and a user identifier to ensure proper branding and attribution.
Screenshots demonstrating the functionality of the dashboard are included at the end of this document.
Tools and Technologies
MongoDB was used as the database component for this project due to its flexibility in handling semi-structured data. Its document-based format aligns naturally with Python dictionaries, making it efficient for storing and querying animal data.
Python was used as the primary programming language for implementing the application logic. A custom CRUD module was developed to manage database operations such as retrieving filtered datasets.
The Dash framework was used to build the dashboard interface. Dash integrates both the view and controller components, allowing for interactive elements such as radio buttons and dynamic updates through callbacks.
Plotly Express was used to create the data visualization component of the dashboard. Specifically, it was used to generate a pie chart representing breed distribution.
Dash Leaflet was used to implement the geolocation map, enabling the display of animal locations using latitude and longitude data.
Development Process
The development process began with setting up the MongoDB database using the Austin Animal Center dataset. A Python CRUD module was then created to handle database interactions.
An initial dashboard was built with an unfiltered data table to display all available records. From there, filtering functionality was implemented using MongoDB queries that match the requirements for each rescue type.
Interactive controls were added using radio buttons, allowing users to select different filters. These controls were connected to the data table through Dash callbacks, enabling real-time updates.
Additional components were then integrated, including a pie chart for visualizing breed distribution and a geolocation map for displaying animal locations.
The final step involved testing the dashboard to ensure that all components functioned correctly. Screenshots were taken to demonstrate the successful operation of each feature.
Challenges and Solutions
One challenge encountered during development was ensuring that MongoDB queries matched the dataset values exactly. Since MongoDB queries rely on precise string matching, careful attention was required when specifying breed names and other attributes.
Another challenge involved handling errors within Dash callbacks, particularly when dealing with empty or null data. This was resolved by adding conditional checks to prevent runtime errors and ensure stability.
There was also a challenge related to data formatting between MongoDB and the dashboard. Specifically, the ObjectId field needed to be removed to ensure compatibility with the Dash data table.
How to Run the Project
To run this project, MongoDB must be installed and running locally. The Austin Animal Center dataset should be loaded into the MongoDB database.
All project files should be placed in the same directory, including the dashboard notebook file, the CRUD Python module, and the logo image file.
The Jupyter Notebook can then be opened, and all cells can be executed to launch the dashboard application.
Conclusion
This project demonstrates the successful integration of MongoDB, Python, and the Dash framework to create a fully functional and interactive dashboard. The application meets all specified requirements and provides an efficient tool for identifying dogs suitable for rescue training.
The completed dashboard highlights the effectiveness of combining database systems with modern web-based visualization tools to create intuitive and powerful user interfaces.
