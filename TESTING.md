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
>- One filtered out warning for *'no Top Nav Bar'* - this is because of django templating to access the dynamic page titles *{{ page_title }}*
>- One filtered out error for *'bad value for attribute action'* in the delete form - this is because of django templating to access urls - specifically *{{ delete_url }}*

<details>
<summary>Click to view the HTML validation results for Charles Gemini Apparel</summary>
<br>

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
<br>

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
<br>

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
<br>

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

- [Chrome](https://www.google.com/chrome)
- [Firefox](https://www.mozilla.org/en-GB/firefox/new/)
- [Safari](https://www.apple.com/uk/safari/)

I decided to use these three browsers as they use different platforms independant of each other.

> [!NOTE]
>
>Charles Gemini Apparel behaved as expected on all browsers tested.

<details>
<summary>Click to view the Browser compatibility testing results for Charles Gemini Apparel</summary>
<br>

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
<br>

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

## Lighthouse Audit

I've tested the Charles Gemini Apparel deployed project using the [Lighthouse Audit tool](https://developer.chrome.com/docs/lighthouse/overview) to check for any major issues.

>[!NOTE]
>
>*General notes for lighthouse audit results*
>
>- Mobile results have a significant drop in performance over desktop results.
>- The highest drops in performance on desktop appear to be in relation to the number of garment images on each page.
>- These drops in performace could potentially be the result of a combination of image size and fetch time from the AWS S3 storage. 
>- All garment images have been saved in webp format but could potentially be shrunk to smaller sizes to aid storage capacities and fetch times.
>- Accessibility could be improved in some areas.
>- Best practices and SEO are the same across the site with SEO needing some improvement.

<details>
<summary>Click to view the Lighthouse Audit test results for Charles Gemini Apparel</summary>
<br>

| Page | Mobile | Desktop |
| --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/desktop/home.png) | ![screenshot](documentation/lighthouse/mobile/home.png) |
| All Designs | ![screenshot](documentation/lighthouse/desktop/all_designs.png) | ![screenshot](documentation/lighthouse/mobile/all_designs.png) |
| New Designs | ![screenshot](documentation/lighthouse/desktop/new_designs.png) | ![screenshot](documentation/lighthouse/mobile/new_designs.png) |
| Tees | ![screenshot](documentation/lighthouse/desktop/tees.png) | ![screenshot](documentation/lighthouse/mobile/tees.png) |
| Hoodies | ![screenshot](documentation/lighthouse/desktop/hoodies.png) | ![screenshot](documentation/lighthouse/mobile/hoodies.png) |
| Garment | ![screenshot](documentation/lighthouse/desktop/garment.png) | ![screenshot](documentation/lighthouse/mobile/garment.png) |
| Bag | ![screenshot](documentation/lighthouse/desktop/bag.png) | ![screenshot](documentation/lighthouse/mobile/bag.png) |
| Checkout | ![screenshot](documentation/lighthouse/desktop/checkout.png) | ![screenshot](documentation/lighthouse/mobile/checkout.png) |
| Checkout Success | ![screenshot](documentation/lighthouse/desktop/checkout_success.png) | ![screenshot](documentation/lighthouse/mobile/checkout_success.png) |
| Profile | ![screenshot](documentation/lighthouse/desktop/profile.png) | ![screenshot](documentation/lighthouse/mobile/profile.png) |
| Admin Panel | ![screenshot](documentation/lighthouse/desktop/admin_panel.png) | ![screenshot](documentation/lighthouse/mobile/admin_panel.png) |
| Add Garment | ![screenshot](documentation/lighthouse/desktop/add_garment.png) | ![screenshot](documentation/lighthouse/mobile/add_garment.png) |
| List Garment | ![screenshot](documentation/lighthouse/desktop/list_garment.png) | ![screenshot](documentation/lighthouse/mobile/list_garment.png) |
| Edit Garment | ![screenshot](documentation/lighthouse/desktop/edit_garment.png) | ![screenshot](documentation/lighthouse/mobile/edit_garment.png) |
| Add Colour | ![screenshot](documentation/lighthouse/desktop/add_colour.png) | ![screenshot](documentation/lighthouse/mobile/add_colour.png) |
| List Colour | ![screenshot](documentation/lighthouse/desktop/list_colour.png) | ![screenshot](documentation/lighthouse/mobile/list_colour.png) |
| Edit Colour | ![screenshot](documentation/lighthouse/desktop/edit_colour.png) | ![screenshot](documentation/lighthouse/mobile/edit_colour.png) |
| Add Size | ![screenshot](documentation/lighthouse/desktop/add_size.png) | ![screenshot](documentation/lighthouse/mobile/add_size.png) |
| List Size | ![screenshot](documentation/lighthouse/desktop/list_size.png) | ![screenshot](documentation/lighthouse/mobile/list_size.png) |
| Edit Size | ![screenshot](documentation/lighthouse/desktop/edit_size.png) | ![screenshot](documentation/lighthouse/mobile/edit_size.png) |
| Add Category | ![screenshot](documentation/lighthouse/desktop/add_category.png) | ![screenshot](documentation/lighthouse/mobile/add_category.png) |
| List Category | ![screenshot](documentation/lighthouse/desktop/list_category.png) | ![screenshot](documentation/lighthouse/mobile/list_category.png) |
| Edit Category | ![screenshot](documentation/lighthouse/desktop/edit_category.png) | ![screenshot](documentation/lighthouse/mobile/edit_category.png) |
| Contact | ![screenshot](documentation/lighthouse/desktop/contact.png) | ![screenshot](documentation/lighthouse/mobile/contact.png) |
| Contact List | ![screenshot](documentation/lighthouse/desktop/contact_list.png) | ![screenshot](documentation/lighthouse/mobile/contact_list.png) |
| Newsletter | ![screenshot](documentation/lighthouse/desktop/newsletter.png) | ![screenshot](documentation/lighthouse/mobile/newsletter.png) |
| Newsletter List | ![screenshot](documentation/lighthouse/desktop/newsletter_list.png) | ![screenshot](documentation/lighthouse/mobile/newsletter_list.png) |

</details>

## Wave Compatibility

The Charles Gemini Apparel deployed site was tested using the [Wave Compatibility tester](https://wave.webaim.org/), however the Wave tester could only test pages that were not signed into as it does not have access to secured pages.
The following results are from the non secured pages of the site.

>[!NOTE]
>
>The errors noted by the tester are due to django templating.

<details>
<summary>Click to view the Wave accesibility test results for Charles Gemini Apparel</summary>
<br>

| Page | Summary Screenshot | Contrast Screenshot |
| --- | --- | --- |
| Home | ![screenshot](documentation/wave/home_summary.png) | ![screenshot](documentation/wave/home_contrast.png) |
| All Designs | ![screenshot](documentation/wave/all_designs_summary.png) | ![screenshot](documentation/wave/all_designs_contrast.png) |
| New Designs | ![screenshot](documentation/wave/new_designs_summary.png) | ![screenshot](documentation/wave/new_designs_contrast.png) |
| Tees | ![screenshot](documentation/wave/tees_summary.png) | ![screenshot](documentation/wave/tees_contrast.png) |
| Hoodies | ![screenshot](documentation/wave/hoodies_summary.png) | ![screenshot](documentation/wave/hoodies_contrast.png) |
| Garment | ![screenshot](documentation/wave/garment_summary.png) | ![screenshot](documentation/wave/garment_contrast.png) |
| Bag | ![screenshot](documentation/wave/bag_summary.png) | ![screenshot](documentation/wave/bag_contrast.png) |
| Contact | ![screenshot](documentation/wave/contact_summary.png) | ![screenshot](documentation/wave/contact_contrast.png) |
| Newsletter | ![screenshot](documentation/wave/newsletter_summary.png) | ![screenshot](documentation/wave/newsletter_contrast.png) |

</details>

## Defensive Programming

Defensive programming was manually tested for Charles Gemini Apparel with the below user acceptance testing:

<details>
<summary>Click to view the user acceptance test results for Charles Gemini Apparel</summary>
<br>

| Page | Section | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- | --- |
| Home | | | | | | |
| | Top Nav Bar | The *Charles Gemini Logo* is expected to act as a home button when clicked and return the user to the *Home* page. | Tested the feature by navigating away from the home page and clicking the *Charles Gemini Logo*. | The feature behaved as expected, and retuned the user to the *Home* page. | Test concluded and passed. | ![screenshot](documentation/features/charles_gemini_logo.png) |
| | Top Nav Bar | The *Shop Now!* button is expected to open a dropdown with navigation links to the site. | Tested the feature by clicking on the *Shop Now!* button and selecting each of the navigation links in the dropdown in turn. | The feature behaved as expected, and opened a dropdown with the site navigation links. Each link clicked opened the corresponding page or modal. | Test concluded and passed. | ![screenshot](documentation/features/shop_now_button.png) ![screenshot](documentation/features/shop_now_dropdown_highlighted.png) |
| | Top Nav Bar | The *Search box and button* is expected to accept a criteria of terms based on the garment details and category names to search the site and return results based on that criteria. | Tested the feature by entering keywords and clicking the *Search box and button*. | The feature behaved as expected, and return results based on the search criteria or returns an error message informing the user that no garment was found. | Test concluded and passed. | ![screenshot](documentation/features/search_bar.png) |
| | Bottom Nav Bar | The *Bag* button is expected to open the shopping bag page and display an item counter if any items are in the bag. | Tested the feature by clicking the *Bag* button when no items were in the bag and also by putting an item in the bag and clicking on the *Bag* button. | The feature behaved as expected, and returned the empty shopping bag page when no items were in the bag and returned the shopping bag with items when items were in the bag along with an item counter in the *Bag* button. | Test concluded and passed. | ![screenshot](documentation/features/bag_button.png) ![screenshot](documentation/features/bag_counter.png) |
| | Bottom Nav Bar | The *Login / Logout* button is expected to open the *Login or Logout* page and change state to a *Login or Logout* button dependant on the users login status. | Tested the feature by clicking the *Login / Logout* button and logging in and out of the site. | The feature behaved as expected, and change state dependant on login status. | Test concluded and passed. | ![screenshot](documentation/features/login_button.png) ![screenshot](documentation/features/logout_button.png) |
| | Main Body | The *Page links* are expected to open the associated page when the user clixks on the image.  | Test the feature by clicking on the links in turn. | The feature behaved as expected, and open the associated page connected with that link. | Tes cocluded and passed. | ![screenshot](documentation/features/page_links.png) |
| | Main Body | The home page *Carousel* is expected to display a rotation of different images that can be stopped and manually rotated if required. | Tested the feature by hovering the mouse on the *Carousel* and by clicking the *Carousel Next and Previous* buttons. | The feature behaved as expected, and the *Carousel* stopped when the mouse was hovered on the images. The images were also able to be rotated manually using the *Carousel Next and Previous* buttons.  | Test concluded and passed. | ![screenshot](documentation/features/carousel.png) |
| | Footer | The *Newsletter Signup* button is expected to open a page where the user can input and submit their email address to a mailing list. | Tested the feature by clicking on the *Newsletter Signup* button. | The feature behaved as expected, and opened the newsletter signup page. | Test concluded and passed.| ![screenshot](documentation/features/newsletter_signup_button.png) |
| | Footer | The *Admin Panel* button is expected to open a page where the site *Administrator / Superuser* can administer various aspects of the site without having to log in to the backend server side. the button is also expected to be only visible when the superuser is logged in to the site. | Tested the feature by clicking on the *Admin Panel* button while logged in as the superuser. | The feature behaved as expected, and opened the Admin Panel page page. | Test concluded and passed.| ![screenshot](documentation/features/admin_panel_button.png) |
| | Footer | The *GitHub* icon is expected to act as a button that opens the site creators *GitHub* profile in a new browser tab. | Tested the feature by clicking on the *GitHub* icon. | The feature behaved as expected, and opened the site creators *GitHub* profile in a new browser tab. | Test concluded and passed. | ![screenshot](documentation/features/github_icons.png) |
| | Footer | The *Social Media* icons are expected to act as buttons that open the associated social media site in a new browser tab. | Tested the feature by clicking on the *Social Media* icons in turn. | The feature behaved as expected, and opened the associated social media pages in new browser tabs. | Test concluded and passed. | ![screenshot](documentation/features/social_icons.png) |
| All Designs, New Designs, Tees and Hoodies | | | | | | |
| | Garment Cards | The *Garment* images are expected to to act as buttons / links to open the page associated with the garment that is clicked. | Tested the feature by clicking on each *Garment* image in turn. | The feature behaved as expected, and opened the associated garment page. | Test concluded and passed. | ![screenshot](documentation/features/garment_images.png) |
| Garment | | | | | | |
| | Garment Card | The garment page *Carousel* is expected to display a rotation of the same image in different colours that can be stopped and manually rotated if required. | Tested the feature by hovering the mouse on the *Carousel* and by clicking the *Carousel Next and Previous* buttons. | The feature behaved as expected, and the *Carousel* stopped when the mouse was hovered on the images. The images were also able to be rotated manually using the *Carousel Next and Previous* buttons.  | Test concluded and passed. | ![screenshot](documentation/features/carousel.png) |
| | Garment Card | The *Number Selector* is expected to increment or decrement the number of items that the user wants to add to the bag. It is also expected to not exceed the range of 1-99 inclusive. | Tested the feature by selecting different quantities and adding the item to the bag. Quantites outside the range were also tested by manual entry. | The feature behaved as expected, and incremented or decremented the quantity as desired and did not allow numbers outside the range to be used. | Test concluded and passed. | ![screenshot](documentation/features/number_selector.png) |
| | Garment Card | The *Size Selector* dropdown is expected to open a dropdown selection of sizes that the user can select for the garment. | Tested the feature by clicking the *Size Selector* button and selecting a size then adding the item to the bag. | The feature behaved as expected, and the size selected was added to the bag with the item and quantity. | Test concluded and passed. | ![screenshot](documentation/features/size_selector.png) |
| | Garment Card | The *Colour Selector* dropdown is expected to open a dropdown selection of colours that the user can select for the garment. | Tested the feature by clicking the *Colour Selector* button and selecting a colour then adding the item to the bag. | The feature behaved as expected, and the colour selected was added to the bag with the item and quantity. | Test concluded and passed. | ![screenshot](documentation/features/colour_selector.png) |
| | Garment Card | The *Size Guide* button is expected to open the size guide modal. | Tested the feature by clicking the *Size Guide* button. | The feature behaved as expected, and opened the size guide modal. | Test concluded and passed. | ![screenshot](documentation/features/size_guide_button.png) |
| | Garment Card | The *Add to bag* button is expected to add the selected item and put it in the shopping bag then redirect the user to the all designs page. | Tested the feature by clicking the *Add to bag* button. | The feature behaved as expected, and added the selected item to the bag then redirected the user to the all designs page. | Test concluded and passed. | ![screenshot](documentation/features/add_to_bag_button.png) |
| | Garment Card | The *All Designs* button is expected to open the all designs page without saving the selected item. | Tested the feature by clicking the *All Designs* button. | The feature behaved as expected, and opened the all designs page without saving the item selection. | Test concluded and passed. | ![screenshot](documentation/features/all_designs.png) |
| Shopping Bag | | | | | | |
| | Bag Table | The *Size Selector* dropdown is expected to open a dropdown selection of sizes that the user can select for the garment. | Tested the feature by clicking the *Size Selector* button and selecting a size then adding the item to the bag. | The feature behaved as expected, and the size selected was added to the bag with the item and quantity. | Test concluded and passed. | ![screenshot](documentation/features/size_selector1.png) |
| | Bag Table | The *Colour Selector* dropdown is expected to open a dropdown selection of colours that the user can select for the garment. | Tested the feature by clicking the *Colour Selector* button and selecting a colour then adding the item to the bag. | The feature behaved as expected, and the colour selected was added to the bag with the item and quantity. | Test concluded and passed. | ![screenshot](documentation/features/colour_selector1.png) |
| | Bag Table | The *Number Selector* is expected to increment or decrement the number of items that the user wants to add to the bag. It is also expected to not exceed the range of 1-99 inclusive. | Tested the feature by selecting different quantities and adding the item to the bag. Quantites outside the range were also tested by manual entry. | The feature behaved as expected, and incremented or decremented the quantity as desired and did not allow numbers outside the range to be used. | Test concluded and passed. | ![screenshot](documentation/features/number_selector1.png) |
| | Bag Table | The *Update* button is expected to update the selected item in the bag after the user has changed their size, colour and quantity selections. | Tested the feature by clicking the *Update* button. | The feature behaved as expected, and updated the item in the bag and reflected the updates in the adjusted shopping bag price structure. | Test concluded and passed. | ![screenshot](documentation/features/update_button.png) |
| | Bag Table | The *Remove* button is expected to remove the selected item fromthe shopping bag. | Tested the feature by clicking the *Remove* button. | The feature behaved as expected, and removed the item selection from the shopping bag and redirected the user to the empty bag page if no other items were present in the bag. | Test concluded and passed. | ![screenshot](documentation/features/remove_button.png) |
| | Bag Table | The *Continue Shopping* button is expected to return the user to the all designs page while saving the items already in the shopping bag. | Tested the feature by clicking the *Continue Shopping* button. | The feature behaved as expected, and returned the user to the all designs page saving the items already in the shopping bag. | Test concluded and passed. | ![screenshot](documentation/features/continue_shopping.png) |
| | Bag Table | The *Secure Checkout* button is expected to add the items of the bag to the checkout and open the checkout page so the user can purchase the items. | Tested the feature by clicking the *Secure Checkout* button. | The feature behaved as expected, and opened the checkout page with all the selected items that were added to the bag. | Test concluded and passed. | ![screenshot](documentation/features/secure_checkout.png) |
| Checkout | | | | | | |
| | Order Summary | The *Change Your Order* button is expected to return the user to the shopping bag so they can edit their order. | Tested the feature by clicking the *Change Your Order* button. | The feature behaved as expected, and returned the user to the shopping bag. | Test concluded and passed. | ![screenshot](documentation/features/change_your_order_button.png) |
| | Checkout Form | The *Checkout Form* is expected to store the details of the user for order and payment processing. | Tested the feature by entering details and completing a test sale and checking the *Stripe* dashboard and the order database. | The feature behaved as expected, and and stored the user details for the sale passing them to *Stripe and the order database. | Test concluded and passed. | ![screenshot](documentation/features/checkout_form.png) |
| | Checkout Form | The *Save Info* checkbox is expected to save the details of the logged in user to their profile for future use. | Tested the feature by entering details and completing a test sale with the checkbox enabled while logged into the site. | The feature behaved as expected, and stored the user details to their profile for future. | Test concluded and passed. | ![screenshot](documentation/features/save_info.png) |
| | Checkout Form | The *Create Account* link is expected to open the signup page to create a user profile when no user is logged in. | Tested the feature by clicking the link. | The feature behaved as expected, and opened the signup page. | Test concluded and passed. | ![screenshot](documentation/features/create_account_link.png) |
| | Checkout Form | The *Login* link is expected to open the login page to allow a previous user to log in without creating new account details. | Tested the feature by clicking the link. | The feature behaved as expected, and opened the login page. | Test concluded and passed. | ![screenshot](documentation/features/login_link.png) |
| | Checkout Form | The *Card Payment* input is expected to temporarily store the users card details for payment processing. | Tested the feature by entering test card details and processing a sale. | The feature behaved as expected, and temporarily stored the test card details before passing them to *Stripe for payment processing. | Test concluded and passed. | ![screenshot](documentation/features/card_details.png) |
| | Checkout Form | The *Complete Order* button is expected to process the order and pass payment details to *Stripe*. | Tested the feature by clicking the *Complete Order* button. | The feature behaved as expected, and processed the order saving the order details to the database (and user profile if logged in), passing the card details to *Stripe*, sending a confirmation email to the user and passing the user to an checkout success page displaying an order summary. | Test concluded and passed. | ![screenshot](documentation/features/complete_order_button.png) |
| Checkout Success | | | | | | |
| | Order Summary | The *Continue Shopping* button is expected to return the user to the all designs page while saving the items already in the shopping bag. | Tested the feature by clicking the *Continue Shopping* button. | The feature behaved as expected, and returned the user to the all designs page saving the items already in the shopping bag. | Test concluded and passed. | ![screenshot](documentation/features/continue_shopping1.png) |
| Admin Panel | | | | | | |
| | Add Garment | The *Add Garment* button is expected to open the *Add Garment* page.| Tested the feature by clicking the *Add Garment* button. | The feature behaved as expected, and opened the *Add Garment* page. | Test concluded and passed. | ![screenshot](documentation/features/add_garment.png) |
| | Edit Garment | The *Edit Garment* button is expected to open the *Garment Selection* page.| Tested the feature by clicking the *Edit Garment* button. | The feature behaved as expected, and opened the *Garment Selection* page. | Test concluded and passed. | ![screenshot](documentation/features/edit_garment.png) |
| | Add Category | The *Add Category* button is expected to open the *Add Category* page.| Tested the feature by clicking the *Add Category* button. | The feature behaved as expected, and opened the *Add Category* page. | Test concluded and passed. | ![screenshot](documentation/features/add_category.png) |
| | Edit Category | The *Edit Category* button is expected to open the *Category Selection* page.| Tested the feature by clicking the *Edit Category* button. | The feature behaved as expected, and opened the *Category Selection* page. | Test concluded and passed. | ![screenshot](documentation/features/edit_category.png) |
| | Add Colour | The *Add Colour* button is expected to open the *Add Colour* page.| Tested the feature by clicking the *Add Colour* button. | The feature behaved as expected, and opened the *Add Colour* page. | Test concluded and passed. | ![screenshot](documentation/features/add_colour.png) |
| | Edit Colour | The *Edit Colour* button is expected to open the *Colour Selection* page.| Tested the feature by clicking the *Edit Colour* button. | The feature behaved as expected, and opened the *Colour Selection* page. | Test concluded and passed. | ![screenshot](documentation/features/edit_colour.png) |
| | Add Size | The *Add Size* button is expected to open the *Add Size* page.| Tested the feature by clicking the *Add Size* button. | The feature behaved as expected, and opened the *Add Size* page. | Test concluded and passed. | ![screenshot](documentation/features/add_size.png) |
| | Edit Size | The *Edit Size* button is expected to open the *Size Selection* page.| Tested the feature by clicking the *Edit Size* button. | The feature behaved as expected, and opened the *Size Selection* page. | Test concluded and passed. | ![screenshot](documentation/features/edit_size.png) |
| | Contact List | The *Contact List* button is expected to open the *Contact List* page.| Tested the feature by clicking the *Contact List* button. | The feature behaved as expected, and opened the *Contact List* page. | Test concluded and passed. | ![screenshot](documentation/features/contact_list.png) |
| | Subscribers | The *Newsletter Subscribers* button is expected to open the *Newsletter Subscribers* page.| Tested the feature by clicking the *Subscribers* button. | The feature behaved as expected, and opened the *Newsletter Subscribers* page. | Test concluded and passed. | ![screenshot](documentation/features/subscribers.png) |
| Add Garment and Edit Garment | | | | | | |
|  | Add and Edit Garment Forms | The *Add and Edit Garment* forms are expected to allow the admin of the site to add or edit a garment respectively by utilising the inputs and checkboxes in the forms. | Tested the features by completing the form of each and clicking the *Add or Edit Garment* button at the bottom of the form. | The *Add and Edit* Garment forms behaved as expected, and either added a new garment or edited an exisiting garment depending on the form selected for use. | Test concluded and passed. | ![screenshot](documentation/features/add_garment_form.png)![screenshot](documentation/features/edit_garment_form.png) |
| | Add and Edit Garment Forms | The *Back to Garments* button is expected to return the user to the all designs page without saving any changes to the forms. | Tested the feature by clicking the *Back to Garments* button. | The feature behaved as expected, and returned the user to the all designs page. | Test concluded and passed. | ![screenshot](documentation/features/back_to_garments_button.png) |
| | Add and Edit Garment Forms | The *Add and Edit Garment* buttons are expected to submit the form and add a new garment or edit and existing garment. | Tested the feature by clicking the *Add and Edit Garment* buttons in turn after completing the forms. | The feature behaved as expected, and either added a new garment or edited and existing garment dependant on form selected and then returned the user to the garment page of the added or edited garment. | Test concluded and passed. | ![screenshot](documentation/features/add_garment_button.png) ![screenshot](documentation/features/edit_garment_button.png) |
| Add and Edit Category, Colour and Size | | | | | | |
| | Add and Edit Category Forms | The *Add and Edit Category* forms are expected to allow the admin of the site to add new or edit existing categories dependant on the selected. | Tested by completing each of forms in turn and clicking on the add or edit button on the form. | The features behaved as expected and either added new or edited existing categories based on the selected. | Test concluded and passed. | ![screenshot](documentation/features/add_category_form.png) ![screenshot](documentation/features/edit_category_form.png) |
| | Add and Edit Category Forms | The *Add and Edit Category* buttons are expected to submit the form and add a new category or edit and existing category. | Tested the feature by clicking the *Add and Edit Category* buttons in turn after completing the forms. | The feature behaved as expected, and either added a new category or edited and existing category dependant on form selected and then returned the user to the category selection page of the added or edited category. | Test concluded and passed. | ![screenshot](documentation/features/add_category_button.png) ![screenshot](documentation/features/edit_category_button.png) |
| | Add and Edit Colour Forms | The *Add and Edit Colour* forms are expected to allow the admin of the site to add new or edit existing colours dependant on the selected. | Tested by completing each of forms in turn and clicking on the add or edit button on the form. | The features behaved as expected and either added new or edited existing colours based on the selected. | Test concluded and passed. | ![screenshot](documentation/features/add_colour_form.png) ![screenshot](documentation/features/edit_colour_form.png) |
| | Add and Edit Colour Forms | The *Add and Edit Colour* buttons are expected to submit the form and add a new colour or edit and existing colour. | Tested the feature by clicking the *Add and Edit Colour* buttons in turn after completing the forms. | The feature behaved as expected, and either added a new colour or edited and existing colour dependant on form selected and then returned the user to the colour selection page of the added or edited colour. | Test concluded and passed. | ![screenshot](documentation/features/add_colour_button.png) ![screenshot](documentation/features/edit_colour_button.png) |
| | Add and Edit Size Forms | The *Add and Edit Size* forms are expected to allow the admin of the site to add new or edit existing sizes dependant on the selected. | Tested by completing each of forms in turn and clicking on the add or edit button on the form. | The features behaved as expected and either added new or edited existing sizes based on the selected. | Test concluded and passed. | ![screenshot](documentation/features/add_size_form.png) ![screenshot](documentation/features/edit_size_form.png) |
| | Add and Edit Size Forms | The *Add and Edit Size* buttons are expected to submit the form and add a new size or edit and existing size. | Tested the feature by clicking the *Add and Edit Size* buttons in turn after completing the forms. | The feature behaved as expected, and either added a new size or edited and existing size dependant on form selected and then returned the user to the size selection page of the added or edited size. | Test concluded and passed. | ![screenshot](documentation/features/add_size_button.png) ![screenshot](documentation/features/edit_size_button.png) |
| Edit Garment, Category, Colour and Size Selection | | | | | | |
| | Listed Item | The *Edit Category / Colour / Size* button is expected to open the respective edit page.| Tested the feature by clicking the *Edit Category / Colour / Size* button. | The feature behaved as expected, and opened the respective edit page. | Test concluded and passed. | ![screenshot](documentation/features/edit_garment_button.png) ![screenshot](documentation/features/edit_category_button.png) ![screenshot](documentation/features/edit_colour_button.png) ![screenshot](documentation/features/edit_size_button.png) |
| | Listed Item | The *Delete Category / Colour / Size* button is expected to open the respective delete confirmation modal.| Tested the feature by clicking the *Delete Category / Colour / Size* button. | The feature behaved as expected, and opened the respective delete confirmation modal. | Test concluded and passed. | ![screenshot](documentation/features/delete_garment_button.png) ![screenshot](documentation/features/delete_category_button.png) ![screenshot](documentation/features/delete_colour_button.png) ![screenshot](documentation/features/delete_size_button.png) |

</details>
