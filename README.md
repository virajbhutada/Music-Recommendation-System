
![Screenshot 2024-06-20 201356](https://github.com/virajbhutada/Music-Recommendation-System/assets/143819712/11b27a9b-e432-45f4-8f88-138ee17eae14)

# Music Recommendation System


- ## Table of Contents
  - [Problem Statement](#problem-statement)
  - [Overview](#overview)
  - [Dataset Details](#dataset-details)
  - [Methodologies](#methodologies)
  - [Project Structure](#project-structure)
  - [Usage Instructions](#usage-instructions)
  - [Contribution Guidelines](#contribution-guidelines)
  - [Key Recommendations](#key-recommendations)
  - [Conclusion](#conclusion)
  - [MIT License](#mit-license)


---

## Problem Statement
In today's digital age, despite the vast availability of music, users often struggle to find tracks that match their specific preferences, especially for activities like meditation and relaxation. This challenge stems from the sheer volume of choices and the subjective nature of individual tastes.

---

## Overview
The Music Recommendation System aims to solve this problem by providing personalized music recommendations tailored to each user's preferences. Users can input their preferences through dropdown selections and the system utilizes both user-provided data and automatically gathered information to enhance the accuracy of recommendations. This project leverages various data analysis and machine learning techniques to improve the recommendation process, ensuring that users discover music that resonates with their tastes and enhances their listening experience.

---

## Dataset Details
The dataset used in this project consists of various attributes related to Spotify tracks, including:

| Attribute             | Description |
|-----------------------|-------------|
| *user_id*           | A unique identifier for Spotify users, essential for tracking user-specific data and preferences. |
| *Track Name*        | The name of the track, allowing users to identify their preferred songs. |
| *Artist Name(s)*    | The name of the artist(s) associated with the track, providing additional context and aiding in artist-specific recommendations. |
| *Album Name*        | The name of the album to which the track belongs, useful for users who prefer album-based listening. |
| *Album Release Date*| The release date of the album, which can help in filtering tracks by release period. |
| *Track Number*      | The unique track number within the album, assisting in maintaining the order of tracks as they appear in the album. |
| *Track Duration (ms)*| The duration of the track in milliseconds, which can be useful for time-based filtering. |
| *Explicit*          | An indicator if the track contains explicit content, allowing for filtering based on content appropriateness. |
| *Popularity*        | A measure indicating how popular a track is based on its play count, aiding in recommending trending music. |
| *Added By*          | The user who added the track to a playlist, which can help in collaborative filtering. |
| *Added At*          | The timestamp when the track was added to the playlist, useful for tracking the timeline of user activity. |
| *Danceability*      | A metric describing how suitable a track is for dancing based on tempo, rhythm stability, beat strength, and overall regularity. |
| *Energy*            | A perceptual measure of intensity and activity in the track, helping to match tracks to user activity levels. |
| *Key*               | The key in which the track is performed. Integers map to pitches using standard Pitch Class notation, useful for music theory-based recommendations. |
| *Loudness*          | The loudness of the track in decibels (dB), aiding in adjusting for volume preferences. |
| *Mode*              | Indicates the modality (major or minor) of the track, which can influence the emotional tone of the music. |
| *Speechiness*       | The presence of spoken words in the track, measured as the ratio of speech-like sounds to music-like sounds. |
| *Acousticness*      | A confidence measure from 0.0 to 1.0 indicating whether the track is acoustic, useful for users who prefer acoustic music. |
| *Instrumentalness*  | Predicts whether a track contains vocals. Higher values suggest instrumental tracks, beneficial for background music. |
| *Liveness*          | Detects the presence of an audience in the recording. Higher values represent a higher probability of a live audience. |
| *Valence*           | A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track, helping to match music to user mood. |
| *Tempo*             | Beats per minute (BPM) of the track, which can influence the energy and pace of the music. |
| *Time Signature*    | The estimated overall time signature of the track, useful for rhythm matching. |

---

## Methodologies
The project employs the following methodologies:
- **Data Collection**: Aggregating data from Spotify API and user inputs. This ensures a rich and diverse dataset to base recommendations on.
- **Data Preprocessing**: Cleaning and structuring the dataset for analysis, which is crucial for accurate and efficient model training.
- **Feature Engineering**: Extracting and refining features relevant to music recommendation. This step enhances the model's ability to understand and predict user preferences.
- **Similarity Metrics**: Calculating similarity between tracks based on various audio features. This helps in grouping similar tracks together for better recommendations.
- **Machine Learning**: Implementing algorithms to predict user preferences and generate recommendations. Machine learning models learn from user behavior to provide more accurate suggestions.
- **Evaluation**: Testing the recommendation accuracy and refining the model. Continuous evaluation helps in improving the recommendation quality over time.

---

## Project Structure

- **alltracks.py**: Contains the logic for handling and processing all tracks data, ensuring that all track-related information is accurately processed.
- **app.py**: Main application script for running the recommendation system. This is the entry point for users to interact with the system.
- **link.py**: Manages the linkage and integration of different components. Ensures seamless communication between various modules of the system.
- **main.py**: Entry point for the system, initializing and running the application. This script sets up the environment and starts the application.
- **music.ipynb**: Jupyter notebook containing data analysis and model development. This is used for experimenting with and developing the recommendation algorithms.
- **projectcode.py**: Core logic for the music recommendation algorithms. Contains the implementation of the recommendation models and their logic.
- **requirement.txt**: List of dependencies required for the project. Ensures that all necessary libraries and packages are installed.
- **streamlitapp.py**: Script for running the Streamlit web application interface. Provides a web-based interface for users to interact with the system.
- **data/**: Directory containing dataset files. Organized storage of all dataset files used in the project.
- **report/**: Folder containing project reports and documentation. Maintains all relevant documentation and reports for the project.
- **html/**: Directory containing HTML files with assets and artifacts. Stores all HTML files required for the web interface.

---

## Usage Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/virajbhutada/Music-Recommendation-System.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Music-Recommendation-System
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python app.py
   ```
5. **Running the Streamlit app**:
   ```bash
   streamlit run streamlitapp.py
   ```

---

## Contribution Guidelines

[![Pull Requests](https://img.shields.io/badge/Make%20a%20Pull%20Request-green)](https://github.com/virajbhutada/Music-Recommendation-System/pulls) [![Issues](https://img.shields.io/badge/Report%20an%20Issue-red)](https://github.com/virajbhutada/Music-Recommendation-System/issues) [![Discussions](https://img.shields.io/badge/Join%20the%20Discussion-blue)](https://github.com/virajbhutada/Music-Recommendation-System/discussions) [![Code Style](https://img.shields.io/badge/Check%20Code%20Style-orange)](https://github.com/virajbhutada/Music-Recommendation-System/blob/main/CODE_STYLE.md) [![Clone Repository](https://img.shields.io/badge/Clone%20Repository-gray)](https://github.com/virajbhutada/Music-Recommendation-System.git) [![Push Changes](https://img.shields.io/badge/Push%20Changes-blue)](https://github.com/virajbhutada/Music-Recommendation-System)

- **Pull Requests**: We welcome pull requests. Please ensure your code follows the project’s coding standards. Before submitting, make sure your code is well-documented and tested.
- **Issues**: If you find any issues or have suggestions, please create an issue on the GitHub repository. Clear and detailed issue reports help us improve the project efficiently.
- **Discussions**: Join the discussion about this project. Ask questions, share ideas, and collaborate with the community.
- **Code Style**: Check the code style guidelines to ensure your contributions meet the project's coding standards and practices.
- **Clone Repository**: Clone this repository to your local machine to get a copy of the project for development or testing purposes.
- **Push Changes**: Push your changes back to the remote repository after making modifications or improvements to the codebase.

---



## Key Recommendations 

- **Enhanced Personalization**: Implement advanced machine learning techniques for more personalized recommendations. This can include deep learning models or hybrid recommendation systems.
- **Real-time Updates**: Integrate real-time data streaming to keep recommendations up-to-date. This ensures that user preferences are always reflected accurately.
- **User Interface Optimization**: Improve the UI for better user experience and easier navigation. A user-friendly interface can significantly enhance the overall experience.
- **Expand Dataset Coverage**: Continuously expand the dataset to include a wider variety of music genres. A diverse dataset can cater to a broader audience.
- **Incorporate Feedback Mechanisms**: Develop user feedback systems to refine recommendations. User feedback can provide valuable insights into improving the system.
- **Ethical Considerations**: Ensure transparency in data usage and respect user privacy. Ethical considerations are crucial for maintaining user trust and compliance with regulations.

---

## Conclusion

The Music Recommendation System enhances user experience by providing personalized music suggestions for relaxation and meditation. Leveraging advanced data analysis and machine learning, the system delivers precise recommendations based on user preferences, including tempo, energy, and genre. Incorporating user feedback and ethical considerations ensures transparency and privacy.

Future enhancements include real-time data streaming for updates, UI improvements for intuitive interaction, and dataset expansion for broader music genre coverage. Join us in shaping the future of music discovery through collaborative contributions to the Music Recommendation System.

Feel free to contribute, provide feedback, and make the most out of this system to enrich your musical journey!

---

## MIT License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/virajbhutada/Music-Recommendation-System/blob/main/LICENSE) file for details.


### Connect With Me 

**[![LinkedIn](https://img.shields.io/badge/LinkedIn-Viraj%20Bhutada-blue?logo=linkedin)](https://www.linkedin.com/in/virajnbhutada24/)**

