import streamlit as st
from googlesearch import search
from itertools import islice

class ResumeExplorer:
    def __init__(self):
        self.query = ""
        self.num_results = 0

        # List of technological positions with additional keywords
        self.technological_positions = {
            "Software Engineer": "Software Engineer resume OR CV OR curriculum vitae site:linkedin.com",
            "Data Scientist": "Data Scientist resume OR CV OR curriculum vitae site:linkedin.com",
            "Web Developer": "Web Developer resume OR CV OR curriculum vitae site:linkedin.com",
            "Database Administrator": "Database Administrator resume OR CV OR curriculum vitae site:linkedin.com",
            "Network Engineer": "Network Engineer resume OR CV OR curriculum vitae site:linkedin.com",
            # Add more positions with additional keywords as needed
            "Machine Learning Engineer": "Machine Learning Engineer resume OR CV OR curriculum vitae site:linkedin.com",
            "Frontend Developer": "Frontend Developer resume OR CV OR curriculum vitae site:linkedin.com",
            "System Administrator": "System Administrator resume OR CV OR curriculum vitae site:linkedin.com",
            # Add more positions and their keywords here
        }

        # Display the list of technological positions for the user to choose from
        st.title("Resume Explorer")
        st.write("List of Technological Positions:")
        for i, position in enumerate(self.technological_positions, start=1):
            st.write(f"{i}. {position}")

        # Input for user to choose a position
        user_input = st.text_input("Enter position number or name:")

        # Input for the number of results
        self.num_results = st.number_input("Enter the number of results to fetch:", value=5, min_value=1)

        # Button to start the search
        if st.button("Start Search"):
            self.start_search(user_input)

    def start_search(self, user_input):
        # Check if the user input is a number or a name
        if user_input.isdigit():
            position_index = int(user_input)
        else:
            # If the input is not a number, try to find the position by name
            position_index = next((i + 1 for i, pos in enumerate(self.technological_positions) if pos.lower() == user_input.lower()), None)

        # Check if a valid position index was found
        if position_index is not None and 1 <= position_index <= len(self.technological_positions):
            position_name = list(self.technological_positions.keys())[position_index - 1]
            self.query = f"{self.technological_positions[position_name]} site:linkedin.com"

            # Search for potential candidates
            potential_candidates = self.search_candidates()

            # Display the LinkedIn profiles of potential candidates
            for i, candidate_url in enumerate(potential_candidates, start=1):
                st.write(f"Potential Candidate {i}: {candidate_url}")
        else:
            st.write("Invalid input. Please enter a valid position number or name.")

    def search_candidates(self):
        candidates = []

        # Use Google search to find potential candidates
        for j in islice(search(self.query), self.num_results):
            candidates.append(j)

        return candidates

if __name__ == "__main__":
    resume_explorer = ResumeExplorer()
