# djexp - Django Export

CLI application which exports Django models to json.

### Installation
```bash
$ pip install djexp
```

### Requirements
- Django

### Example
Terminal:
```bash
$ djexp -r ./ -s ProjectName.settings
```

Code:
```python
from djexpapp.task import export_django_models

export_django_models('root/directory', 'ProjectName.settings')
```

### Author
* [Yuriy Lisovskiy](https://github.com/YuriyLisovskiy)

### License
The project is licensed under the terms of the [GNU General Public License v3.0](https://opensource.org/licenses/GPL-3.0), see the [LICENSE](LICENSE) file for more information.
