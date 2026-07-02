## Project Structure

```
automated-youtube-mixtape/
├─── .gitignore
├─── README.md
├─── pyproject.toml             # uv project file
├─── uv.lock
│
├── notebooks/                  # Section 3 exploration (Jupyter)
│   ├── 01_audio_basics.ipynb
│   ├── 02_pydub_editing.ipynb
│   ├── 03_mixtape_logic_prototype.ipynb
│   └── 04_video_generation_prototype.ipynb
│
├─── api/
│    ├─── __init__.py
│    ├─── routes.py
│
├─── assets/                # local runtime artifacts (gitignored)
│    ├─── audio/
│    └─── images/
│
├─── frontend/
│    ├─── __init__.py
│    ├─── streamlit_app.py
│
├─── outputs/
│
├─── services/                  # Pure logic, no API/UI awareness
│    ├─── __init__.py
│    ├── audio_loader.py         # load/validate audio files
│    ├─── discription_generator.py    # timestamps + YouTube description text
│    ├─── mixtape_generator.py        # merge tracks, crossfades, ordering
│    ├─── video_generator.py          # audio + background image -> video
│
└─── tests
     ├── test_mixtape_builder.py
     ├── test_description_generator.py
     └── test_api.py
```