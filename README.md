**Character Generator**

**Version 1.9.1 Update** 

**Overview**
Update 1.9.1 — Introduced a new folder structure (`core-geni`) for ongoing backend development. 
This will eventually replace the old `core` folder as the project transitions toward faster 
implementations (Rust/C++), SQL database support, and improved scalability for large-scale 
character generation.

**Key Features**

* **Character Generation:** The script generates multiple characters based on user input.
* **Randomized Attributes:** It incorporates randomized attributes such as names, birth dates, locations, height, weight, hair and eye color, and personality types.
* **CSV Output:** The generated character data is exported to a structured CSV file, facilitating easy import into data analysis tools.
* **Summary Statistics:** The script provides summary statistics, including averages and demographics.
* **External Data Files:** The script organizes the data with external data files for names, countries, and regions.

**Getting Started**

1. Clone the repository.
2. Ensure that the data files (male_names.txt, female_names.txt, last_names.txt, countries.txt) are located within the data/ folder.
3. Run the main.py script and specify the desired number of characters to generate.
4. Generated profiles will be saved in the output/output.csv file.

**Requirements**

* Python 3.x
* No external libraries are required beyond standard Python modules.

**Contributing**

Contributions are welcome! If you wish to enhance the project, please follow these steps:

* Fork the repository.
* Create a new branch dedicated to your feature or bug fix.
* Implement your changes with clear and concise commits.
* Submit a pull request describing your changes.

**Code Documentation and Testing**

Please ensure that your code is well-documented and thoroughly tested. For significant changes, it is advisable to open an issue prior to discussing your plans.

**License**

This project is licensed under the MIT License. For further details, please refer to the LICENSE file.




