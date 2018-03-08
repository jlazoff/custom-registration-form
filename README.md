# Customization of Registration Form on Open Edx

## Prerequisites

Modify Country of residence to Optional by making the following modification to lms.env.conf

```
"REGISTRATION_EXTRA_FIELDS": =>  "country": "optional",
```

## Installing

1. Install with `pip install -e .` within this folder within the edx platform virtual environment.
2. Add "custom_reg_form" to the "ADDL_INSTALLED_APPS" **array** in `lms.env.json` (you may have to create it)
3. Set "REGISTRATION_EXTENSION_FORM" to "custom_reg_form.forms.ExtraInfoForm" in `lms.env.json`.
4. Run migrations. DEV Command:

```
make lms-shell
source /edx/app/edxapp/edxapp_env
cd /edx/app/edxapp/edx-platform
./manage.py lms makemigrations custom_reg_form —-settings=devstack_docker
```

5. Start/restart the LMS.
* [Docker Migration and Restart](https://github.com/edx/devstack/blob/master/README.rst) - Instructions on managing docker locally