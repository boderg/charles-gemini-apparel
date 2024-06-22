# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

>[!NOTE]
>
>*HTML Validation was performed in two ways:*
>
>1. From the live site the page source was inspected, copied and pasted into the validator.
>2. From the live site the url was copied and pasted into the validator.
>
>These two methods were chosen for HTML validation due to the django content in the site being incompatible with the validator.
>
>*Pages marked with '#' had one or both of the following two warnings / errors noted and filtered out of the testing results for the following reasons:*
>
>- One filtered out warning for *'no header'* - this is because of django templating to access the dynamic page titles *{{ page_title }}*
>- One filtered out error for *'bad value for attribute action'* in the delete form - this is because of django templating to access urls - specifically *{{ delete_url }}*

<details>
<summary>Click to view the HTML validation results for Charles Gemini Apparel</summary>

| Directory | File | Screenshot Errors | Screenshot Method 1 | Screenshot Method 2 | Notes / Fixes |
| --- | --- | --- | --- | --- | --- |
| admin_panel | add_category.html | No errors to show. | ![screenshot](documentation/validation/html/add_category/add_category_pass.png) | ![screenshot](documentation/validation/html/add_category/add_category_url_pass.png) | Passed! '#' |
| admin_panel | add_colour.html | No errors to show. | ![screenshot](documentation/validation/html/add_colour/add_colour_pass.png) | ![screenshot](documentation/validation/html/add_colour/add_colour_url_pass.png) | Passed! '#' |
| admin_panel | add_garment.html | ![screenshot](documentation/validation/html/add_garment/add_garment.png) | ![screenshot](documentation/validation/html/add_garment/add_garment_pass.png) | ![screenshot](documentation/validation/html/add_garment/add_garment_url_pass.png) | *34 x 'Duplicate attribute' errors for `class="form-control"`* - this was due to the form-control class being added as an extra attribute to the form. Extra attribute was removed from forms.py to remove errors. <hr> *'Bad value `submit` for attribute type on element `a`' error* - this was due to the attribute not being removed from a link when it was converted from a button. Removed attribute `submit` from `a`. |
| admin_panel | add_size.html | No errors to show. | ![screenshot](documentation/validation/html/add_size/add_size_pass.png) | ![screenshot](documentation/validation/html/add_size/add_size_url_pass.png) | Passed! '#' |
| admin_panel | admin_panel.html | No errors to show. | ![screenshot](documentation/validation/html/admin_panel/admin_panel_pass.png) | ![screenshot](documentation/validation/html/admin_panel/admin_panel_url_pass.png) | Passed! |
| admin_panel | contact_list.html | No errors to show. | ![screenshot](documentation/validation/html/contact_list/contact_list_pass.png) | ![screenshot](documentation/validation/html/contact_list/contact_list_url_pass.png) | Passed! '#' |
| admin_panel | edit_category.html | No errors to show. | ![screenshot](documentation/validation/html/edit_category/edit_category_pass.png) | ![screenshot](documentation/validation/html/edit_category/edit_category_url_pass.png) | Passed! '#' |
| admin_panel | edit_colour.html | No errors to show. | ![screenshot](documentation/validation/html/edit_colour/edit_colour_pass.png) | ![screenshot](documentation/validation/html/edit_colour/edit_colour_url_pass.png) | Passed! '#' |
| admin_panel | edit_garment.html | No errors to show. | ![screenshot](documentation/validation/html/edit_garment/edit_garment_pass.png) | ![screenshot](documentation/validation/html/edit_garment/edit_garment_url_pass.png) | Passed! '#' |
| admin_panel | edit_size.html | No errors to show. | ![screenshot](documentation/validation/html/edit_size/edit_size_pass.png) | ![screenshot](documentation/validation/html/edit_size/edit_size_url_pass.png) | Passed! '#' |
| admin_panel | list_categories.html | No errors to show. | ![screenshot](documentation/validation/html/list_categories/list_categories_pass.png) | ![screenshot](documentation/validation/html/list_categories/list_categories_url_pass.png) | Passed!'*' |
| admin_panel | list_colours.html | No errors to show. | ![screenshot](documentation/validation/html/list_colours/list_colours_pass.png) | ![screenshot](documentation/validation/html/list_colours/list_colours_url_pass.png) | Passed!'#' |
| admin_panel | list_garments.html | ![screenshot](documentation/validation/html/list_garments/list_garments.png) | ![screenshot](documentation/validation/html/list_garments/list_garments_pass.png) | ![screenshot](documentation/validation/html/list_garments/list_garments_url_pass.png) | Passed!'#' |
| admin_panel | list_sizes.html | No errors to show. | ![screenshot](documentation/validation/html/list_sizes/list_sizes_pass.png) | ![screenshot](documentation/validation/html/list_sizes/list_sizes_url_pass.png) | Passed!'#' |
| admin_panel | newsletter_list.html | No errors to show. | ![screenshot](documentation/validation/html/newsletter_list/newsletter_list_pass.png) | ![screenshot](documentation/validation/html/newsletter_list/newsletter_list_url_pass.png) | Passed!'#' |
| apparel | all_garments.html | ![screenshot](documentation/validation/html/all_garments/all_garments.png) | ![screenshot](documentation/validation/html/all_garments/all_garments_pass.png) | ![screenshot](documentation/validation/html/all_garments/all_garments_url_pass.png) | *'Heading `h3` cannot be a child of another heading' error* - this was due to a heading tag in the page title on the base template conflicting with a heading tag in the block element on the page. Removed heading tag from base template. The following warnings and errors were all related - *2 x 'Empty heading', 'Stray end tag `h3`'.* <hr> *2 x `aria-labelldby` attribute must point to an element in the same document' error* - Re-named `aria-labelledby` attriute. |
| apparel | garment.html | ![screenshot](documentation/validation/html/garment/garment.png) | ![screenshot](documentation/validation/html/garment/garment_pass.png) | ![screenshot](documentation/validation/html/garment/garment_url_pass.png) | *2 x 'Stray start tag', 1 x 'Stray end tag' and 'Text not allowed in element `select` in this context'* - due to an icon being erroneously added to a `select` element. Removed all offending articles. <hr> *'Bad value `submit` for attribute type on element `a`' error* - this was due to an attribute not being removed from a link when it was converted from a button. Removed attribute `submit` from `a`. |
| bag | bag.html | ![screenshot](documentation/validation/html/bag/bag.png) | ![screenshot](documentation/validation/html/bag/bag_pass.png) | ![screenshot](documentation/validation/html/bag/bag_url_pass.png) | *2 x 'Trailing slash `/` on void elements has no effect and interacts badly with unquoted attribute values'* - Removed trailing slash `/`. <hr> *5 x 'Duplicate ID' and 'The first occurence of ID was here'* - this is due to the way django is set to create ID's for the select dropdown options. |
| checkout | checkout.html | ![screenshot](documentation/validation/html/checkout/checkout.png) | ![screenshot](documentation/validation/html/checkout/checkout_pass.png) | ![screenshot](documentation/validation/html/checkout/checkout_url_pass.png) | '#' and *'Empty heading'* - the empty heading is caused by the loading spinner having no text. |
| checkout | checkout_success.html | No errors to show. | ![screenshot](documentation/validation/html/checkout_success/checkout_success_pass.png) | ![screenshot](documentation/validation/html/checkout_success/checkout_success_url_pass.png) | Passed! |
| contact | contact.html | No errors to show. | ![screenshot](documentation/validation/html/contact/contact_pass.png) | ![screenshot](documentation/validation/html/contact/contact_url_pass.png) | Passed! |
| contact | contact_success.html | No errors to show. | ![screenshot](documentation/validation/html/contact_success/contact_success_pass.png) | ![screenshot](documentation/validation/html/contact_success/contact_success_url_pass.png) | Passed! |
| contact | newsletter_signup.html | No errors to show. | ![screenshot](documentation/validation/html/newsletter_signup/newsletter_signup_pass.png) | ![screenshot](documentation/validation/html/newsletter_signup/newsletter_signup_url_pass.png) | Passed! |
| contact | newsletter_success.html | No errors to show. | ![screenshot](documentation/validation/html/newsletter_success/newsletter_success_pass.png) | ![screenshot](documentation/validation/html/newsletter_success/newsletter_success_url_pass.png) | Passed! |
| home | index.html | ![screenshot](documentation/validation/html/index/index.png) | ![screenshot](documentation/validation/html/index/index_pass.png) | ![screenshot](documentation/validation/html/index/index_url_pass.png) | *'Element `h3` not allowed as child of elemet `ul` in this context'* - Added `li` element around `h3`. <hr> *'No space between attributes'* - Added a space between `image` and `alt` attributes. <hr> *2 x 'The element `button` must not appear as a descendant of the `a` element'* - Moved the link inside of the carousel to wrap the image instead of the whole carousel. <hr> *'The `type` attribute is unnecessary for JavaScript resources'* - Removed the `type` attribute. <hr> *2 x `aria-labelldby` attribute must point to an element in the same document' error* - Re-named `aria-labelledby` attriute. |
| profiles | profile.html | ![screenshot](documentation/validation/html/profile/profile.png) | ![screenshot](documentation/validation/html/profile/profile_pass.png) | ![screenshot](documentation/validation/html/profile/profile_url_pass.png) | *'Stray end tag `thead`'* - Re-located `</thead>` back to end of table head. <hr> *'The `type` attribute is unnecessary for JavaScript resources'* - Removed the type attribute. |
| all_auth | login.html | No errors to show. | ![screenshot](documentation/validation/html/login/login_pass.png) | ![screenshot](documentation/validation/html/login/login_url_pass.png) | Passed! '#' |
| all_auth | logout.html | No errors to show. | ![screenshot](documentation/validation/html/logout/logout_pass.png) | ![screenshot](documentation/validation/html/logout/logout_url_pass.png) | Passed! '#' |
| all_auth | signup.html | No errors to show. | ![screenshot](documentation/validation/html/signup/signup_pass.png) | ![screenshot](documentation/validation/html/signup/signup_url_pass.png) | Passed! '#' |

