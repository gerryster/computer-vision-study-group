# Computer Vision Study Group

This repo contains code and used as part of my computer vision study group. More information about this group [can be found here](https://docs.google.com/document/d/11lrBxT2PjmspmWQ14Av2Sh1bYO1e5vTNo3ZEdfEjjyk/edit?usp=sharing).

## Installation

Install the Python version specified in the .tool-versions file and then run:

```bash
pip install -r requirements.txt
```

### Testing

From the root directory of this project, run:

```bash
pytest
```

Also, [pytest-watch](https://github.com/joeyespo/pytest-watch) can be installed installed and tests can be auto ran on change by: `ptw`.

### Python Reminders

Because I am new to Python, here are some quick reference items for me.

Set a breakpoint: `import pdb; pdb.set_trace()`

## Attribution

The study group and this repository are based on "[Programming Computer Vision with Python](http://programmingcomputervision.com/)" by Jan Erik Solem (O'Reilly Media, 2012). The example-images directory is from that book and is included in this project for ease of reference and so that Git can notify me if I accidentally change any of the original images.
