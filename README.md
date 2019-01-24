## djexp - Django Export

Application which exports Django models to json or yaml file format.
> Use this module on your own risk because of non-stable version.

### Installation
```bash
$ pip install djexp
```
> This module has not been deployed yet.

### Requirements
- Django>=1.7
- PyYAML==4.2b4

### Example
##### Using as command line application:
```bash
# read usage
$ djexp -h

# export models
$ djexp -r ./ -s ProjectName.settings --json
```

##### Using in Django project
Update `settings.py`:
```python
...

INSTALLED_APPS = [
    ...
    'djexp.app'
]
...
```

Run the command from `djexp` application:
```bash
$ python manage.py export_models
```

### Authors
* [Orest Hopiak](https://github.com/OHopiak)
* [Yuriy Lisovskiy](https://github.com/YuriyLisovskiy)

### License
The project is licensed under the terms of the [GNU General Public License v3.0](https://opensource.org/licenses/GPL-3.0), see the [LICENSE](LICENSE) file for more information.