</details>

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

>[!NOTE]
>
>All files passed the CSS Jigsaw validation tests.

<details>
<summary>Click to view the CSS validation results for Charles Gemini Apparel</summary>

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| admin_panel | add_garment.css | ![screenshot](documentation/validation/css/admin_panel/add_garment.png) | Passed! |
| admin_panel | admin_panel.css | ![screenshot](documentation/validation/css/admin_panel/admin_panel.png) | Passed! |
| admin_panel | edit_garment.css | ![screenshot](documentation/validation/css/admin_panel/edit_garment.png) | Passed! |
| admin_panel | list_garments.css | ![screenshot](documentation/validation/css/admin_panel/list_garment.png) | Passed! |
| apparel | garment.css | ![screenshot](documentation/validation/css/apparel/garment.png) | Passed! |
| bag | bag.css | ![screenshot](documentation/validation/css/bag/bag.png) | Passed! |
| checkout | checkout.css | ![screenshot](documentation/validation/css/checkout/checkout.png) | Passed! |
| checkout | checkout_success.css | ![screenshot](documentation/validation/css/checkout/checkout_success.png) | Passed! |
| contact | contact.css | ![screenshot](documentation/validation/css/contact/contact.png) | Passed! |
| profiles | profile.css | ![screenshot](documentation/validation/css/profiles/profile.png) | Passed! |
| static | base.css | ![screenshot](documentation/validation/css/static/base.png) | Passed! |
| static | error_pages.css | ![screenshot](documentation/validation/css/static/error_pages.png) | Passed! |
| static | login.css | ![screenshot](documentation/validation/css/static/login.png) | Passed! |
| static | modal.css | ![screenshot](documentation/validation/css/static/modal.png) | Passed! |
| static | error.css | ![screenshot](documentation/validation/css/toasts/error.png) | Passed! |
| static | info.css | ![screenshot](documentation/validation/css/toasts/info.png) | Passed! |
| static | success.css | ![screenshot](documentation/validation/css/toasts/success.png) | Passed! |
| static | warning.css | ![screenshot](documentation/validation/css/toasts/warning.png) | Passed! |

