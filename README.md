# Aedric-Addington-Python-Portfolio
Aedric Addington's Senior Year Highschool Python Portfolio

Project 1: Dinosaur Finder
Summary
This interactive command-line application allows users to explore and filter a dataset containing details on over 300 Mesozoic animals. It parses data from a custom CSV file to provide comprehensive breakdowns of individual dinosaur profiles, physical traits, and historical discoveries.
Key Features
Multi-Criteria Filtering: Enables searches across nine distinct categories, including taxonomy, geographic location, diet, and geological period.
Dynamic Range Searching: Filters physical attributes like length by parsing and converting string data into numeric values for comparative analysis.
Input Normalization: Uses case-insensitive matching and string cleaning to catch user formatting variations.
Robust Error Handling: Employs try-except blocks to handle invalid entries and maintain continuous program execution.
Paced User Interface: Integrates time delays to give users adequate time to read large data tables before the screen refreshes.

Project 2: Hogwarts House Sorting Hat
Summary
This command-line script simulates the iconic Harry Potter Sorting Hat experience by assigning users to a Hogwarts house. It utilizes predefined lore-based overrides for specific characters alongside a randomized assignment mechanism for original names.
Key Features
Conditional Lore Overrides: Detects canonical character names to automatically assign them to their historically accurate houses.
Randomized Selection: Employs pseudo-random selection to dynamically distribute unknown user names among the four traditional houses.
Immersive User Interface: Integrates sequential time delays to mimic a suspenseful, narrative-driven decision process.
Persistent Execution Loop: Features a continuous validation loop that allows users to instantly restart or exit the program on demand.

Project 3: Interactive Mad Libs Generator
Summary
This terminal-based game allows users to generate custom, multi-part comedic stories by submitting various parts of speech. It features a branchable two-part narrative structure that dynamically inserts user entries and randomized fallback options into styled text layouts.
Key Features
Dynamic Content Randomization: Employs fallback lists that automatically select random placeholder names if the user inputs "RANDOM".
String Case Standardization: Sanitizes all text inputs using capitalization methods to maintain uniform text formatting.
ANSI Escape Styling: Integrates embedded ANSI escape codes to render generated variables in bold and italic styles within the terminal.
Conditional Narrative Branching: Uses localized control flow checks to let users choose whether to conclude the game or extend the story into a complex second act.
State Preservation: Keeps variable references active across multiple code paths to weave early user inputs directly into the final story climax.

Project 4: Superhero Nickname Generator
Summary
This terminal application functions as a interactive personality quiz that assigns users a famous comic book superhero moniker. It relies on a deeply nested binary decision tree to map personal traits and behavioral preferences directly to corresponding pop-culture alter egos.
Key Features
Nested Control Flow: Features a complex hierarchical if-elif-else architecture to manage multi-layered, conditional user pathways.
Input Sanitization: Automatically formats terminal inputs to lowercase to prevent program crashes from inconsistent text casing.
Explicit Input Catching: Implements fallback error flags across every branching logic layer to instantly flag invalid user responses.
Persistent Session Loops: Wraps the entire core algorithm inside a continuous verification system so users can repeatedly test different character paths.

Project 5: Persistent Reading List Manager
Summary
This terminal application serves as a personal reading tracker that allows users to manage a reading wish list and track completed books. It features persistent file storage, dynamic index-based content manipulation, and motivational milestones based on user progress.
Key Features
Persistent File I/O: Implements flat-file storage to save and parse separate to-read and completed states across program restarts.
List Index Mapping: Translates 1-indexed user menu selections into 0-indexed array lookups for secure dataset target targeting.
Dynamic Content Reallocation: Pops items from active tracking structures and inserts them into history lists when milestones are met.
Conditional Gamification Flags: Triggers automated motivational feedback milestones when the completed history array reaches specific target counts.
Comprehensive Data Safety: Incorporates structural confirmation checks and data resetting paths alongside type-checked input handlers.

Project 6: Chicago Traffic Data Analyzer
Summary
This data analysis script processes traffic volume records across fifty major streets in Chicago. It utilizes parallel data arrays to perform filtering operations, identify maximum values, and isolate high-congestion thoroughfares based on user-defined thresholds.
Key Features
Parallel Array Processing: Synchronizes matching indices across separate string and integer lists to pair location names with numeric data points.
Linear Threshold Filtering: Iterates through a complete numeric dataset to dynamically isolate elements that meet or exceed a specific value.
Extrema Identification: Leverages built-in evaluation methods to instantly pinpoint the maximum value and retrieve its exact positional index.
Algorithmic Search Efficiency: Extracts targeted metadata directly from synchronized collections without needing a heavy third-party data library like Pandas.
