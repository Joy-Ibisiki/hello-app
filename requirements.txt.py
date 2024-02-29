file="""streamlit==1.20.0
pandas==1.3.5
numpy==1.21.6
"""

from pathlib import Path
Path("streamlit").mkdir(parents=True, exist_ok=True)
Path("./streamlit/project").mkdir(parents=True, exist_ok=True)

with open("streamlit/project/requirements.txt", "w") as f: 
    f.write(file)