</details>

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

>[!NOTE]
>
>All files passed the JShint validation tests.

<details>
<summary>Click to view the JavaScript validation results for Charles Gemini Apparel</summary>

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| admin_panel | delete_modal.js | ![screenshot](documentation/validation/js/delete_modal.png) | Passed! |
| checkout | stripe_elements.js | ![screenshot](documentation/validation/js/stripe_elements.png) | Passed! |
| contact | success_timer.js | ![screenshot](documentation/validation/js/success_timer.png) | Passed! |
| profiles | countryfield.js | ![screenshot](documentation/validation/js/countryfield.png) | Passed! |
| static | quantity.js | ![screenshot](documentation/validation/js/quantity.png) | Passed! |

</details>

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

>[!NOTE]
>
>All files passed the PEP8 CI Python Linter validation tests.

<details>
<summary>Click to view the Python validation results for Charles Gemini Apparel</summary>

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| admin_panel | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/admin_panel/admin.py) | *File not used* | *Nothing to note* |
| admin_panel | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/admin_panel/forms.py) | ![screenshot](documentation/validation/python/admin_panel/forms.png) | Passed! |
| admin_panel | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/admin_panel/models.py) | *File not used* | *Nothing to note* |
| admin_panel | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/admin_panel/urls.py) | ![screenshot](documentation/validation/python/admin_panel/urls.png) | Passed! |
| admin_panel | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/admin_panel/views.py) | ![screenshot](documentation/validation/python/admin_panel/views.png) | Passed! |
| apparel | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/apparel/admin.py) | ![screenshot](documentation/validation/python/apparel/admin.png) | Passed! |
| apparel | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/apparel/forms.py) | ![screenshot](documentation/validation/python/apparel/forms.png) | Passed! |
| apparel | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/apparel/models.py) | ![screenshot](documentation/validation/python/apparel/models.png) | Passed! |
| apparel | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/apparel/urls.py) | ![screenshot](documentation/validation/python/apparel/urls.png) | Passed! |
| apparel | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/apparel/views.py) | ![screenshot](documentation/validation/python/apparel/views.png) | Passed! |
| bag | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/bag/admin.py) | *File not used* | *Nothing to note* |
| bag | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/bag/contexts.py) | ![screenshot](documentation/validation/python/bag/contexts.png) | Passed! |
| bag | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/bag/models.py) | *File not used* | *Nothing to note* |
| bag | bag_tools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/validation/python/bag/bag_tools.png) | Passed! |
| bag | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/bag/urls.py) | ![screenshot](documentation/validation/python/bag/urls.png) | Passed! |
| bag | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/bag/views.py) | ![screenshot](documentation/validation/python/bag/views.png) | Passed! |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/checkout/admin.py) | ![screenshot](documentation/validation/python/checkout/admin.png) | Passed! |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/checkout/forms.py) | ![screenshot](documentation/validation/python/checkout/forms.png) | Passed! |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/checkout/models.py) | ![screenshot](documentation/validation/python/checkout/models.png) | Passed! |
| checkout | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/checkout/signals.py) | ![screenshot](documentation/validation/python/checkout/signals.png) | Passed! |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/checkout/urls.py) | ![screenshot](documentation/validation/python/checkout/urls.png) | Passed! |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/checkout/views.py) | ![screenshot](documentation/validation/python/checkout/views.png) | Passed! |
| checkout | webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/checkout/webhook_handler.py) | ![screenshot](documentation/validation/python/checkout/webhook_handler.png) | Passed! |
| checkout | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/checkout/webhooks.py) | ![screenshot](documentation/validation/python/checkout/webhooks.png) | Passed! |
| contact | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/contact/admin.py) | ![screenshot](documentation/validation/python/contact/admin.png) | Passed! |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/contact/forms.py) | ![screenshot](documentation/validation/python/contact/forms.png) | Passed! |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/contact/models.py) | ![screenshot](documentation/validation/python/contact/models.png) | Passed! |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/contact/urls.py) | ![screenshot](documentation/validation/python/contact/urls.png) | Passed! |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/contact/views.py) | ![screenshot](documentation/validation/python/contact/views.png) | Passed! |
|  | custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/custom_storages.py) | ![screenshot](documentation/validation/python/custom_storages.png) | Passed! |
| home | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/home/admin.py) | *File not used* | *Nothing to Note* |
| home | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/home/models.py) | *File not used* | *Nothing to Note* |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/home/urls.py) | ![screenshot](documentation/validation/python/home/urls.png) | Passed! |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/home/views.py) | ![screenshot](documentation/validation/python/home/views.png) | Passed! |
| main | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/main/settings.py) | ![screenshot](documentation/validation/python/main/settings.png) | Passed! |
| main | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/main/urls.py) | ![screenshot](documentation/validation/python/main/urls.png) | Passed! |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/manage.py) | ![screenshot](documentation/validation/python/manage.png) | Passed! |
| profiles | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/profiles/admin.py) | *File not used* | *Nothing to note* |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/profiles/forms.py) | ![screenshot](documentation/validation/python/profiles/forms.png) | Passed! |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/profiles/models.py) | ![screenshot](documentation/validation/python/profiles/models.png) | Passed! |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/profiles/urls.py) | ![screenshot](documentation/validation/python/profiles/urls.png) | Passed! |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/boderg/charles-gemini-apparel/main/profiles/views.py) | ![screenshot](documentation/validation/python/profiles/views.png) | Passed! |

