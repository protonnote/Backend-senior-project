# Backend facial authentication system for building access using adaptive machine learning algorithms #


## Installation ##
- **Python on Windows**
    1. Go to  [Python.org](https://www.python.org/downloads/) for download Python installer.
    2. Open setup file.
    3. Click Install now and wait untill success.
    4. After installed Python open Windows Terminal or PowerShell.
    5. Use command : ``python -V`` or `` python --version ``.
    6. If installed successfully Terminal or PowerShell will show Python version eg. `` 3.9.8 ``.

- **Flask framework**
    1. Open Windows Terminal or PowerShell.
    2. Use command : `` pip install Flask ``

- **OpenCV on Windows**
    1. Open PowerShell or Windows Terminal.
    2. Use command : `` pip install opencv-python `` and wait untill success.
    3. After installed use command : `` python `` and type
    > \>>import cv2 \
    \>>cv2.\__version__
    4. If install success it will show version of OpenCV eg.`` 4.5.2 ``.


- **Scikit learn on Windows**
    1. Open PowerShell or Windows Terminal.
    2. Use command : `` pip install scikit-learn `` and wait untill success.


## Usage ##
After use `` git colne `` command for download this repository.
1. Open PowerShell or Windows Terminal.
2. Edit ``UPLOAD_FOLDER`` to ``upload`` folder path.
 *you can use these command to see upload directory ``pwd`` command.
```python
    from flask import Flask

    UPLOAD_FOLDER = 'path-of-upload-folder' <------- edit path

    app = Flask(__name__)
    app.secret_key = "secret-key"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
```
3. Use command : `` python main.py `` for start server.