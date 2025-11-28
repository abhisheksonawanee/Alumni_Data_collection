# ESB Alumni & Student Journey Dashboard

A Streamlit application for collecting and managing alumni and student journey data for the Eberhardt School of Business at the University of the Pacific.

## Features

- **3-Step Survey Form**: Collect student information, internship experiences, and job outcomes
- **Database Integration**: SQLite database for storing all collected data
- **Custom Styling**: Branded with University of the Pacific colors and styling
- **Responsive Design**: Clean, modern UI with step-by-step navigation

## Local Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize the database** (if not already created):
   - The database `esb.db` will be created automatically when you first run the app
   - Or run the SQL schema from `schdb.sql` to set up the database structure

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Access the app**:
   - Open your browser to `http://localhost:8501`

## Deployment to Streamlit Cloud

### Option 1: Deploy via Streamlit Cloud (Recommended)

1. **Push your code to GitHub**:
   - Create a new repository on GitHub
   - Push all files including:
     - `app.py`
     - `db.py`
     - `requirements.txt`
     - `.streamlit/config.toml`
     - `esb.db` (if you want to include initial data)
     - `pacific_logo.jpg` (optional)
     - `creator_photo.jpg` (optional)

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository
   - Set the main file path to `app.py`
   - Click "Deploy"

3. **Your app will be live** at: `https://your-app-name.streamlit.app`

### Option 2: Deploy via Streamlit Community Cloud

1. **Requirements**:
   - GitHub account
   - Repository with your code
   - `requirements.txt` file (already created)
   - `.streamlit/config.toml` file (already created)

2. **Steps**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Click "New app"
   - Select repository: `Alumni_Data_collection`
   - Main file path: `app.py`
   - Click "Deploy"

## File Structure

```
Alumni_Data_collection/
├── app.py                 # Main Streamlit application
├── db.py                  # Database helper functions
├── esb.db                 # SQLite database (created automatically)
├── schdb.sql              # Database schema
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── pacific_logo.jpg       # University logo (optional)
└── creator_photo.jpg      # Creator photo (optional)
```

## Important Notes

- **Database**: The SQLite database (`esb.db`) will be created automatically if it doesn't exist. Make sure the database schema matches `schdb.sql`.
- **Images**: Logo and creator photo can be uploaded through the app interface or included in the repository.
- **Data Persistence**: On Streamlit Cloud, the database persists between sessions, but consider backing up important data regularly.

## Troubleshooting

- **Database errors**: Ensure `esb.db` exists or the schema is properly initialized
- **Import errors**: Make sure all dependencies in `requirements.txt` are installed
- **Image not loading**: Check that image files are in the correct directory and have proper permissions

## Support

For issues or questions, please contact the development team.

---

**Created by**: Abhishek Jitendra Sonawane

