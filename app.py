# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.preprocessing import StandardScaler

# app = Flask(__name__)
# CORS(app)  # This will allow all origins

# # Load the dataset
# df = pd.read_csv('final_data.csv')

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     skills_input = request.json.get('skills', [])
    
#     # Initialize user profile with zeros
#     user_profile = {skill: 0 for skill in ['AI', 'REACTJS', 'ML', 'NODEJS', 'EXCEL', 'POWER BI']}
    
#     # Update user profile based on input skills
#     for skill in skills_input:
#         if skill in user_profile:
#             user_profile[skill] = 1
    
#     user_df = pd.DataFrame([user_profile])
    
#     # Clean the dataset by selecting relevant columns
#     df_cleaned = df[['Company_Name', 'Designation', 'Location', 'Industry', 'AI', 'REACTJS', 'ML', 'NODEJS', 'EXCEL', 'POWER BI']]
    
#     # Normalize the data using StandardScaler for better results
#     scaler = StandardScaler()
#     df_scaled = scaler.fit_transform(df_cleaned[['AI', 'REACTJS', 'ML', 'NODEJS', 'EXCEL', 'POWER BI']])
#     user_scaled = scaler.transform(user_df)
    
#     # Calculate cosine similarity between the user's profile and all job postings
#     similarity_scores = cosine_similarity(user_scaled, df_scaled)
    
#     # Add similarity scores back to the dataframe
#     df_cleaned['Similarity_Score'] = similarity_scores[0]
    
#     # Sort jobs based on the similarity scores to recommend top matches
#     top_recommendations = df_cleaned.sort_values(by='Similarity_Score', ascending=False).drop_duplicates(subset=['Company_Name', 'Designation']).head(3)
    
#     # Return the top recommendations
#     recommendations = top_recommendations[['Company_Name', 'Designation', 'Location', 'Industry', 'Similarity_Score']].to_dict(orient='records')
#     return jsonify(recommendations)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)  # This will allow all origins

# Load the dataset
df = pd.read_csv('final_data.csv')  # Replace with your actual CSV file

@app.route('/recommend', methods=['POST'])
def recommend():
    skills_input = request.json.get('skills', [])
    
    # Initialize user profile with zeros
    user_profile = {skill: 0 for skill in ['AI', 'REACTJS', 'ML', 'NODEJS', 'EXCEL', 'POWER BI']}
    
    # Update user profile based on input skills
    for skill in skills_input:
        if skill in user_profile:
            user_profile[skill] = 1
    
    user_df = pd.DataFrame([user_profile])
    
    # Clean the dataset by selecting relevant columns
    df_cleaned = df[['Company_Name', 'Designation', 'Location', 'Industry', 'AI', 'REACTJS', 'ML', 'NODEJS', 'EXCEL', 'POWER BI']]
    
    # Normalize the data using StandardScaler for better results
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_cleaned[['AI', 'REACTJS', 'ML', 'NODEJS', 'EXCEL', 'POWER BI']])
    user_scaled = scaler.transform(user_df)
    
    # Calculate cosine similarity between the user's profile and all job postings
    similarity_scores = cosine_similarity(user_scaled, df_scaled)
    
    # Add similarity scores back to the dataframe
    df_cleaned['Similarity_Score'] = similarity_scores[0]
    
    # Sort jobs based on the similarity scores to recommend top matches
    top_recommendations = df_cleaned.sort_values(by='Similarity_Score', ascending=False).drop_duplicates(subset=['Company_Name', 'Designation']).head(3)
    
    # Return the top recommendations
    recommendations = top_recommendations[['Company_Name', 'Designation', 'Location', 'Industry', 'Similarity_Score']].to_dict(orient='records')
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
