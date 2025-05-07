# franky_projects
Control routines for the Franka Emika R3 using the franky Python API with real-time trajectory generation.
=======
# franky_project

Pick-and-place control for the Franka Emika R3 using the franky Python API.

## Structure

- `scripts/`: robot motion and gripper control routines
- `requirements.txt`: Python dependencies

## Setup

Requires Python 3.10+ and a real-time kernel.

Create and activate your virtual environment:
```bash
python3 -m venv ~/franky_env
source ~/franky_env/bin/activate
pip install franky-control

python3 scripts/pick_place_loop.py --host 10.150.5.51

Save and exit.

---

### 4. Freeze dependencies
```bash
source ~/franky_env/bin/activate
pip freeze > requirements.txt

