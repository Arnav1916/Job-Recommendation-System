import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [skills, setSkills] = useState(['', '', '']);
  const [recommendations, setRecommendations] = useState([]);

  // List of skills for dropdown
  const skillOptions = [
    'JavaScript', 
    'Python', 
    'Java', 
    'React', 
    'Node.js', 
    'SQL', 
    'Machine Learning', 
    'Data Analysis', 
    'HTML/CSS', 
    'AWS', 
    'Docker'
  ];

  const handleSkillChange = (index, value) => {
    const newSkills = [...skills];
    newSkills[index] = value;
    setSkills(newSkills);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/recommend', { skills });
      setRecommendations(response.data);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    }
  };

  return (
    <div className="App">
      <h1>Job Recommendation System</h1>
      <form onSubmit={handleSubmit}>
        {skills.map((skill, index) => (
          <div key={index}>
            <label>
              Skill {index + 1}:
              <select
                value={skill}
                onChange={(e) => handleSkillChange(index, e.target.value)}
              >
                <option value="">Select a skill</option>
                {skillOptions.map((option) => (
                  <option key={option} value={option}>
                    {option}
                  </option>
                ))}
              </select>
            </label>
          </div>
        ))}
        <button type="submit">Get Recommendations</button>
      </form>
      {recommendations.length > 0 && (
        <ul>
          {recommendations.map((rec, index) => (
            <li key={index}>
              <h3>{rec.Company_Name}</h3>
              <p>{rec.Designation}</p>
              <p>{rec.Location}</p>
              <p>{rec.Industry}</p>
              <p>Similarity Score: {rec.Similarity_Score.toFixed(2)}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
