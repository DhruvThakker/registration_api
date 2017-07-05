# registration_api

## Registration API version 1

The APIs in this repository, are for Open edX platform.

### Installation

* Clone the repository:

  https://github.com/DhruvThakker/registration_api.git

* Copy the API folder (registration_api) to the folder, /edx/app/edxapp/edx-platform/lms/djangoapps/

* Add the name of the app (registration_api) in the key ‘INSTALLED_APPS’ in python file /edx/app/edxapp/edx-platform/lms/envs/common.py

```python
INSTALLED_APPS = (

...

‘registration_api',

)
```

* Add the urls of the app (registration_api) to ‘url_patterns’ in python file /edx/app/edxapp/edx-platform/lms/urls.py

```python
urlpatterns = (

...

url(r’^api/courses’, include(‘registration_api.urls’)),

)
```

* Restart LMS and CMS servers by the command:
```bash
sudo /edx/bin/supervisorctl restart edxapp:
```


### [Documentation for APIs](https://github.com/DhruvThakker/registration_api/wiki)