</details>

## Browser Compatibility

I've tested my deployed project on the following three browsers to check for compatibility issues:

- Chrome
- Firefox
- Safari

I decided to use these three browsers as they use different platforms independant of each other.

> [!NOTE]
>
>Charles Gemini Apparel behaved as expected on all browsers tested.

<details>
<summary>Click to view the Browser compatibility testing results for Charles Gemini Apparel</summary>

| Page | Chrome | Firefox | Safari |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/browsers/chrome/home.png) | ![screenshot](documentation/browsers/firefox/home.png) | ![screenshot](documentation/browsers/safari/home.png) |
| All Designs | ![screenshot](documentation/browsers/chrome/all_designs.png) | ![screenshot](documentation/browsers/firefox/all_designs.png) | ![screenshot](documentation/browsers/safari/all_designs.png) |
| Garment | ![screenshot](documentation/browsers/chrome/garment.png) | ![screenshot](documentation/browsers/firefox/garment.png) | ![screenshot](documentation/browsers/safari/garment.png) |
| Bag | ![screenshot](documentation/browsers/chrome/bag.png) | ![screenshot](documentation/browsers/firefox/bag.png) | ![screenshot](documentation/browsers/safari/bag.png) |
| Checkout | ![screenshot](documentation/browsers/chrome/checkout.png) | ![screenshot](documentation/browsers/firefox/checkout.png) | ![screenshot](documentation/browsers/safari/checkout.png) |
| Checkout Success | ![screenshot](documentation/browsers/chrome/checkout_success.png) | ![screenshot](documentation/browsers/firefox/checkout_success.png) | ![screenshot](documentation/browsers/safari/checkout_success.png) |
| Profile | ![screenshot](documentation/browsers/chrome/profile.png) | ![screenshot](documentation/browsers/firefox/profile.png) | ![screenshot](documentation/browsers/safari/profile.png) |
| Admin Panel | ![screenshot](documentation/browsers/chrome/admin_panel.png) | ![screenshot](documentation/browsers/firefox/admin_panel.png) | ![screenshot](documentation/browsers/safari/admin_panel.png) |
| Add, List, Edit Garment | ![screenshot](documentation/browsers/chrome/add_garment.png) | ![screenshot](documentation/browsers/firefox/list_garment.png) | ![screenshot](documentation/browsers/safari/edit_garment.png) |
| Add, List, Edit Colour | ![screenshot](documentation/browsers/chrome/add_colour.png) | ![screenshot](documentation/browsers/firefox/list_colour.png) | ![screenshot](documentation/browsers/safari/edit_colour.png) |
| Add, List, Edit Size | ![screenshot](documentation/browsers/chrome/add_size.png) | ![screenshot](documentation/browsers/firefox/list_size.png) | ![screenshot](documentation/browsers/safari/edit_size.png) |
| Add, List, Edit Category | ![screenshot](documentation/browsers/chrome/add_category.png) | ![screenshot](documentation/browsers/firefox/list_category.png) | ![screenshot](documentation/browsers/safari/edit_category.png) |
| Contact, Contact List, Contact Success | ![screenshot](documentation/browsers/chrome/contact.png) | ![screenshot](documentation/browsers/firefox/contact_list.png) | ![screenshot](documentation/browsers/safari/contact_success.png) |
| Newsletter Signup, Newsletter List, Newsletter Success | ![screenshot](documentation/browsers/chrome/newsletter_signup.png) | ![screenshot](documentation/browsers/firefox/newsletter_list.png) | ![screenshot](documentation/browsers/safari/newsletter_success.png) |
| About, Size Guide, Delete Modals | ![screenshot](documentation/browsers/chrome/about_modal.png) | ![screenshot](documentation/browsers/firefox/size_guide_modal.png) | ![screenshot](documentation/browsers/safari/delete_modal.png) |
| Login, Logout, Signup | ![screenshot](documentation/browsers/chrome/login.png) | ![screenshot](documentation/browsers/firefox/logout.png) | ![screenshot](documentation/browsers/safari/signup.png) |

