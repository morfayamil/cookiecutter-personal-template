# {{ cookiecutter.project_title }}

{{ cookiecutter.project_description }}

## Project Features
- Python: {% if  cookiecutter.python_interpreter == "python3" %} 3.7+ {% else %} 2.7 {%endif%}


## Requirements
- Anaconda >= 4.x
- git >= 2.x

## Directories Distribution
```

    {{ cookiecutter.project_slug }}
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        ├── LICENSE            <- License
        │
        └── README.md          <- The top-level README for developers using this project.

```