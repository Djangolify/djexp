# djexp - Django Export

Python3 application which exports Django models to json or yaml.

### Installation
```bash
$ pip install djexp
```

### Requirements
- Django>=2.1.5
> I am not sure if it works with earlier Django versions.
- PyYAML==3.13

### Example
##### Using as cli application:
```bash
$ djexp -r ./ -s ProjectName.settings --json
```

##### Using in Django project
Example structure:
```
ProjectName/
    ...
    manage.py
    core/
        __init__.py
        ...
        models.py
        management/
            __init__.py
            commands/
                __init__.py
                export_models.py
        views.py
        ...
    ...
```
Implement command, `export_models.py`:
```python
from ProjectName.settings import BASE_DIR
from djexpapp.task import export_django_models
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, **options):
        export_django_models(
            root=BASE_DIR,
            settings_module='ProjectName.settings',
            file_format='yml'
        )
```

Run created management command:
```bash
$ python manage.py export_models
```

### Author
* [Yuriy Lisovskiy](https://github.com/YuriyLisovskiy)

### License
The project is licensed under the terms of the [GNU General Public License v3.0](https://opensource.org/licenses/GPL-3.0), see the [LICENSE](LICENSE) file for more information.