</details>

## Responsiveness

I've tested the Charles Gemini Apparel deployed project on multiple devices to check for responsiveness issues.

> [!NOTE]
>
>Charles Gemini Apparel behaved as expected on all responsive tests.

<details>
<summary>Click to view the Responsiveness testing results for Charles Gemini Apparel</summary>

| Page | Mobile (DevTools) | Tablet (DevTools) | 1080p Laptop | 1080p Monitor | 1440p UW Monitor | Samsung Galaxy S10+ |
| --- | --- | --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/responsive/mobile_(dev_tools)/home.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/home.png) | ![screenshot](documentation/responsive/1080p_laptop/home.png) | ![screenshot](documentation/responsive/1080p_monitor/home.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/home.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/home.jpg) |
| All Designs | ![screenshot](documentation/responsive/mobile_(dev_tools)/all_designs.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/all_designs.png) | ![screenshot](documentation/responsive/1080p_laptop/all_designs.png) | ![screenshot](documentation/responsive/1080p_monitor/all_designs.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/all_designs.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/all_designs.jpg) |
| Garment | ![screenshot](documentation/responsive/mobile_(dev_tools)/garment.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/garment.png) | ![screenshot](documentation/responsive/1080p_laptop/garment.png) | ![screenshot](documentation/responsive/1080p_monitor/garment.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/garment.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/garment.jpg) |
| Bag | ![screenshot](documentation/responsive/mobile_(dev_tools)/bag.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/bag.png) | ![screenshot](documentation/responsive/1080p_laptop/bag.png) | ![screenshot](documentation/responsive/1080p_monitor/bag.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/bag.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/bag.jpg) |
| Checkout | ![screenshot](documentation/responsive/mobile_(dev_tools)/checkout.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/checkout.png) | ![screenshot](documentation/responsive/1080p_laptop/checkout.png) | ![screenshot](documentation/responsive/1080p_monitor/checkout.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/checkout.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/checkout.jpg) |
| Checkout Success | ![screenshot](documentation/responsive/mobile_(dev_tools)/checkout_success.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/checkout_success.png) | ![screenshot](documentation/responsive/1080p_laptop/checkout_success.png) | ![screenshot](documentation/responsive/1080p_monitor/checkout_success.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/checkout_success.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/checkout_success.jpg) |
| Profile | ![screenshot](documentation/responsive/mobile_(dev_tools)/profile.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/profile.png) | ![screenshot](documentation/responsive/1080p_laptop/profile.png) | ![screenshot](documentation/responsive/1080p_monitor/profile.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/profile.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/profile.jpg) |
| Admin Panel | ![screenshot](documentation/responsive/mobile_(dev_tools)/admin_panel.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/admin_panel.png) | ![screenshot](documentation/responsive/1080p_laptop/admin_panel.png) | ![screenshot](documentation/responsive/1080p_monitor/admin_panel.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/admin_panel.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/admin_panel.jpg) |
| Add, List, Edit Garment | ![screenshot](documentation/responsive/mobile_(dev_tools)/add_garment.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/list_garments.png) | ![screenshot](documentation/responsive/1080p_laptop/edit_garment.png) | ![screenshot](documentation/responsive/1080p_monitor/add_garment.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/list_garments.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/edit_garment.jpg) |
| Add, List, Edit Colour | ![screenshot](documentation/responsive/mobile_(dev_tools)/add_colour.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/list_colours.png) | ![screenshot](documentation/responsive/1080p_laptop/edit_colour.png) | ![screenshot](documentation/responsive/1080p_monitor/add_colour.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/list_colours.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/edit_colour.jpg) |
| Add, List, Edit Size | ![screenshot](documentation/responsive/mobile_(dev_tools)/add_size.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/list_sizes.png) | ![screenshot](documentation/responsive/1080p_laptop/edit_size.png) | ![screenshot](documentation/responsive/1080p_monitor/add_size.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/list_sizes.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/edit_size.jpg) |
| Add, List, Edit Category | ![screenshot](documentation/responsive/mobile_(dev_tools)/add_category.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/list_categories.png) | ![screenshot](documentation/responsive/1080p_laptop/edit_category.png) | ![screenshot](documentation/responsive/1080p_monitor/add_category.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/list_categories.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/edit_category.jpg) |
| Contact, Contact List, Contact Success | ![screenshot](documentation/responsive/mobile_(dev_tools)/contact.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/contact_list.png) | ![screenshot](documentation/responsive/1080p_laptop/contact_success.png) | ![screenshot](documentation/responsive/1080p_monitor/contact.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/contact_list.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/contact_success.jpg) |
| Newsletter, Newsletter List, Newsletter Success | ![screenshot](documentation/responsive/mobile_(dev_tools)/newsletter_signup.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/newsletter_list.png) | ![screenshot](documentation/responsive/1080p_laptop/newsletter_success.png) | ![screenshot](documentation/responsive/1080p_monitor/newsletter_signup.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/newsletter_list.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/newsletter_success.jpg) |
| About, Size Guide, Delete Modals | ![screenshot](documentation/responsive/mobile_(dev_tools)/about_modal.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/size_guide_modal.png) | ![screenshot](documentation/responsive/1080p_laptop/delete_modal.png) | ![screenshot](documentation/responsive/1080p_monitor/about_modal.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/size_guide_modal.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/delete_modal.jpg) |
| Login, Logout, Signup | ![screenshot](documentation/responsive/mobile_(dev_tools)/login.png) | ![screenshot](documentation/responsive/tablet_(dev_tools)/logout.png) | ![screenshot](documentation/responsive/1080p_laptop/signup.png) | ![screenshot](documentation/responsive/1080p_monitor/login.png) | ![screenshot](documentation/responsive/1440p_ultra_wide_monitor/logout.png) | ![screenshot](documentation/responsive/samsung_galaxy_s10_plus/signup.jpg) |

</details>
