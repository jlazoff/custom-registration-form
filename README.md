# To Use:

1. Install with `pip install -e .` within this folder within the edx platform virtual environment.
2. Add "custom_reg_form" to the "ADDL_INSTALLED_APPS" array in `lms.env.json` (you may have to create it if it doesn't exist.)
3. Set "REGISTRATION_EXTENSION_FORM" to "custom_reg_form.forms.ExtraInfoForm" in `lms.env.json`.
4. Run migrations.  
#DEV Command:  `./manage.py lms makemigrations custom_reg_form —-settings=devstack_docker`
5. Start/restart the LMS.
#Docker Migration and Restart: `https://github.com/edx/devstack/blob/master/README.rst`

# Other config requests outside the scope of this code
1.Make Country of residence optional - see lms.env.conf and modify to optional  `"REGISTRATION_EXTRA_FIELDS": =>  "country": "optional",`