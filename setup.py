import sys
import os
import streamlit
from cx_Freeze import setup, Executable

# Streamlit data layout source assets files internal structure tracing configuration
streamlit_dir = os.path.dirname(streamlit.__file__)

build_exe_options = {
    "packages": ["streamlit", "pandas", "numpy", "joblib", "sklearn", "os", "sys"],
    "include_files": [
        "prediction.py",
        # Automatically include internal structural files layout models configurations
        (os.path.join(streamlit_dir, "static"), "lib/streamlit/static"),
        (os.path.join(streamlit_dir, "runtime"), "lib/streamlit/runtime")
    ],
    "excludes": ["tkinter"]
}

base = None
if sys.platform == "win32":
    base = "Console"

setup(
    name="PriceChilli",
    version="1.0",
    description="PriceChilli Enterprise Standalone Analytics Desktop Suite",
    options={"build_exe": build_exe_options},
    executables=[Executable("run_app.py", base=base, target_name="PriceChilli.exe")]
)
